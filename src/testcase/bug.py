"""
This module exposes the "Bug" class, which is responsible for running a bug on a database.
It handles multiple scenarios, where different SQL instructions are being ran, and saves the
result in a file.

It relies on the "TestcaseRunner" class to run the scenarios.
"""

import database.config as db_config
import pathlib
from typing import Optional
import logging
from context import Context
from testcase.helpers import Instruction
import testcase.testcase_runner as testcase_runner


def _parse_instructions(instructions: str) -> list[Instruction]:
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
    instruction_str, conn_last = "", -1
    nr_instr = 0

    for line in instructions.split("\n"):
        line = line.strip()
        if line == "":
            continue
        if line.startswith("conn_"):
            if instruction_str != "":
                result.append(testcase_runner.Instruction(conn_last, nr_instr, instruction_str))
                instruction_str = ""
                nr_instr += 1

            prefix, command = line.split(">", 1)
            instruction_str = command
            conn_last = int(prefix.split("_")[1])
        else:
            instruction_str += " " + line

    if instruction_str != "":
        result.append(testcase_runner.Instruction(conn_last, nr_instr, instruction_str))

    return result

def _compute_execution_order(instructions: list[Instruction]) -> list[Optional[int]]:
    """
    Computes the execution order of the instructions. It relies on the time the instruction
    was executed.
    """
    execution_times = sorted([
        (i.executed_time, idx)
        for idx, i in enumerate(instructions)
        if i.executed_time is not None
    ])

    answer = [None for _ in instructions]

    for idx, (_, i) in enumerate(execution_times):
        answer[i] = idx

    return answer


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
        setup_sql_script: Optional[str] = None,
        is_valid: bool = True,
    ):
        """
        Creates a new bug.

        :param bug_id: The ID of the bug (e.g. "TIDB-1234").
        :param description: The description of the bug (basic info on the bug).
        :param db_and_type: The database and the version on which the bug should be replicable.
        :param scenarios: A list of scenarios used for detecting the bug.
        :param setup_sql_script: The SQL script used for setting up the environment.
        :param is_valid: If the bug is valid or not (if we are able to replicate it or not).
        """
        self.bug_id = bug_id
        self.description = description
        self.db_and_type = db_and_type
        self.scenarios = scenarios
        self.setup_sql_script = setup_sql_script
        self.testcase_runners: list[testcase_runner.TestcaseRunner] = []
        self.is_valid = is_valid

    def _save_result_from_user(self):
        """
        Saves the result of the bug from the user
        """
        file = (
            Context.get_context().data_folder_path
            / ("results" if self.is_valid else "invalid_results")
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
            f" * Initial setup script: {"Yes" if self.setup_sql_script else "No"}",
            "",
            "## Results",
        ]
        for nr, runner in enumerate(self.testcase_runners):
            result.append(f"### Scenario {nr}")
            execution_order = _compute_execution_order(runner.runned_instructions)
            for nr_instr, instr in enumerate(runner.runned_instructions):
                result.append(f" * Instruction #{nr_instr}:")
                sql = instr.instruction.replace("\n", " ").replace("  ", " ")
                if len(sql) > 80:
                    sql = sql[:80] + "..."
                result.append(f"     - Instruction: {sql}")
                result.append(f"     - Transaction: conn_{instr.transaction_id}")
                result.append(f"     - Output: {instr.output}")
                result.append(f"     - Executed order: {execution_order[nr_instr] if execution_order[nr_instr] is not None else 'Not executed'}")
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
            pre_run_instruction = [
                testcase_runner.Instruction(None, None, self.setup_sql_script)
            ]

        for nr, scenario_content in enumerate(self.scenarios):
            print(f" Scenario #{nr}...", end="", flush=True)
            runner = testcase_runner.TestcaseRunner(
                name=f"{self.bug_id} - Scenario {nr}",
                instructions=_parse_instructions(scenario_content),
                db_and_type=self.db_and_type,
                pre_run_instructions=pre_run_instruction,
            )
            runner.run()
            self.testcase_runners.append(runner)
            print(" Done    ", end="", flush=True)

        self._save_result_from_user()
