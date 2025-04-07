## SELECT
### SELECT statement
- 테이블에서 데이터를 조회

### SELECT syntax
~~~SQL
SELECT
    select_list
FROM
    table_name;
~~~
- SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정

#### SELECT 활용 1
- 테이블 employees에서 LastName 필드의 모든 데이터를 조회
~~~SQL
SELECT LASTNAME
FROM employees;
~~~

#### SELECT 활용 2
- 테이블 employees에서 LastName, FirstName 필드의 모든 데이터를 조회
~~~SQL
SELECT LastName, FirstName
FROM employees;
~~~

#### SELECT 활용 3
- 테이블 employees에서 모든 필드 데이터를 조회
~~~SQL
SELECT *
FROM employees;
~~~

#### SELECT 활용 4
- 테이블 employees에서 FirstName 필드의 모든 데이터를 조회
- (단, 조회 시 FirstName이 아닌 '이름'으로 출력될 수 있도록 변경)
~~~SQL
SELECT FirstName AS '이름'
FROM employees;
~~~

#### SELECT 활용 5
- 테이블 tracks에서 Name, Milliseconds 필드의 모든 데이터 조회
- (단, Milliseconds 필드는 60000으로 나눠 분 단위 값으로 출력)
~~~SQL
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM tracks;
~~~

### SELECT 정리
- 테이블의 데이터를 조회 및 반환
- '*'를 사용하여 모든 필드 선택