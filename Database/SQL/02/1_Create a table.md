## CREATE TABLE statement
- 테이블 생성

### CREATE TABLE syntax
~~~SQL
CREATE TABLE table_name (
    column_1 data_type constraints,
    column_2 data_type constraints,
    ...,
);
~~~
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성

### CREATE TABLE 활용
- examples 테이블 생성 및 확인
~~~SQL
CREATE TABLE examples (
ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
LastName VARCHAR(50) NOT NULL,
FirstName VARCHAR(50) NOT NULL
);
~~~

### PRAGMA
- 테이블 schema(구조) 확인
~~~SQL
PRAGMA table_info('examples');
~~~
<img src="images/image_1.png" width="600" height="400">
- "cid"
  - Column ID를 의미하며 각 컬럼의 고유한 식별자를 나타내는 정수 값
  - 직접 사용하지 않으며 PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용됨
  
### 데이터 타입
<img src="images/image_2.png" width="600" height="400">

### 제약 조건
<img src="images/image_3.png" width="600" height="400">

### AUTOINCREMENT 키워드
<img src="images/image_4.png" width="600" height="400">

### SQLite 데이터 타입
- NULL
  - 아무런 값도 포함되지 않음을 나타냄

- INTEGER
  - 정수

- REAL
  - 부동 소수점

- TEXT
  - 문자열

- BLOB
  - 이미지, 동영상, 문서 등의 바이너리 데이터

### Constraints (제약 조건)
- 테이블의 필드에 적용되는 규칙 또는 제한 사항
- <strong>데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장</strong>

### 대표 제약 조건 3가지
- PRIMARY KEY
  - 해당 필드를 기본 키로 지정
  - INTEGER 타입에만 적용되며, INT, BIGINT 등과 같은 다른 정수 유형은 적용되지 않음

- NOT NULL
  - 해당 필드에 NULL 값을 허용하지 않도록 지정

- FOREIGN KEY
  - 다른 테이블과의 외래 키 관계를 정의

### AUTOINCREMENT keyword
- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성

#### AUTOINCREMENT 특징
- 필드의 자동 증가를 나타내는 특수한 키워드
- 주로 primary key 필드에 적용
- INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
- 삭제된 값은 무시되며 재사용할 수 없게 됨

