import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29081"
LINK = "https://jira.mariadb.org/browse/MDEV-29081"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)

DESCRIPTION = "Sometimes a different number of results are returned by SELECT."

# Need to restart the server after each request.
KILL_SERVER_AFTER_TESTCASE = True

op = """
conn_0> 
START TRANSACTION;
conn_0> 
START TRANSACTION;
conn_0> 
START TRANSACTION;
conn_0> 
START TRANSACTION;
conn_0> 
delete from t__cwzpb
where 
t__cwzpb.c__xujbd is not NULL;
conn_0> 
update t_khn17c set 
  wkey = 187, 
  c_ci0ked = coalesce(case when 54 <= t_khn17c.pkey then null else PI() end
      ,
    TRUNCATE(
      case when exists (
          select  
              ref_3.c_3eervc as c0, 
              ref_3.c_enxa7 as c1, 
              ref_3.c_abxjed as c2, 
              ref_3.c_hs9pic as c3, 
              ref_3.c__xujbd as c4, 
              ref_3.c_nagjcb as c5, 
              69 as c6
            from 
              t__cwzpb as ref_3
            where ref_3.pkey between ref_3.wkey and ref_3.c_vlrpid
            order by c0, c1, c2, c3, c4, c5, c6 asc) then PI() else case when t_khn17c.c_qdo5gb between 4 and 62 then PI() else 4.55 end
           end
        ,
      coalesce(case when 32 < 14 then STRCMP(
            'jnlvwb',
            null) else 25 end
          ,
        length(
          coalesce('jonut',
            '18wdg')))))
where t_khn17c.wkey = case when t_khn17c.wkey is not NULL then t_khn17c.wkey else case when (t_khn17c.c_ci0ked > ( 
          select  
              ref_0.c_cgzhhc as c0
            from 
              (t_2nqc_c as ref_0
                inner join t_2nqc_c as ref_1
                on (ref_0.pkey = ref_1.wkey ))
            where 1 = 1)) 
        and ((t_khn17c.c_qdo5gb between t_khn17c.wkey and t_khn17c.pkey) 
          and (t_khn17c.wkey >= ( 
            select  
                ref_2.c_rpekod as c0
              from 
                t_2nqc_c as ref_2
              where t_khn17c.wkey > ref_2.wkey))) then 2 else t_khn17c.wkey end
       end
    ;
conn_0> 
START TRANSACTION;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
update t_khn17c set 
  wkey = 231, 
  c_ci0ked = 78.57, 
  c_qdo5gb = t_khn17c.pkey
where t_khn17c.c_ci0ked in (
  t_khn17c.c_ci0ked, PI(), t_khn17c.c_ci0ked, t_khn17c.c_ci0ked, case when ((t_khn17c.c_qdo5gb <= t_khn17c.c_qdo5gb) 
        and ('__9uhc' like '_bsfh%' and t_khn17c.wkey > t_khn17c.pkey or t_khn17c.c_qdo5gb > t_khn17c.wkey)) 
      or ((t_khn17c.c_ci0ked in (
            t_khn17c.c_ci0ked, t_khn17c.c_ci0ked, t_khn17c.c_ci0ked) or t_khn17c.c_qdo5gb = ( 
            select  
                ref_0.c_fq8z_ as c0
              from 
                t_2nqc_c as ref_0
              where ref_0.c_cgzhhc is not NULL or ref_0.c_tu2dv in (
                    select  
                          ref_1.c_3eervc as c0
                        from 
                          t__cwzpb as ref_1
                        where ref_1.c_vlrpid between ref_1.wkey and ref_1.c_vlrpid
                      union
                      select  
                          ref_2.c_hzulvc as c0
                        from 
                          t_2nqc_c as ref_2
                        where exists (
                          select  
                              ref_3.c_ywpeyc as c0, 
                              ref_3.c_ywpeyc as c1, 
                              ref_2.c_cgzhhc as c2, 
                              ref_3.c_cgzhhc as c3, 
                              ref_3.c_6udum as c4, 
                              ref_2.c_hzulvc as c5, 
                              ref_3.c_fq8z_ as c6, 
                              ref_2.pkey as c7, 
                              ref_3.c_hzulvc as c8, 
                              ref_3.c_6udum as c9, 
                              37 as c10, 
                              ref_3.c_ijrc5 as c11, 
                              ref_3.c_tu2dv as c12, 
                              ref_3.c_ijrc5 as c13, 
                              ref_3.c_fq8z_ as c14, 
                              ref_3.wkey as c15
                            from 
                              t_2nqc_c as ref_3
                            where (ref_3.c_6udum < ref_3.c_rpekod) 
                              or ((ref_3.pkey = ref_3.c_ijrc5) 
                                  and (ref_2.c_6udum <> ref_3.wkey) and 49 <> ref_3.c_rpekod))) or ((ref_0.wkey <> ref_0.c_fq8z_) 
                      and (ref_0.pkey < ( 
                        select distinct 
                            ref_4.c_rpekod as c0
                          from 
                            t_2nqc_c as ref_4
                          where 1 = 1
                          window w_m48oad as ( partition by t_khn17c.wkey order by ref_4.c_fq8z_ desc)))) 
                    and (t_khn17c.pkey > t_khn17c.wkey) and ref_0.c_ijrc5 < t_khn17c.c_qdo5gb
              window w_dpjs_ as ( partition by t_khn17c.c_ci0ked order by ref_0.pkey asc))) is NULL) then t_khn17c.c_ci0ked else case when 'gsp8vb' not like 'd_easc' then t_khn17c.c_ci0ked else t_khn17c.c_ci0ked end
       end
    );
conn_0> 
select  
  ref_0.wkey as c0, 
  ref_0.pkey as c1, 
  ref_0.c_hzulvc as c2, 
  ref_0.c_6udum as c3, 
  ref_0.c_tu2dv as c4, 
  ref_0.c_ywpeyc as c5, 
  ref_0.c_rdjvb as c6, 
  ref_0.c_ijrc5 as c7, 
  ref_0.c_cgzhhc as c8, 
  ref_0.c_fq8z_ as c9, 
  ref_0.c_rpekod as c10
from 
  t_2nqc_c as ref_0
where (ref_0.c_ijrc5 > ref_0.wkey) 
  and (ref_0.c_rpekod between ref_0.c_6udum and ref_0.c_rpekod or ref_0.c_ijrc5 < ref_0.c_rpekod);
conn_0> 
select  
  ref_0.wkey as c0, 
  ref_0.pkey as c1, 
  ref_0.c__xujbd as c2, 
  ref_0.c_hs9pic as c3, 
  ref_0.c_vlrpid as c4, 
  ref_0.c_nagjcb as c5, 
  ref_0.c_4fqqwd as c6, 
  ref_0.c_vjulib as c7, 
  ref_0.c_3eervc as c8, 
  ref_0.c_enxa7 as c9, 
  ref_0.c_abxjed as c10
from 
  t__cwzpb as ref_0
where exists (
  select  
      ref_0.c_enxa7 as c0, 
      ref_1.c_qdo5gb as c1, 
      ref_0.c_3eervc as c2
    from 
      t_khn17c as ref_1
    where '5zi0yd' not like 'kb_bg');
conn_0> 
update t_khn17c set 
  wkey = 239, 
  c_qdo5gb = t_khn17c.pkey
where exists (
    select  
        ref_0.c_vlrpid as c0, 
        ref_0.c__xujbd as c1
      from 
        t__cwzpb as ref_0
      where ref_0.c_hs9pic < ref_0.pkey) and t_khn17c.c_qdo5gb > 58;
conn_0> 
ROLLBACK;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
WITH 
cte_0 AS (select  
    ref_0.wkey as c0, 
    ref_0.pkey as c1, 
    ref_0.c_ci0ked as c2, 
    ref_0.c_qdo5gb as c3
  from 
    t_khn17c as ref_0
  where CRC32(
      ELT(
        ref_0.c_qdo5gb,
        substr(
          case when ref_0.pkey <> ref_0.c_qdo5gb then 'utnasb' else 'o_dcfd' end
            ,
          (ref_0.wkey / ref_0.c_qdo5gb),
          ref_0.pkey),
        (('rbx5w' || 'ecogp') || EXPORT_SET(
            ref_0.c_qdo5gb,
            'hmbru',
            '76yc_c',
            'u3zxuc',
            ref_0.c_qdo5gb)),
        case when ref_0.pkey is not NULL then (null || '1_2xmb') else case when ref_0.pkey > ( 
              select  
                    ref_1.wkey as c0
                  from 
                    t_khn17c as ref_1
                  where ref_0.c_qdo5gb not in (
                    ref_0.wkey, ref_0.wkey)
                union all
                select  
                    49 as c0
                  from 
                    t_2nqc_c as ref_2
                  where (ref_2.c_ijrc5 <> ref_0.c_qdo5gb) 
                    and ((exists (
                        select  
                            ref_3.c_3eervc as c0, 
                            ref_0.wkey as c1
                          from 
                            t__cwzpb as ref_3
                          where 1 = 1 and ref_2.c_fq8z_ < ref_2.c_rpekod
                          order by c0, c1 asc)) 
                      or (ref_2.pkey between ref_0.pkey and ref_2.pkey))) then 'urhoi' else 'qlzglb' end
             end
          )) <= ref_0.pkey), 

cte_1 AS (select  
    ref_4.wkey as c0, 
    ref_4.pkey as c1, 
    ref_4.c_hzulvc as c2, 
    ref_4.c_6udum as c3, 
    ref_4.c_tu2dv as c4, 
    ref_4.c_ywpeyc as c5, 
    ref_4.c_rdjvb as c6, 
    ref_4.c_ijrc5 as c7, 
    ref_4.c_cgzhhc as c8, 
    ref_4.c_fq8z_ as c9, 
    ref_4.c_rpekod as c10
  from 
    t_2nqc_c as ref_4
  where (ref_4.c_rdjvb like 'i%_pzd') 
    and ((ref_4.c_ijrc5 between ref_4.c_6udum and ref_4.pkey) 
        or (ref_4.c_6udum is not NULL) or ref_4.c_6udum = ref_4.c_6udum)), 

cte_2 AS (select distinct 
    ref_5.wkey as c0, 
    ref_5.pkey as c1, 
    ref_5.c__xujbd as c2, 
    ref_5.c_hs9pic as c3, 
    ref_5.c_vlrpid as c4, 
    ref_5.c_nagjcb as c5, 
    ref_5.c_4fqqwd as c6, 
    ref_5.c_vjulib as c7, 
    ref_5.c_3eervc as c8, 
    ref_5.c_enxa7 as c9, 
    ref_5.c_abxjed as c10
  from 
    t__cwzpb as ref_5
  where case when ref_5.c_3eervc not like '_elc%c' then ref_5.wkey else case when ref_5.c_vlrpid <= ref_5.wkey then ref_5.pkey else ref_5.c_hs9pic end
         end
       <= ref_5.c_vlrpid), 

cte_3 AS (select distinct 
    ref_6.wkey as c0, 
    ref_6.pkey as c1, 
    ref_6.c_hzulvc as c2, 
    ref_6.c_6udum as c3, 
    ref_6.c_tu2dv as c4, 
    ref_6.c_ywpeyc as c5, 
    ref_6.c_rdjvb as c6, 
    ref_6.c_ijrc5 as c7, 
    ref_6.c_cgzhhc as c8, 
    ref_6.c_fq8z_ as c9, 
    ref_6.c_rpekod as c10
  from 
    t_2nqc_c as ref_6
  where (ref_6.c_6udum between ref_6.c_rpekod and ref_6.c_ijrc5) 
    and (ref_6.c_rdjvb < ( 
      select  
          ref_7.c_rdjvb as c0
        from 
          t_2nqc_c as ref_7
        where (1 = 1 or ref_6.wkey between ref_6.c_rpekod and ref_7.c_6udum or ref_6.c_fq8z_ <> ref_6.pkey) 
          and ((ref_7.c_ijrc5 > ref_7.c_rpekod) 
            and (ref_7.c_fq8z_ < ref_7.c_rpekod))
        order by c0 asc))), 

cte_4 AS (select distinct 
    ref_8.wkey as c0, 
    ref_8.pkey as c1, 
    ref_8.c__xujbd as c2, 
    ref_8.c_hs9pic as c3, 
    ref_8.c_vlrpid as c4, 
    ref_8.c_nagjcb as c5, 
    ref_8.c_4fqqwd as c6, 
    ref_8.c_vjulib as c7, 
    ref_8.c_3eervc as c8, 
    ref_8.c_enxa7 as c9, 
    ref_8.c_abxjed as c10
  from 
    t__cwzpb as ref_8
  where case when 1 = 1 then ref_8.c_vlrpid else ref_8.c_vlrpid end
       <= ref_8.wkey)
select  
    ref_9.wkey as c0, 
    ref_9.pkey as c1, 
    ref_9.c_ci0ked as c2, 
    ref_9.c_qdo5gb as c3
  from 
    t_khn17c as ref_9
  where 83 between (case when ref_9.pkey > ref_9.pkey then ROUND(
          ref_9.c_ci0ked) else ref_9.wkey end
         + ref_9.wkey) and ref_9.pkey
;
conn_0> 
update t_khn17c set 
  wkey = 158, 
  c_ci0ked = PI(), 
  c_qdo5gb = t_khn17c.pkey
where t_khn17c.pkey = t_khn17c.pkey;
conn_0> 
insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values 
(82, 152000, PI(), 54), 
(82, 153000, 31.33, 25), 
(82, 154000, 69.83, case when 'rwm_7d' like 'qcp%cc' then 18 else (95 % 52) end
  ), 
(82, 155000, 94.1, case when 64 not in (
    select  
          ref_0.pkey as c0
        from 
          ((t_2nqc_c as ref_0
              cross join t_2nqc_c as ref_1
              )
            left outer join t_2nqc_c as ref_2
            on (ref_1.c_ywpeyc = ref_2.c_hzulvc ))
        where (ref_2.c_ijrc5 < ref_1.c_6udum) 
          or (ref_1.c_ijrc5 <= ref_0.c_6udum)
      union
      select distinct 
          63 as c0
        from 
          t_2nqc_c as ref_3
        where ref_3.c_cgzhhc in (
          ref_3.c_cgzhhc, ref_3.c_cgzhhc, ref_3.c_cgzhhc)) then 1 else 6 end
  ), 
(82, 156000, 22.86, 39), 
(82, 157000, 3.73, case when exists (
    select  
        ref_6.pkey as c0, 
        ref_5.c_vjulib as c1
      from 
        ((t_2nqc_c as ref_4
            cross join t__cwzpb as ref_5
            )
          cross join t__cwzpb as ref_6
          )
      where 68 >= ref_4.c_6udum and 1 = 1) then (3 + (45 - 67)) else 50 end
  ), 
(82, 158000, PI(), 78), 
(82, 159000, 98.62, 40);
conn_0> 
insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values 
(93, 219000, 8.29, (case when ROUND(
        24.77) between 16 and 30 then 53 else (case when 8 <= 92 then 60 else 77 end
         >> 99) end
     - 90)), 
(93, 220000, 56.41, (33 >> 13)), 
(93, 221000, 12.2, 6), 
(93, 222000, 82.83, 44);
conn_0> 
update t_khn17c set 
  wkey = 96, 
  c_qdo5gb = t_khn17c.pkey
where t_khn17c.wkey between t_khn17c.c_qdo5gb and t_khn17c.wkey;
conn_0> 
delete from t_khn17c
where 
t_khn17c.wkey >= case when t_khn17c.pkey between t_khn17c.pkey and (t_khn17c.pkey + case when t_khn17c.c_qdo5gb in (
            select  
                ref_0.c_ijrc5 as c0
              from 
                t_2nqc_c as ref_0
              where ((41 = ref_0.c_fq8z_) 
                  or (ref_0.pkey between ref_0.c_rpekod and ref_0.c_ijrc5)) 
                or (ref_0.c_6udum >= ref_0.pkey)) then t_khn17c.wkey else t_khn17c.c_qdo5gb end
          ) then t_khn17c.wkey else t_khn17c.c_qdo5gb end
    ;
conn_0> 
update t_khn17c set 
  wkey = 119, 
  c_qdo5gb = t_khn17c.pkey
where 1 = 1 and (t_khn17c.pkey <> coalesce(t_khn17c.c_qdo5gb,
          t_khn17c.wkey)) 
      or ((1 = 1 and t_khn17c.pkey = t_khn17c.c_qdo5gb) 
        and (t_khn17c.wkey <> t_khn17c.pkey)) or (t_khn17c.c_qdo5gb in (
        select  
            ref_0.c_hs9pic as c0
          from 
            t__cwzpb as ref_0
          where 83 >= ref_0.pkey
          window w_brig2c as ( partition by ref_0.c_vlrpid,ref_0.c_enxa7 order by ref_0.c_4fqqwd,ref_0.c_vjulib asc)
          order by c0 asc)) 
      and (t_khn17c.c_ci0ked in (
        select  
            ref_1.c_cgzhhc as c0
          from 
            t_2nqc_c as ref_1
          where 1 = 1));
conn_0> 
delete from t_2nqc_c
where 
t_2nqc_c.c_ijrc5 not in (
  t_2nqc_c.pkey, CHAR_LENGTH(
    t_2nqc_c.c_hzulvc));
conn_0> 
ROLLBACK;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
delete from t__cwzpb
where 
t__cwzpb.c_vjulib is NULL;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
ROLLBACK;
conn_0> 
COMMIT;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enxa7, c_abxjed) values 
(263, 467000, 6.49, 42, 94.50, 'qd15xb', nullif(PI(),
  35.19), PI()), 
(263, 468000, case when PI() in (
    select  
          ref_0.c_ci0ked as c0
        from 
          t_khn17c as ref_0
        where ref_0.wkey > ref_0.pkey
      union
      select distinct 
          abs(
            ref_1.c_cgzhhc) as c0
        from 
          t_2nqc_c as ref_1
        where (ref_1.c_rpekod is not NULL) 
          and ((ref_1.pkey between ref_1.c_ijrc5 and ref_1.c_rpekod) 
            or (exists (
                select  
                    ref_2.c_hzulvc as c0
                  from 
                    t_2nqc_c as ref_2
                  where exists (
                    select  
                        ref_3.c_qdo5gb as c0, 
                        ref_3.c_ci0ked as c1, 
                        ref_3.c_qdo5gb as c2, 
                        ref_3.c_qdo5gb as c3
                      from 
                        t_khn17c as ref_3
                      where 0 <> 0)
                  window w_znevgd as ( partition by ref_1.c_ijrc5,ref_2.c_tu2dv order by ref_2.pkey desc)) or ref_1.pkey between ref_1.c_fq8z_ and ref_1.c_fq8z_))
        window w_rx1ydd as ( partition by ref_1.wkey,ref_1.c_tu2dv order by ref_1.wkey,ref_1.c_ijrc5 desc)) then ROUND(
    92.64,
    19) else 77.85 end
  , (61 * (39 * case when (90 in (
          select  
                ref_4.wkey as c0
              from 
                t_2nqc_c as ref_4
              where 31 between ref_4.c_fq8z_ and ref_4.pkey
            union all
            select  
                ref_6.c_qdo5gb as c0
              from 
                (t_khn17c as ref_5
                  inner join t_khn17c as ref_6
                  on (ref_5.wkey = ref_6.wkey ))
              where 78 = ref_5.pkey)) 
        or (86 between 6 and 63) then 53 else 73 end
      )), PI(), 'miwyqc', 91.29, case when 99 > 75 then case when 41 > case when 8 not in (
          select  
              ref_7.pkey as c0
            from 
              t_khn17c as ref_7
            where (1 = 1) 
                or (ref_7.pkey >= ref_7.wkey) and ref_7.wkey is NULL) then 48 else 20 end
         then 68.75 else 54.60 end
     else PI() end
  ), 
(263, 469000, PI(), case when exists (
    select  
        ref_8.pkey as c0, 
        ref_8.wkey as c1, 
        ref_8.c_ci0ked as c2, 
        ref_8.c_ci0ked as c3
      from 
        t_khn17c as ref_8
      where ref_8.pkey between ref_8.wkey and ref_8.wkey
      order by c0, c1, c2, c3 asc) then 4 else nullif((14 | 46),
    case when 100 in (
        select  
            ref_9.pkey as c0
          from 
            t_khn17c as ref_9
          where ref_9.c_ci0ked is not NULL) then 97 else 15 end
      ) end
  , 38.97, 'hejf_c', nullif(PI(),
  71.11), PI()), 
(263, 470000, PI(), (95 % 87), 6.79, 'd3ndq', PI(), 39.76), 
(263, 471000, nullif(PI(),
  6.86), SIGN(
  22), SIN(
  case when 12 in (
      select  
            40 as c0
          from 
            t_khn17c as ref_10
          where ref_10.pkey = ref_10.pkey
        union
        select  
            ref_11.c_qdo5gb as c0
          from 
            t_khn17c as ref_11
          where ref_11.pkey <> 83
          window w_wrjvvb as ( partition by ref_11.c_qdo5gb order by ref_11.wkey desc)) then TRUNCATE(
      60.49,
      case when 37 = 25 or 57 > 79 then 21 else 28 end
        ) else 10.16 end
    ), '6sybo', LOG(
  ROUND(
    9.16,
    90)), TAN(
  case when (70 <= case when 56 in (
              select  
                  ref_12.c_qdo5gb as c0
                from 
                  t_khn17c as ref_12
                where 0 <> 0) then 78 else 91 end
             and 'ulml_d' not like 'tx_scd') 
      or (99 <= 26) then COS(
      69.40) else 49.18 end
    )), 
(263, 472000, PI(), 79, case when 38 in (
    select  
        ref_13.pkey as c0
      from 
        t_2nqc_c as ref_13
      where ref_13.c_rpekod is not NULL) then case when exists (
      select  
          subq_0.c0 as c0, 
          subq_0.c0 as c1, 
          subq_0.c0 as c2, 
          subq_0.c0 as c3, 
          subq_0.c0 as c4, 
          subq_0.c0 as c5, 
          subq_0.c0 as c6, 
          subq_0.c0 as c7, 
          subq_0.c0 as c8, 
          subq_0.c0 as c9
        from 
          (select  
                ref_14.c_ci0ked as c0
              from 
                t_khn17c as ref_14
              where ref_14.wkey = ref_14.c_qdo5gb) as subq_0
        where (3 >> 60) <> 98) then 10.62 else 48.81 end
     else coalesce(17.61,
    71.3) end
  , ELT(
  38,
  '8c6evb',
  ('z1jxpc' || (null || 'fm_g7b')),
  '8_wmc'), 71.33, 16.5), 
(263, 473000, 62.44, (50 + 50), null, 'kqyhl', null, 20.59);
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
SELECT 1 WHERE 0 <> 0;
conn_0> 
COMMIT;
"""


def get_scenarios(isolation_level: IsolationLevel):
    return (
        [
            f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        {op}
        """
        ]
        * 100
    )
