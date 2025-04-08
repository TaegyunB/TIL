## ALTER TABLE
### ALTER TABLE statement
- 테이블 및 필드 조작

### ALTER TABLE 역할
- ALTER TABLE ADD COLUMN
  - 필드 추가

- ALTER TABLE RENAME COLUMN
  - 필드 이름 변경

- ALTER TABLE DROP COLUMN
  - 필드 삭제

- ALTER TABLE RENAME TO
  - 테이블 이름 변경

### ALTER TABLE ADD COLUMN syntax
~~~SQL
ALTER TABLE
    table_name
ADD COLUMN
    column_definition;
~~~
- ADD COLUMN 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
- 단, 추가하고자 하는 필드에 NOT NULL 제약조건이 있을 경우 NULL이 아닌 기본 값 설정 필요

#### ALTER TABLE ADD COLUMN 활용 1
- examples 테이블에 다음 조건에 맞는 Country 필드 추가
~~~SQL
ALTER TABLE examples
ADD COLUMN Country VARCHAR(100) NOT NULL DEFAULT 'default value';
~~~
- 테이블 생성시 정의한 필드는 기본 값이 없어도 NOT NULL 제약조건으로 생성되며 내부적으로 Default Value는 NULL로 설정됨

#### ALTER TABLE ADD COLUMN 활용 2
- examples 테이블에 다음 조건에 맞는 Age, Address 필드 추가
~~~SQL
ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL DEFAULT 'default value';
~~~

### ALTER TABLE RENAME COLUMN syntax
~~~SQL
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name
~~~
- RENAME COLUMN 키워드 뒤에 이름을 바꾸려는 필드의 이름을 지정하고 TO 키워드 뒤에 새 이름을 지정

#### ALTER TABLE RENAME COLUMN 활용 1
- examples 테이블 Address 필드의 이름을 PostCode로 변경
~~~SQL
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;
~~~

### ALTER TABLE DROP COLUMN syntax
~~~SQL
ALTER TABLE table_name
DROP COLUMN column_name
~~~
- DROP COLUMN 키워드 뒤에 삭제 할 필드 이름 지정

#### ALTER TABLE DROP COLUMN 활용
- examples 테이블의 PostCode 필드를 삭제
~~~SQL
ALTER TABLE examples
DROP COLUMN PostCode;
~~~

### ALTER TABLE RENAME TO syntax
~~~SQL
ALTER TABLE table_name
RENAME TO new_table_name
~~~
- RENAME TO 키워드 뒤에 새로운 테이블 이름 지정

#### ALTER TABLE RENAME TO 활용
- examples 테이블 이름을 new_examples로 변경
~~~SQL
ALTER TABLE examples
RENAME TO new_examples;
~~~


