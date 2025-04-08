## Update
### UPDATE statement
- 테이블 레코드 수정

### UPDATE syntax
~~~SQL
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];
~~~
- SET 절 다음에 수정 할 필드와 새 값을 지정
- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드를 수정

#### UPDATE 활용 1
- articles 테이블 1번 레코드의 title 필드 값을 'update Title'로 변경
~~~SQL
UPDATE articles
SET title = 'update Title'
WHERE id = 1;
~~~

#### UPDATE 활용 2
- articles 테이블 2번 레코드의 title, content 필드 값을 각각 'update Title', 'update Content'로 변경
~~~SQL
UPDATE articles
SET title='update Title', content='update Content'
WHERE id = 2;
~~~
