import database.config as db_config
import testcase.testcase as testcase

def run():
    instructions = [
        testcase.Instruction(1, "CREATE DATABASE testdb;",      False),
        testcase.Instruction(1, "USE testdb;",                  False),
        testcase.Instruction(1, "CREATE TABLE t (id INT);",     False),
        testcase.Instruction(1, "INSERT INTO t VALUES (1);",    False),
        testcase.Instruction(1, "SET AUTOCOMMIT = ON;",         False),
        testcase.Instruction(1, "BEGIN;",                       False),
        testcase.Instruction(1, "SELECT * FROM t;",             True),
        testcase.Instruction(1, "update t set id = id+1;",      False),
        testcase.Instruction(1, "SELECT * FROM t;",             True),
        testcase.Instruction(1, "SET AUTOCOMMIT = ON;",         False),
        testcase.Instruction(1, "ROLLBACK;",                    False),
        testcase.Instruction(1, "SELECT * FROM t;",             True),
    ]

    test = testcase.Testcase(
        "Test",
        1,
        instructions,
        db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "6.2.0")
    )

    test.run()