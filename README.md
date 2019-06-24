# wanted-test
This is a repository for wanted's coding assessment

소스코드를 다운받으시려면 아래의 주소의 소스코드를 받으시면 됩니다.

GITHUB URL: https://github.com/tejun007/wanted-test


## 실행방법

Docker로 구현하였으며, 실행을 위해서 아래의 실행 명령어로 이미지 생성 & container build를 할 수 있습니다.

```bash
$ cd <project_folder>
$ docker-compose up 
```

아래의 명령어로 container 를 종료 시킬 수 있습니다
```bash
$ cd <project_folder>
$ docker-compose down 
```

Docker container를 실행 한 후,
Flask-Migrate(alembic기반) 패캐지를 사용하여 database를 관리하도록 했기 때문에,
아래의 명령어로 models의 데이터 셋으로 database에 업데이트 할 수 있습니다.

```bash
# docker container의 터미널로 접속합니다
$ docker exec -it wanted-test-server bash

# migration version을 생성 후 db에 model의 변화를 적용할 경우 
# (가장 최신 소스코드는 이 부분 부터 사용하면됩니다.) 
/server# python database/manage.py db upgrade 
```

만약 migration version 정보가 없거나 새로 model의 소스코드가 변경되었을 경우
```bash
# docker container의 터미널로 접속합니다
$ docker exec -it wanted-test-server bash

# 만약 migrations 가 없어서 init해야할 경우
/server# python database/manage.py db init

# 첫 init 이후 alembic에 현재의 models/models.py 기반으로 migration version을 생성해야 할 경우
/server# python database/manage.py db migrate
```

database에 default test dataset 삽입하기
```bash
# docker container의 터미널로 접속합니다
$ docker exec -it wanted-test-server bash

# dataset initializer 실행
/server# ./database/init_database.sh 

```

## API 
Docker container를 실행 한 후, 아래의 주소로 가시면 API 명세 페이지를 볼 수 있습니다.
Flask-restplus에서 swagger와 연동하여 docs페이지를 만들 수 있는 decorator 및 소스코드를 추가하여 만들었습니다.
- url: http://0.0.0.0:5000/apis/v1
- Reference: https://flask-restplus.readthedocs.io/en/stable/swagger.html

API 명세 추가
(만약 http://0.0.0.0:5000/apis/v1 으로 swagger명세 보기가 불편하시다면 아래의 명세를 참조해주세요)
- GET /apis/v1/company/search : 회사명 혹은 태그로 회사를 검색할 수 있습니다.
    - Parameters: 
        - search_word string(query)	회사명 ex) 원티드랩
        - tags string (query) 태그 ex) tag1|tag2|tag3

    - Responses
        - 200	Success Example Value \
        Model
            ```json
                {
                  "success": true,
                  "reason": "string",
                  "companies": [
                    {
                      "id": 0,
                      "name_ko": "string",
                      "name_en": "string",
                      "name_ja": "string",
                      "tag_ko": "string",
                      "tag_en": "string",
                      "tag_ja": "string"
                    }
                  ]
                }
            ```
        - 400 Validation Error
        - 500 Server Error

- PUT /apis/v1/company/\<int:company_id\>/tags : 회사 태그정보 추가.
    - Parameters: 
        - company_id : 회사 고유 식별 번호
    - data(form):
        - tag_ko string(query)	한글 태그 ex) 원티드랩
        - tag_en string (query) 영문 태그 ex) tag1|tag2|tag3
        - tag_ja string (query) 일본어 태그 ex) タグ_4|タグ_20|タグ_16
    - Responses
        - 200	Success Example Value \
        Model
            ```json
                {
                  "success": true,
                  "reason": "string"
                }
            ```
        - 204 No Content 
        - 400 Validation Error
        - 500 Server Error

- DELETE /apis/v1/company/\<int:company_id\>/tags : 회사 태그정보 삭제.
    - Parameters: 
        - company_id : 회사 고유 식별 번호
    - data(form):
        - tag_ko string(query)	한글 태그 ex) 원티드랩
        - tag_en string (query) 영문 태그 ex) tag1|tag2|tag3
        - tag_ja string (query) 일본어 태그 ex) タグ_4|タグ_20|タグ_16
    - Responses
        - 200	Success Example Value \
        Model
            ```json
                {
                  "success": true,
                  "reason": "string"
                }
            ```
        - 204 No Content 
        - 400 Validation Error
        - 500 Server Error

## Pytest
아래의 명령어로 만들어진 API들에 대해 pytest를 진행 할 수 있습니다.

Local PC의 프로젝트 폴더에서는 아래와 같이 실행할 수 있습니다.
```bash
$ cd <project_folder>/server
$ py.test 
```
wanted-test-server container 내부에서는 아래와 같이 실행할 수 있습니다.
```bash
$ docker exec -it wanted-test-server bash
/server# py.test 
```
