# >wecode 27th 2팀 'Dr.Tart' BE
 
## 개발기간 
2021/11/29~2021/12/09


## 팀원
 
**_FE_** : [길도연](https://github.com/sanha-kil) [홍유진](https://github.com/howyoujini) [김상훈](https://github.com/Ho0on)




**_BE_** : [성주호](https://github.com/Joshua-sung) 박정현 [유민혁](https://github.com/MinHyeouk)




 
## 서비스 소개
 
> - 일상에 지친 당신을 위한 디저트 솔루션 ! 닥터타르트는 당신에게 딱 맞는 디저트를 처방해드립니다.
> - 글로벌 코스메틱 기업의 포털 사이트 [닥터자르트](www.drjart.co.kr/)를 클로닝한 프로젝트 Dr.Tart 입니다!
> - 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.
> - 개발은 초기 세팅부터 전부 직접 구현했습니다.
 



### Demo
[![Dr.Tart](http://img.youtube.com/vi/ofcgg-3-B28/0.jpg)](https://youtu.be/ofcgg-3-B28)




## 기술 스택
 
Front-End : JavaScript, React.js, sass, React-router-dom 


 
Back-End : Python, Django, MySQL, Miniconda 


 
## 협업 툴
Common : Git, Github, Slack, Trello, Notion





## 구현 기능 




#### User



* 이메일 유효성 검사 및 비밀번호 조건부여 회원가입



* bcrypt 비밀번호 암호화



* 로그인시 JWT 토큰 발행 및 토큰 검사



* 회원가입시 계정 중복 확인 
 
 
 
#### Product



* 제품 목록 조회



* 제품 상세 정보



* 제품 필터링 (top5,찜하기 많은 순)



* 제품 찜하기 


 
#### Order



* 장바구니 추가,삭제 기능



* 결제 진행 페이지 구현(제품 상세페이지에서 즉시 구매, 장바구니 아이템 구매)



* 주문 생성 후 주문 내역 페이지 구현



* 주문 취소 후 주문 상태 업데이트 구현




### 본인 담당 파트
> - 제품 목록 조회
> - 제품 상세 정보
> - 제품 필터링 (top5,찜하기 많은 순)
> - 결제 진행 페이지 구현(제품 상세페이지에서 즉시 구매, 장바구니 아이템 구매)
> - 주문 생성 후 주문 내역 페이지 구현
> - 주문 취소 후 주문 상태 업데이트 구현




## Project Structure
```bash
.
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── validators.py
│   └── views.py
├── dr_tart
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── orders
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── products
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pull_request_template.md
├── requirements.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```



## ERD Modeling
![](https://haileysbucket.s3.ap-northeast-2.amazonaws.com/Screen+Shot+2022-03-15+at+1.55.21+PM.png)





### Resource


1. 홈페이지 - 배포 전
2. **[Frontend Github](https://github.com/wecode-bootcamp-korea/27-1st-DrTart-frontend)**
3. **[Backend Github](https://github.com/wecode-bootcamp-korea/27-1st-DrTart-backend)**
4. **[Trello](https://trello.com/b/dFkizfeW/%EB%8B%A5%ED%84%B0-%ED%83%80%EB%A5%B4%ED%8A%B8)**
5. **[Notion](https://flint-vulture-659.notion.site/Dr-Tart-3b4e438bb0804ee3bfba830b111c2942)**
6. **[백엔드 API 명세서](https://docs.google.com/spreadsheets/d/1n2_Wbt1LcQuaXMw_rSI5OrGETkpUJidcoyRMXQbgb3w/edit#gid=0)**


- - -






 
_Reference 이 프로젝트는 닥터자르트 사이트를 참조하여 학습목적으로 만들었습니다. 
실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다. 
이 프로젝트에서 사용하고 있는 사진 대부분은 직접 촬영한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다._




