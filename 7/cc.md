### Concurrency Control 실습

```sql
-- 초기 설정
TRUNCATE TABLE account;
INSERT INTO account (id, balance) VALUES (1, 100);
COMMIT;

------------------------------------
-- Now, under "SERIALIZABLE" mode --
------------------------------------

-- 트랜잭션 T2 (세션 1에서 실행)
\c your_database your_username
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM account;
-- 결과:
-- id | balance
-- ----+---------
--  1 | 100

-- 트랜잭션 T1 (세션 2에서 실행)
\c your_database your_username
BEGIN;
UPDATE account SET balance = balance + 10 WHERE id = 1;
COMMIT;

-- 트랜잭션 T2 (세션 1에서 실행)
SELECT * FROM account WHERE id = 1;
-- 결과:
-- id | balance
-- ----+---------
--  1 | 100
-- "non-repeatable read" 없음

-- 트랜잭션 T3 (세션 3에서 실행)
\c your_database your_username
BEGIN;
INSERT INTO account (id, balance) VALUES (2, 200);
COMMIT;

-- 트랜잭션 T2 (세션 1에서 실행)
SELECT * FROM account;
SELECT * FROM account WHERE id = 1;
SELECT SUM(balance) FROM account;
-- 결과:
-- id | balance
-- ----+---------
--  1 | 100
-- 합계(sum): 100
-- "phantom phenomenon" 없음

ROLLBACK;

------------------------------------
-- Now, under "READ COMMITTED" mode --
------------------------------------

-- 트랜잭션 T2 (세션 1에서 실행)
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
DO $$
DECLARE
    bal NUMERIC;
BEGIN
    SELECT balance INTO bal FROM account WHERE id = 1;

    -- 트랜잭션 T1 (세션 2에서 실행)
    -- 다른 세션에서 다음 명령을 실행
    PERFORM pg_sleep(1);
    UPDATE account SET balance = balance + 10 WHERE id = 1;

    -- 트랜잭션 T2 (세션 1에서 실행)
    UPDATE account SET balance = bal * 1.1 WHERE id = 1;
END $$;
COMMIT;

-- 트랜잭션 T2 (세션 1에서 실행)
SELECT * FROM account WHERE id = 1;
-- 결과:
-- id | balance
-- ----+---------
--  1 | 110
-- "scholar lost update" 문제 발생

ROLLBACK;

```

### 추가 설명

- **Dirty Read**: 트랜잭션이 다른 트랜잭션에 의해 변경된 데이터를 해당 트랜잭션이 커밋되기 전에 읽는 것을 의미
- **Non-repeatable read**: 같은 트랜잭션 내에서 같은 쿼리를 두 번 실행할 때 다른 결과를 반환하는 경우
- **Phantom Read**: 트랜잭션 내에서 특정 조건에 맞는 행을 두 번 조회할 때, 다른 트랜잭션이 새로운 행을 삽입하거나 삭제하여 결과 행 집합이 달라지는 경우
