import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-94338"
LINK = "https://bugs.mysql.com/bug.php?id=94338"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.25"
)

SETUP_SQL_SCRIPT = """
CREATE TABLE `t1` (
  `a_id` bigint(20) NOT NULL,
  `b_id` bigint(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE `t2` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `a_id` bigint(20) NOT NULL,
  `b_id` bigint(20) NOT NULL,
  `c_code` char(1) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `c_id` bigint(20) NOT NULL,
  `state` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `secondary` (`a_id`,`b_id`,`c_code`,`c_id`,`state`)
) ENGINE=InnoDB;

INSERT INTO t1 (a_id, b_id) VALUES (1,18), (1,19);

INSERT INTO t2 (a_id, b_id, c_code, c_id, state) VALUES
  (1,18,'B',10,1),
  (1,19,'B',10,1),
  (1,20,'B',10,1),
  (1,21,'B',10,1),
  (1,18,'B',11,0),
  (1,19,'B',11,0),
  (1,20,'B',11,0),
  (1,21,'B',11,0),
  (1,18,'C',12,1),
  (1,19,'C',12,1),
  (1,21,'C',12,1),
  (1,18,'C',13,1);
"""

DESCRIPTION = "Dirty read-like behavior in transaction"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_1> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> ANALYZE TABLE t1, t2;

        conn_0> BEGIN;
        conn_1> BEGIN;

        conn_0> SELECT t1.b_id
                FROM t1
                WHERE (
                    t1.a_id = 1
                    AND IFNULL(1 = (
                    SELECT state
                    FROM t2 FORCE INDEX(secondary)
                    WHERE
                        a_id = 1
                        AND b_id = t1.b_id
                        AND ((c_code = 'A' AND c_id = 11) OR (c_code = 'B' AND c_id = 11))
                    ORDER BY state LIMIT 1), 1))
                LIMIT 10;

        conn_1> INSERT INTO t2 (a_id, b_id, c_code, c_id, state) VALUES
                (1,22,'B',10,1),
                (1,23,'B',10,1),
                (1,24,'B',10,1),
                (1,25,'B',10,1),
                (1,26,'B',10,1),
                (1,27,'B',10,1),
                (1,28,'B',10,1),
                (1,29,'B',10,1),
                (1,30,'B',10,1),
                (1,31,'B',10,1),
                (1,32,'B',10,1),
                (1,33,'B',10,1),
                (1,34,'B',10,1),
                (1,35,'B',10,1),
                (1,36,'B',10,1),
                (1,37,'B',10,1),
                (1,38,'B',10,1),
                (1,39,'B',10,1),
                (1,40,'B',10,1),
                (1,41,'B',10,1),
                (1,42,'B',10,1),
                (1,43,'B',10,1),
                (1,44,'B',10,1),
                (1,45,'B',10,1),
                (1,46,'B',10,1),
                (1,22,'B',11,0),
                (1,23,'B',11,0),
                (1,24,'B',11,0),
                (1,25,'B',11,0),
                (1,26,'B',11,0),
                (1,27,'B',11,0),
                (1,28,'B',11,0),
                (1,29,'B',11,0),
                (1,30,'B',11,0),
                (1,31,'B',11,0),
                (1,32,'B',11,0),
                (1,33,'B',11,0),
                (1,34,'B',11,0),
                (1,35,'B',11,0),
                (1,36,'B',11,0),
                (1,37,'B',11,0),
                (1,38,'B',11,0),
                (1,39,'B',11,0),
                (1,40,'B',11,0),
                (1,41,'B',11,0),
                (1,42,'B',11,0),
                (1,43,'B',11,0),
                (1,44,'B',11,0),
                (1,45,'B',11,0),
                (1,46,'B',11,0),
                (1,23,'C',12,1),
                (1,25,'C',12,1),
                (1,26,'C',12,1),
                (1,29,'C',12,1),
                (1,32,'C',12,1),
                (1,34,'C',12,1),
                (1,35,'C',12,1),
                (1,36,'C',12,1),
                (1,37,'C',12,1),
                (1,38,'C',12,1),
                (1,39,'C',12,1),
                (1,42,'C',12,1),
                (1,43,'C',12,1),
                (1,44,'C',12,1),
                (1,46,'C',12,1),
                (1,28,'C',13,1),
                (1,29,'C',13,1),
                (1,31,'C',13,1),
                (1,33,'C',13,1),
                (1,35,'C',13,1),
                (1,36,'C',13,1),
                (1,38,'C',13,1),
                (1,39,'C',13,1),
                (1,43,'C',13,1),
                (1,46,'C',14,1),
                (1,22,'C',15,1),
                (1,24,'C',15,1),
                (1,27,'C',15,1),
                (1,28,'C',15,1),
                (1,30,'C',15,1),
                (1,31,'C',15,1),
                (1,33,'C',15,1),
                (1,40,'C',15,1),
                (1,41,'C',15,1),
                (1,45,'C',15,1),
                (1,24,'C',16,1),
                (1,26,'C',16,1),
                (1,27,'C',16,1),
                (1,34,'C',16,1),
                (1,40,'C',16,1),
                (1,42,'C',16,1);

        conn_0> SELECT t1.b_id
                FROM t1
                WHERE (
                    t1.a_id = 1
                    AND IFNULL(1 = (
                    SELECT state
                    FROM t2 FORCE INDEX(secondary)
                    WHERE
                        a_id = 1
                        AND b_id = t1.b_id
                        AND ((c_code = 'A' AND c_id = 11) OR (c_code = 'B' AND c_id = 11))
                    ORDER BY state LIMIT 1), 1))
                LIMIT 10;

        conn_1> COMMIT;

        conn_0> SELECT t1.b_id
                FROM t1
                WHERE (
                    t1.a_id = 1
                    AND IFNULL(1 = (
                    SELECT state
                    FROM t2 FORCE INDEX(secondary)
                    WHERE
                        a_id = 1
                        AND b_id = t1.b_id
                        AND ((c_code = 'A' AND c_id = 11) OR (c_code = 'B' AND c_id = 11))
                    ORDER BY state LIMIT 1), 1))
                LIMIT 10;
        """,
    ]
