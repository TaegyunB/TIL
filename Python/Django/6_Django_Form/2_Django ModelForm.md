## Django ModelForm
### Form
- 사용자 입력 데이터를 DB에 저장하지 않을 때(ex. 검색, 로그인)

### ModelForm
- 사용자 입력 데이터를 DB에 저장해야 할 때(ex. 게시글 작성, 회원가입)

## Meta class
- ModelForm의 정보를 작성하는 곳

### 'fields' 및 'exclude' 속성
- exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
<img src="images/image_1.png" width="600" height="400">

### Meta class 주의사항
- Django에서 ModelForm에 대한 추가 정보나 속성을 작성하는 클래스 구조를 Meta 클래스로 작성 했을 뿐이며, 파이썬의 inner class와 같은 문법적인 관점으로 접근하지 말 것

## ModelFrom 적용
### ModelForm을 적용한 create 로직
<img src="images/image_2.png" width="600" height="400">

## save 메서드
- 데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드

### save() 메서드가 생성과 수정을 구분하는 법
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정
<img src="images/image_3.png" width="600" height="400">

### Django Form 정리
- "사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구"
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움


