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

    def save_result_from_user(self):
        """
        Saves the result of the bug from the user
        """
        file = Context.get_context().data_folder_path / "results" / f"{self.bug_id}_result.md"
        file.parent.mkdir(parents=True, exist_ok=True)

        print("Saving results...")
        if file.exists():
            print("Result file already exists:")
            content = open(file).readlines()
            content = [" > " + i for i in content]
            print("".join(content))
            print("Do you want to overwrite it? (y/n)")
            answer = input("> ")
            if answer.lower() != "y":
                return
        
        print("Please enter the result of the bug (CRL+C to stop):")
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
        print("\n".join(["# " + i for i in result]))
        while True:
            try:
                line = input("# ")
                result.append(line)
            except KeyboardInterrupt:
                break
        
        with open(file, "w") as f:
            f.write("\n".join(result))
        print(f"Result saved in {file}.")
        logging.info(f"Result for {self.bug_id} saved in {file}.")

    def run(self):
        """
        Runs the buggy scenarios
        """
        logging.info(f"Running bug {self.bug_id} on {self.db_and_type}")
        print(f"Running bug {self.bug_id} on {self.db_and_type}")

        pre_run_instruction = []
        if self.setup_sql_script:
            data = open(self.setup_sql_script).read()
            pre_run_instruction = [testcase_runner.Instruction(None, data)]
        print(f"Pre-run instructions: {'Yes' if pre_run_instruction else 'No'}")

        for nr, scenario_content in enumerate(self.scenarios):
            print(f"Running scenario #{nr}...")
            runner = testcase_runner.TestcaseRunner(
                name=f"{self.bug_id} - Scenario {nr}",
                instructions=parse_instructions(scenario_content),
                db_and_type=self.db_and_type,
                pre_run_instructions=pre_run_instruction
            )
            try:
                runner.run()
            except Exception as e:
                print(f"Error running scenario {nr}: {e}")
                logging.error(f"Error running scenario {nr}: {e}")
        
        self.save_result_from_user()