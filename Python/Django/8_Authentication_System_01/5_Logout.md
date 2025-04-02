## Logout
- 로그아웃은 Session을 Delete하는 과정

### logout(request)
1. DB에서 현재 요청에 대한 Session Data를 삭제
2. 클라이언트의 쿠키에서도 Session Id를 삭제

### 로그아웃 로직 작성
<img src="images/image_15.png" width="600" height="400">
<img src="images/image_16.png" width="600" height="400">