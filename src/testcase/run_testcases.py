import database.config as db_config
import testcase.testcase_runner as testcase_runner


def run():
    instructions = [
        testcase_runner.Instruction(1, "CREATE DATABASE testdb;",      False),
        testcase_runner.Instruction(1, "USE testdb;",                  False),
        testcase_runner.Instruction(1, "CREATE TABLE t (id INT);",     False),
        testcase_runner.Instruction(1, "INSERT INTO t VALUES (1);",    False),
        testcase_runner.Instruction(1, "SET AUTOCOMMIT = ON;",         False),
        testcase_runner.Instruction(1, "BEGIN;",                       False),
        testcase_runner.Instruction(1, "SELECT * FROM t;",             True),
        testcase_runner.Instruction(1, "update t set id = id+1;",      False),
        testcase_runner.Instruction(1, "SELECT * FROM t;",             True),
        testcase_runner.Instruction(1, "SET AUTOCOMMIT = ON;",         False),
        testcase_runner.Instruction(1, "ROLLBACK;",                    False),
        testcase_runner.Instruction(1, "SELECT * FROM t;",             True),
    ]

    test = testcase_runner.TestcaseRunner(
        "Test",
        1,
        instructions,
        db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "6.2.0")
    )

    test.run()