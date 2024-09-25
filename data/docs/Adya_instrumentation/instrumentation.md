# Adya Graphs

## Introduction

In his thesis, Adya introduced Direct Serialisability Graphs (DSGs) as a tool to reason about the serialisability of transactions. A DSG is a directed graph where each node represents a transaction and each edge represents a conflict between two transactions.

Isolation levels can be expressed as constraints on the structure of DSGs. For example, a transaction is serialisable if and only if its corresponding node in the DSG has no cycles.

## Previous Work

There are 2 main papers we refer to in this section:
 * _Validating Database System Isolation Level Implementations with Version Certificate Recovery_
    The authors use a white-box approach for extracting versioning information from DBMSs, and use this information to construct DSGs. We are interested in obtaining the same DSG, except we want to do it in a black-box way.
 
 * _Detecting Transactional Bugs in Database Engines via Graph-Based Oracle Construction_ (OSDI 2023)
    The authors use a black-box approach, by instrumenting SQL instructions to extract statement dependencies. This is very promissing for us, except that sporadic depenencies might be captured by this approach, which makes the cycle-detection impossible.

## Instrumentation in OSDI 2023

The OSDI paper proposes to add a _Before Write Read_, _After Write Read_ and _Version Set Read_ dependencies.

The dependencies captured by the paper are the following:
 1. Direct stmt-item-read dependency - A statement reads an item that was written by another statement.
 2. Direct stmt-item-write dependency - A statement overwrites an item that was written by another statement.
 3. Direct stmt-item-anti dependency - A statement reads an item which is then overwritten by another statement.
 4. Direct stmt-predicate-read dependency - A predicated in a select statement considers an item that was written by another statement.
 5. Direct stmt-predicate-write dependency - A predicated in a write statement considers an item that was written by another statement.
 6. Direct stmt-predicate-anti dependency - A predicated in a select statement considers an item that was overwritten by another statement.
 7. Direct stmt-value-write dependency - A statement writes a value which depends on an item written by another statement.

The instrumentation methodology is the following:
 * Before and after any write statments, we add a _Before Write Read_ and _After Write Read_ dependency.
 * Before any read statement, we add a _Version Set Read_ dependency.


The dependencies can be found in the following way:
 1. Using the VSR, we can check the version of the items read by a statement. We verify that the version is the same as the version of the item written by the dependent statement.
 2. Using the BWR and AWR, we can check that the version of the item read by a statement is the same as the version written by the dependent statement.
 3. same as 2.
 4. Using the VSR, we can check that the version of the item read by a statement is the same as the version written by the dependent statement.
 5. Same as 4.
 6. Using the VSR, we cn check that the version of the item read by a statement is the same as the version written by the dependent statement.
 7. Using the VSR, we can check that the version read by a statement is the same as the version written by the dependent statement.

This approach is complete, but not sound. In particular, sporadic dependencies might be captured.
The paper addresses this issue by adding a graph decycling step. However, graph cycles are precisely what we are interseted in, so we cannot use this approach.


## Our Approach

We use SQL instrumentation for extracting the dependencies between transactions. We then use these dependencies to construct DSGs.

The main steps are:
 * Extracting the dependencies between transactions.
 * Constructing DSGs from these dependencies.
 * Detecting cycles in the DSGs.
    

Steps 2 and 3 are trivial, and the real difficulty lies in step 1. We need to extract the dependencies between transactions in a way that is both sound and complete.

### Dependencies

We follow the Adya model ad-literam. We need to be able to extract the following types of dependencies:

 1. Direct read-depends: Tj -> Ti
    * Item-read-depends - Ti installs an object version xi and Tj reads xi.
    * Predicate-read-depends - Tj performs rj(P: Vset(P)) and xi ∈ Vset(P).
 
 2. Direct write-depends: Tj -> Ti
    * Item-write-depends - Ti installs xi, and Tj installs the next version xj.
    * Predicate-write-depends -
        Tj performs wj(P: Vset(P)) and xi ∈ Vset(P)
        OR
        Tj overwrites wi(P: Vset(P))

3. Direct anti-depends: Tj -> Ti
    * Item-anti-depends - Ti reads xk, and Tj installs the next version xj.
    * Predicate-anti-depends - Tj overwrites a predicate that was read by Ti.

The definition of an overwrite is the following:
Tj overwrites Ti if:
 * Ti has an operation wi(P: Vset(P)) or ri(P: Vset(P)).
 * Tj installs xj.
 * xk is an older version than xj.
 * xk ∈ Vset(P).
 * xk matches the predicate P and xj does not, or the other way around.

### Instrumentation

We rely on an instrumentation similar to the one in the OSDI paper. We consider the following types of instrumentation:
 * Before Write Read (similar to the OSDI paper).
 * After Write Read (similar to the OSDI paper).
 * Version Set Read (similar to the OSDI paper).
 * Predicate Match Read (new).

The first three types of instrumentation are similar to the ones in the OSDI paper, so we won't go into details about them. The interesting part is the Predicate Match Read instrumentation, which is meant to capture overwrite dependencies.

The idea behind Predicate Match Read is to capture changes in predicate matches between transactions. The instrumentation is the following:
 * Before any write statement, run all predicates to see the items matched by the predicate.
 * After any write statement, run all predicates to see the items matched by the predicate.

The overwrites can be computed by comparing the items matched by the predicates before and after the write statement, combined by the version set read (to see if we are dealing with a newer or older version of the items).

## Example

### Instrumenting SQL Code

Initial testcase (taken from the OSDI paper):
```SQL
T0.S0> start transaction;
T0.S1> update t0 set vkey = 162;
T0.S2> select * from t1;

T1.S0> start transaction;
T1.S1> select * from t0;

T0.S3> commit;

T1.S2> select * from t1 where
        t1.c0 <= (select min(vkey) from t0);
T1.S3> update t1 set vkey = 63 where
        t1.c0 <= (select min(vkey) from t0);

T1.S4> commit;
```

We add the Item-Tracking instrumentation (similar to the OSDI paper):
```SQL
T0.S0>      start transaction;
T0.S1.BWR>  select * from t0;                       -- Before Write Read
T0.S1>      update t0 set vkey = 162;
T0.S1.AWR>  select * from t0 where vkey =162;       -- After Write Read

T0.S2>      select * from t1;

T1.S0>      start transaction;
T1.S1>      select * from t0;

T0.S3>      commit;

T1.S2>      select * from t1 where
              t1.c0 <= (select min(vkey) from t0);
T1.S3.BWR>  select * from t1 where                  -- Before Write Read  
              t1.c0 <= (select min(vkey) from t0);
T1.S3>      update t1 set vkey = 63 where
              t1.c0 <= (select min(vkey) from t0);
T1.S3.AWR>  select * from t1 where vkey = 63;       -- After Write Read

T1.S4>      commit;
```

We then add the Version-Set-Traffic instrumentation (similar to the OSDI paper):
```SQL
T0.S0>      start transaction;

T0.S1.VSR>  select * from t0;                       -- Version Set Read
T0.S1.BWR>  select * from t0;                       -- BWR
T0.S1>      update t0 set vkey = 162;
T0.S1.AWR>  select * from t0 where vkey =162;       -- AWR

T0.S2.VSR>  select * from t1;                       -- Version Set Read
T0.S2>      select * from t1;

T1.S0>      start transaction;

T1.S1.VSR>  select * from t0;                       -- Version Set Read
T1.S1>      select * from t0;

T0.S3>      commit;

T1.S2.VSR>  select * from t0;                       -- Version Set Read
T1.S2.VSR>  select * from t1;                       -- Version Set Read
T1.S2>      select * from t1 where
              t1.c0 <= (select min(vkey) from t0);

T1.S3.VSR>  select * from t0;                       -- Version Set Read
T1.S3.VSR>  select * from t1;                       -- Version Set Read
T1.S3.BWR>  select * from t1 where                  -- BWR 
              t1.c0 <= (select min(vkey) from t0);
T1.S3>      update t1 set vkey = 63 where
              t1.c0 <= (select min(vkey) from t0);
T1.S3.AWR>  select * from t1 where vkey = 63;       -- AWR

T1.S4>      commit;
```

We then add the Predicate-Match instrumentation:

The predicates are the following:
 * P1: `vkey = 162` over `t0`.
 * P2: `c0 <= (select min(vkey) from t0)` over `t1`.
 * P3: `vkey = 63` over `t1`.

For each update, we add a Before-Predicate-Match and an After-Predicate-Match.

```SQL
T0.S0>      start transaction;

T0.S1.BPM>  select * from t0 where vkey = 162;      -- Before Predicate Match P1
T0.S1.BPM>  select * from t1 where
                c0 <= (select min(vkey) from t0);   -- Before Predicate Match P2
T0.S1.BPM>  select * from t1 where vkey = 63;       -- Before Predicate Match P3
T0.S1.VSR>  select * from t1;                       -- VSR
T0.S1.BWR>  select * from t0;                       -- BWR
T0.S1>      update t0 set vkey = 162;
T0.S1.AWR>  select * from t0 where vkey =162;       -- AWR
T0.S1.APM>  select * from t0 where vkey = 162;      -- After Predicate Match P1
T0.S1.APM>  select * from t1 where
                c0 <= (select min(vkey) from t0);   -- After Predicate Match P2
T0.S1.APM>  select * from t1 where vkey = 63;       -- After Predicate Match P3

T0.S2.VSR>  select * from t1;                       -- VSR
T0.S2>      select * from t1;

T1.S0>      start transaction;

T1.S1.VSR>  select * from t0;                       -- VSR
T1.S1>      select * from t0;

T0.S3>      commit;

T1.S2.VSR>  select * from t0;                       -- VSR
T1.S2.VSR>  select * from t1;                       -- VSR
T1.S2>      select * from t1 where
              t1.c0 <= (select min(vkey) from t0);

T1.S3.BPM>  select * from t0 where vkey = 162;      -- Before Predicate Match P1
T1.S3.BPM>  select * from t1 where
                c0 <= (select min(vkey) from t0);   -- Before Predicate Match P2
T1.S3.BPM>  select * from t1 where vkey = 63;       -- Before Predicate Match P3
T1.S3.VSR>  select * from t0;                       -- VSR
T1.S3.VSR>  select * from t1;                       -- VSR
T1.S3.BWR>  select * from t1 where                  -- BWR 
              t1.c0 <= (select min(vkey) from t0);
T1.S3>      update t1 set vkey = 63 where
              t1.c0 <= (select min(vkey) from t0);
T1.S3.AWR>  select * from t1 where vkey = 63;       -- AWR
T1.S3.APM>  select * from t0 where vkey = 162;      -- After Predicate Match P1
T1.S3.APM>  select * from t1 where
                c0 <= (select min(vkey) from t0);   -- After Predicate Match P2
T1.S3.APM>  select * from t1 where vkey = 63;       -- After Predicate Match P3

T1.S4>      commit;
```

### Extracting Dependencies

Similarely to the OSDI implementation, we make sure each table contains at least:
 * A primary key, which uniquely identifies the object.
 * A version key, which tracks the versions of the object.

Recall the dependencies defined in Adya we mentioned above. We now explain how to extract each type of dependency.

 1. Direct read-depends: Tj -> Ti
    * Item-read-depends - Ti installs an object version xi and Tj reads xi.
    * Predicate-read-depends - Tj performs rj(P: Vset(P)) and xi ∈ Vset(P).
    For each object we read, we check which write installed this version. This yields a dependency.
 
 2. Direct write-depends: Tj -> Ti
    * Item-write-depends - Ti installs xi, and Tj installs the next version xj.
    * Predicate-write-depends -
        Tj performs wj(P: Vset(P)) and xi ∈ Vset(P)
        OR
        Tj overwrites wi(P: Vset(P))
    For each object we write, we check which write installed the overwriten version. This yields a dependency.
    We also check for overwritten write predicates. This yields a dependency.

3. Direct anti-depends: Tj -> Ti
    * Item-anti-depends - Ti reads xk, and Tj installs the next version xj.
    * Predicate-anti-depends - Tj overwrites a predicate that was read by Ti.
    For each object we read, we check which write installed the next version. This yields a dependency.
    We also check for overwritten write predicates. This yields a dependency.

### Extracting Overwrites

Extracting overwrites can be done by relying on Adya's definition of an overwrite. Bellow is the definition, with the steps needed to check each condition.

Tj overwrites Ti if:
 1. Ti has an operation wi(P: Vset(P)) or ri(P: Vset(P)).
    This is trivial to check.
 2. Tj installs xj.
    This can be done using the BWR and AWR instrumentation.
 3. xk is an older version than xj.
    From BWR and AWR instrumentations we know the full version chain of the objects. This makes it possible to check which version is older.
 4. xk ∈ Vset(P).
    This can be done using the VSR instrumentation.
 5. xk matches the predicate P and xj does not, or the other way around.
    This can be done using the Predicate Match instrumentation.

## Implementation Overview

The `TxCheck` tool already already implements features similar to what we need. It already supports the following:
 * Generating SQL queries.
 * BWR, AWR and VSR instrumentation of SQL code.
 * Extraction of some dependencies between transactions.

The additional features we need to implement are:
 1. Extracting predicates from `SELECT`, `UPDATE` and `DELETE` statements.
    * For each SQL query check if it contains or not a predicate.
    * Generate a list of predicates for each transaction, together with the tables they are applied on.
 2. Adding Predicate Match instrumentation.
    * For each `UPDATE` or `DELETE` statement, add a Before-Predicate-Match and an After-Predicate-Match for each predicate, need to somehow store the instrumentation, as this design is very different from the current one.
    * Process the output of the tool to extract the Before-Predicate-Match and After-Predicate-Match results.
    * From the given results, extract the modifications to the predicates.
 3. Computing transaction overwrites.
    * For each object, compute the linear version chain.
    * For every pair of transaction & predicate, check if the predicate is overwritten, by using Adya's definition.
 4. Extracting dependencies between transactions and check for bugs.
    * Using the results from the previous steps, extract the dependencies between transactions.
    * Build the DSG from the dependencies.
    * Check for cycles in the DSG.