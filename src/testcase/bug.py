import database.config as db_config
import pathlib
from typing import Optional
import logging
from context import Context
import testcase.testcase_runner as testcase_runner


def parse_instructions(instructions: str) -> list[testcase_runner.Instruction]:
    """
    Parses a string containing instructions running on multiple connections.

    Sample:
    conn_1> BEGIN OPTIMISTIC;
    conn_0> BEGIN OPTIMISTIC;
    conn_1> insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu0, c_slu2bd) values
            (182, 264000, null, 'biiumc', null, 'dwzl6d', 93.90, null);
    conn_0> insert into a values (1);
    """
    result = []
    last, conn_last = "", -1

    for line in instructions.split("\n"):
        line = line.strip()
        if line == "":
            continue
        if line.startswith("conn_"):
            if last != "":
                result.append(testcase_runner.Instruction(conn_last, last))
                last = ""

            prefix, command = line.split(">", 1)
            last = command
            conn_last = int(prefix.split("_")[1])
        else:
            last += " " + line

    if last != "":
        result.append(testcase_runner.Instruction(conn_last, last))

    return result


class Bug:
    """
    This class represents a discovered bug.
    """

    def __init__(
        self,
        bug_id: str,
        description: str,
        db_and_type: db_config.DatabaseTypeAndVersion,
        scenarios: list[str],
        setup_sql_script: Optional[pathlib.Path] = None,
    ):
        self.bug_id = bug_id
        self.description = description
        self.db_and_type = db_and_type
        self.scenarios = scenarios
        self.setup_sql_script = setup_sql_script
        self.testcase_runners: list[testcase_runner.TestcaseRunner] = []

    def _save_result_from_user(self):
        """
        Saves the result of the bug from the user
        """
        file = (
            Context.get_context().data_folder_path
            / "results"
            / f"{self.bug_id}_result.md"
        )
        file.parent.mkdir(parents=True, exist_ok=True)

        result = [
            f"# Bug ID {self.bug_id}",
            "",
            f"## Description",
            self.description,
            "",
            "## Details",
            f" * Database: {self.db_and_type}",
            f" * Number of scenarios: {len(self.scenarios)}",
            f" * Initial setup script: {self.setup_sql_script}",
            "",
            "## Results",
        ]
        for nr, runner in enumerate(self.testcase_runners):
            result.append(f"### Scenario {nr}")
            for nr_instr, instr in enumerate(runner.instructions):
                result.append(f" * Instruction #{nr_instr}:")
                sql = instr.instruction.replace("\n", " ").replace("  ", " ")
                if len(sql) > 80:
                    sql = sql[:80] + "..."
                result.append(f"     - SQL: {sql}")
                result.append(f"     - TID: {instr.transaction_id}")
                result.append(f"     - Output: {instr.output}")
            result.append("")
            result.append(" * Container logs:")
            container_logs = [
                "   > " + i
                for i in runner.db_server_logs.split("\n")
                if i.strip() != ""
            ]
            if container_logs != []:
                result += container_logs + [""]
            else:
                result += ["   No logs available.", ""]

        with open(file, "w") as f:
            f.write("\n".join(result))
        print(f"\n          Result saved in {file}.")
        logging.info(f"Result for {self.bug_id} saved in {file}.")

    def run(self):
        """
        Runs the buggy scenarios
        """
        logging.info(f"Running bug {self.bug_id} on {self.db_and_type}")
        print(f"Running bug {self.bug_id} on {self.db_and_type}: ", end="", flush=True)

        pre_run_instruction = []
        if self.setup_sql_script:
            data = open(self.setup_sql_script).read()
            pre_run_instruction = [testcase_runner.Instruction(None, data)]

        for nr, scenario_content in enumerate(self.scenarios):
            print(f" Scenario #{nr}...", end="", flush=True)
            runner = testcase_runner.TestcaseRunner(
                name=f"{self.bug_id} - Scenario {nr}",
                instructions=parse_instructions(scenario_content),
                db_and_type=self.db_and_type,
                pre_run_instructions=pre_run_instruction,
            )
            runner.run()
            self.testcase_runners.append(runner)
            print(" Done    ", end="", flush=True)

        self._save_result_from_user()
