# 로또 번호 추천 프로젝트 

코드스테이츠 section3 프로젝트 : CRUD를 적용한 Flask API 개발

### 주제 선정
CRUD를 적용하는 것이 프로젝트 통과 조건이었는데 단순 메모장 말고 재미있는 주제가 없을까 생각하다가 로또번호를 추천해주는 API를 제작하게 되었다.

### 프로젝트 진행

- 역대 당첨 번호의 빈도수를 기반으로 번호 추천 

- PostgreSQL을 사용

- 저장할 번호 입력시 자동으로 현재 날짜와 함께 입력, 저장된 목록 불러오기, 수정, 삭제 구현 

- heroku를 사용해 배포 [링크 바로가기](https://mylottoapp.herokuapp.com)

![db_schema](https://user-images.githubusercontent.com/83392231/176826677-7642729e-0289-451e-b03c-b05150204f5b.png)
*db schema*

### 프로젝트 구조

__init__.py : Flask 어플리케이션을 실행하기 위한 초기 app 을 제공

models : 데이터베이스 설정

routes : Flask에서 사용되는 라우트 

utils : 어플리케이션에서 사용할 기능 (번호 추천 알고리즘)  

templates : 각 페이지별 HTML 리소스

### 구현 페이지 

![스크린샷 2022-07-01 오후 2 14 54](https://user-images.githubusercontent.com/83392231/176828342-5692f7ab-bc57-4a86-bf9c-93390b697c87.png)


#### 프로젝트 회고
프로젝트 기한이 3일로 굉장히 짧아서 시간분배를 최우선으로 했으며 다행히 배포까지 무사히 마칠 수 있었다. 

DB연결부터 html에서 데이터를 받고 다시 데이터를 화면으로 뿌려주는 과정의 경험을 했다. 
