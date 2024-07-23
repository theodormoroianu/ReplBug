import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-37925"
LINK = "https://github.com/pingcap/tidb/issues/37925"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.3.0")

DESCRIPTION = """Duplicates in primary key do not throw an error"""

SETUP_SQL_SCRIPT = """
create table tbl_4 (
    col_16 decimal ( 38 , 4 )   not null ,
    col_17 time    default '23:52:24.00' ,
    col_18 char ( 235 ) collate utf8_bin ,
    col_19 tinyint  unsigned not null default 151 ,
    col_20 smallint    default 9203 ,
    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,
    key idx_8 ( col_18 ( 1 ) )
) charset utf8mb4 collate utf8mb4_bin ;

insert into tbl_4 values ( 661,'17:22:57.00','^0',155,-31298 );
insert into tbl_4 values ( 3579.0326,null,'n~KgM',220,-31136 );
insert into tbl_4 values ( 1.4,'05:06:55.00','Q+~(AUo!36S2OD9',35,-12681 );
insert into tbl_4 values ( 66.9,'10:04:39.00','_9ILR!QJ',145,-15820 );
insert into tbl_4 values ( 29082.6117,'00:37:01.00','mdTuS((uApbUxJIAO',196,-30900 );
insert into tbl_4 values ( 57,'11:09:40.00','=@%~n@w+9q',77,30926 );
insert into tbl_4 values ( 308382.06,null,'~Ewt)Z+1mlLzafKu',195,15880 );
insert into tbl_4 values ( 0.26,'03:32:16.00','_$lL2m0AFK9fQQs',178,-29720 );
insert into tbl_4 values ( 993.7,'10:14:55.00','m~a1nM(Xsf_#h7*',4,26689 );
insert into tbl_4 values ( 0.998,'19:57:45.00','I5Q8Xx1',66,-10830 );
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> update tbl_4 set tbl_4.col_17 = '11:16:44.00' ,tbl_4.col_17 = '03:51:50.00' ,tbl_4.col_16 = 9 where tbl_4.col_20 in ( -31298 ,-10876 ,-31136 ,-29720 ) and not( tbl_4.col_18 != 'n~KgM' ) ;
        conn_0> select col_20 from tbl_4 order by col_20;
        conn_0> commit;
        """,
        """
        conn_0> update tbl_4 set tbl_4.col_17 = '11:16:44.00' ,tbl_4.col_17 = '03:51:50.00' ,tbl_4.col_16 = 9 where tbl_4.col_20 in ( -31298 ,-10876 ,-31136 ,-29720 ) and not( tbl_4.col_18 != 'n~KgM' ) ;
        conn_0> select col_20 from tbl_4 order by col_20;
        """,
    ]
