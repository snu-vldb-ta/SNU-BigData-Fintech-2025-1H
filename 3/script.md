### postgres scott script

```sql
create table dept(
  deptno   decimal(2,0) not null,
  dname    varchar(14),
  loc      varchar(13));
create table emp(
  empno    decimal(4,0) not null,
  ename    varchar(10),
  job      varchar(9),
  mgr      decimal(4,0),
  hiredate date,
  sal      decimal(7,2),
  comm     decimal(7,2),
  deptno   decimal(2,0) not null);


insert into DEPT values (10, 'ACCOUNTING', 'NEW YORK');
insert into DEPT values (20, 'RESEARCH', 'DALLAS');
insert into DEPT values (30, 'SALES', 'CHICAGO');
insert into DEPT values (40, 'OPERATIONS', 'BOSTON');

insert into emp values (7839, 'KING',   'PRESIDENT', cast(null as integer), to_date('17-11-1981','dd-mm-yyyy'), 5000, cast(null as integer), 10);
insert into emp  values (7698, 'BLAKE',  'MANAGER',   7839, to_date('1-5-1981','dd-mm-yyyy'),      2850, cast(null as integer), 30);
insert into emp  values (7782, 'CLARK',  'MANAGER',   7839, to_date('9-6-1981','dd-mm-yyyy'),      2450, cast(null as integer), 10);
insert into emp  values (7566, 'JONES',  'MANAGER',   7839, to_date('2-4-1981','dd-mm-yyyy'),      2975, cast(null as integer), 20);
insert into emp  values (7788, 'SCOTT',  'ANALYST',   7566, to_date('13-7-87','dd-mm-rr') - 85,  3000, cast(null as integer), 20);
insert into emp  values (7902, 'FORD',   'ANALYST',   7566, to_date('3-12-1981','dd-mm-yyyy'),     3000, cast(null as integer), 20);
insert into emp  values (7369, 'SMITH',  'CLERK',     7902, to_date('17-12-1980','dd-mm-yyyy'),     800, cast(null as integer), 20);
insert into emp  values (7499, 'ALLEN',  'SALESMAN',  7698, to_date('20-2-1981','dd-mm-yyyy'),     1600,  300, 30 );
insert into emp  values (7521, 'WARD',   'SALESMAN',  7698, to_date('22-2-1981','dd-mm-yyyy'),     1250,  500, 30 );
insert into emp  values (7654, 'MARTIN', 'SALESMAN',  7698, to_date('28-9-1981','dd-mm-yyyy'),     1250, 1400, 30 );
insert into emp  values (7844, 'TURNER', 'SALESMAN',  7698, to_date('8-9-1981','dd-mm-yyyy'),      1500,    0, 30 );
insert into emp  values (7876, 'ADAMS',  'CLERK',     7788, to_date('13-7-87', 'dd-mm-rr') - 51, 1100, cast(null as integer), 20 );
insert into emp  values (7900, 'JAMES',  'CLERK',     7698, to_date('3-12-1981','dd-mm-yyyy'),      950, cast(null as integer), 30 );
insert into emp  values (7934, 'MILLER', 'CLERK',     7782, to_date('23-1-1982','dd-mm-yyyy'),     1300, cast(null as integer), 10);
```