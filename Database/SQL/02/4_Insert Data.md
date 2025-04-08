## INSERT
### INSERT statement
- 테이블 레코드 삽입

### INSERT syntax
~~~SQL
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
~~~
- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성

#### INSERT 활용 1
- articles 테이블에 다음과 같은 데이터 입력
<img src="images/image_5.png" width="600" height="400">

~~~SQL
INSERT INTO articles(title, content, createdAt)
VALUES('hello', 'world', '2000-01-01');
~~~

#### INSERT 활용 2
- articles 테이블에 다음과 같은 데이터 추가 입력
<img src="images/image_6.png" width="600" height="400">

~~~SQL
INSERT INTO articles(title, content, createdAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');
~~~

#### INSERT 활용 3
- DATE함수를 사용해 articles 테이블에 다음과 같은 데이터 추가 입력
~~~SQL
INSERT INTO articles(title, content, createdAt)
VALUES('mytitle', 'mycontent', DATE());
~~~

