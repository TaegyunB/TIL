## GROUP BY
### GROUP BY clause
- 레코드를 그룹화하여 요약본 생성('집계 함수'와 함께 사용)

### Aggregation Functions(집계 함수)
- 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
- SUM, AVG, MAX, MIN, COUNT

### GROUP BY syntax
~~~SQL
SELECT c1, c2, ..., cn, aggregate_function(ci)
FROM table_name
GROUP BY c1, c2, ..., cn;
~~~
- FROM 및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성 =

#### GROUP BY 예시 1
- Country 필드를 그룹화
~~~SQL
SELECT Country
FROM customers
GROUP BY Country;
~~~

#### GROUP BY 예시 2
-0 C0OUNT 함수가 각 그룹에 대한 집계된 값을 계산
~~~SQL
SELECT Country, COUNT(*),
FROM customers
GROUP BY Country;
~~~

#### GROUP BY 활용 1
- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
~~~SQL
SELECT Composer, AVG(Bytes) AS avgOfBytes
FROM tracks
GROUP BY Composer
ORDER BY avgOfBytes DESC;
~~~

#### GROUP BY 활용 2
- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10미만인 데이터 조회(단, Milliseconds 필드는 60,000으로 나눠 분 단위 값의 평균으로 계산)
~~~SQL
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
GROUP BY Composer
HAVING avgOfMinute < 10;
~~~

- Having clause
    - 집계 항목에 대한 세부 조건을 지정
    - 주로 GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE 처럼 동작

### SELECT statement 실행 순서
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
테이블에서(FROM) 특정 조건에 맞추어(WHERE) 그룹화하고(GROUP BY) 만약 그룹 중에서 조건이 있다면 맞추고(HAVING) 조회하여(SELECT) 정렬하고(ORDER BY) 특정 위치의 값을 가져옴(LIMIT)

    
