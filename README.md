# recipe-api-server

# 서버가동
    # python app.py

# 작은 단위로 테스트 하는것
    # 단위 테스트 라고 한다

# API 함수 만들고
포스트맨으로 실행해서 테스트하고
DB에 정확히 반영되었는지 MySQL Workbench로 확인하면서, 개발했습니다
=> 단위테스트 (unit test)
=> 꼼꼼하게 테스트를 해서 버그양성을 안하려고 노력합시다

# 포스트맨으로
API 명세서를 주소로 나타내고
이력서에 나타냄

# 이메일은
중복되면안되기에 데이터베이스에서 중복처리 했습니다

# 유저 처리
### 유저id를 참조하려면?
MySQL에서 foreign keys로 참조

### 회원가입
이메일, 비밀번호 => 암호화 => DB에 저장

### 비밀번호 처리 라이브러리
pip install psycopg2-binary passlib

# 디버깅방법
첫줄빼고 다 주석처리후
마지막 return 처리만 하고 포스트맨에서 성공코드 200뜨나 확인하고
한줄씩 다시 쓰면서 어디서 에러가 나는지 확인한다
\
서버의 오류는 어디서 오류가 났는지 찾기가 힘들다..

# 암호화가 중요하다
user_id의 암호화