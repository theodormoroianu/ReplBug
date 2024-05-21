"""
Parses a string containing instructions running on multiple connections.

Sample:
conn_1> BEGIN OPTIMISTIC;
conn_0> BEGIN OPTIMISTIC;
conn_1> insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu0, c_slu2bd) values
          (182, 264000, null, 'biiumc', null, 'dwzl6d', 93.90, null);
conn_0> insert into a values (1);
"""

import testcase.testcase as testcase

def parse_instructions(instructions: str) -> list[testcase.Instruction]:
    """
    Parses a string containing instructions running on multiple connections.

    :param instructions: The instructions to parse.
    :return: A list of instructions.
    """
    result = []
    last, conn_last = "", -1

    for line in instructions.split("\n"):
        if line.strip() == "":
            continue
        if line.startswith("conn_"):
            if last != "":
                result.append(testcase.Instruction(conn_last, last))
                last = ""
            
            prefix, command = line.split(">", 1)
            last = command
            conn_last = int(prefix.split("_")[1])
        else:
            last += line
    
    if last != "":
        result.append(testcase.Instruction(conn_last, last))

    return result
