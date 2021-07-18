# kuro-rest-api

## Getting Started :
to get started with the project :
1. clone the repository http: ```https://github.com/Team-Tech2021/kuro-rest-api.git``` or ssl :``` git@github.com:Team-Tech2021/kuro-rest-api.git ```

2. redirect to the folder ``` cd kuro-rest-api ```
3. install the dependincies ```poetry install ```
4. create .env file and fill it with your config vars "follow .env.sample"
5. make migrations ```python manage.py makemigrations```
6. migrate to the database ```python manage.py migrate```
7. create superuser ```python manage.py createsuperuser```
8. run the server  ```python manage.py runserver```

## routes:

## main"user"
| Method      | End Point   | Action |   request body         |
| ----------- | ----------- | ----------- | ----------- |
| POST      |  /signup/      | signup      |  required: true ,  content: application/json ,  responses:'201',description: Created ,   requestBodies:  A JSON object containing user information, required felids:  "username:string , email:string , password:string , " optional felids: "first_name:string, is_superuser :boolean , is_staff : boolean ,is_active : boolean , created_at : Date "    |


## API

| Method      | End Point   | Action |            |
| ----------- | ----------- | ----------- | -----------
| POST   | /api/token/       | receives token /"login"  |     |
| GET   | /api/v1/code     |  get list of the codes  |     |
| GET   | /api/v1/code/{code_id}     |  get information about specific code   |     |
| GET   | /api/v1/problem     |  get list of the problems  |     |
| GET   | /api/v1/problem/{problem_id}     |  get information about specific problem   |     |
| GET   | /api/v1/problem     |  get list of the problems  |     |
| GET   | /api/v1/problem/{problem_id}     |  get information about specific problem   |     |





## Problems

| Method      | End Point   | Action |   request body      | headers |
| ----------- | ----------- | ----------- | -----------| -----------|
| GET   | /problems/is-complete/?problem_id     | check if the user completed successfully a problem |     |
| POST   | /problems/check-code/    | get the test result to check if the user completed successfully a problem |  required: true ,  content: application/json ,  responses:'200',description: OK ,   requestBodies:  A JSON object containing encoded code, required felids:  "code:string "    | Authorization: Bearer Token
| POST   | /problems/user-code/    | get the previous code for a specific and a problem |  required: true ,  content: application/json ,  responses:'200',description: OK ,   requestBodies:  A JSON object containing problem id, required felids:  "problem: integer"    | Authorization: Bearer Token
| POST   | /problems/compile/    | get the test result to check if the user completed successfully a problem and save it in passed table |  required: true ,  content: application/json ,  responses:'200',description: OK ,   requestBodies:  A JSON object containing encoded code, required felids:  "code:string "    | Authorization: Bearer Token
