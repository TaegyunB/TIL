## Git 기본 명령어

- 저장소 초기화
    - git init

- 저장소 클론
    - git clone <원격 저장소 URL>

- 파일 스테이징
    - git add <파일명> // 특정 파일 추가
    - git add . // 모든 파일 추가

- 커밋
    - git commit -m "커밋 메시지"

- 원격 저장소 추가
    - git remote add origin <원격 저장소 URL>

- 변경 사항 푸시
    - git push origin <브랜치 이름>

- 변경 사항 가져오기
    - git pull origin <브랜치 이름>

- 브랜치 생성 및 전환
    - git branch <브랜치 이름> // 브랜치 생성
    - git checkout <브랜치 이름> // 브랜치 전환
    - git switch <브랜치 이름> // 최신 방식의 브랜치 전환

- 브랜치 병합
    - git merge <브랜치 이름>
