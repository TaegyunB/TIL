## DELETE
### DELETE statement
- 테이블 레코드 삭제

### DELETE syntax
~~~SQL
DELETE FROM table_name
[WHERE
    condition];
~~~
- DELETE FROM 절 다음에 테이블 이름 작성
- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드를 삭제

#### DELETE 활용 1
- articles 테이블의 1번 레코드 삭제
~~~SQL
DELETE FROM articles
WHERE id = 1;
~~~

#### DELETE 활용 2
- articles 테이블에서 작성일이 오래된 순으로 레코드 2개 삭제
~~~SQL
DELETE FROM articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAT
    LIMIT 2
);
~~~