# kuro-rest-api

## Getting Started :
to get started with the project :
1. clone the repository http: ```https://github.com/Team-Tech2021/kuro-rest-api.git``` or ssl :``` git@github.com:Team-Tech2021/kuro-rest-api.git ```

2. redirect to the folder ``` cd kuro-rest-api ```
3. install the dependincies ```poetry install ```
4. create .env file and fill it with your config vars "follow .env.sample"
5. make migrations ```python manage.py makemigrations```
6. migrate to the database ```python manage.py migrate```
7. create superuser ```python manage.py superuser```
8. run the server  ```python manage.py runserver```

## routes:
1. signup:

    method:POST

    ```http://127.0.0.1:8000/signup/```

2. receives token "login"

    method:POST

    ```http://127.0.0.1:8000/api/token/```

3. get list of the codes:

    method:GET

    ```http://127.0.0.1:8000/api/v1/code/```

4. get list of the problems:

    method:GET

    ```http://127.0.0.1:8000/api/v1/problem/```

5. check if the user completed successfully a problem

    method:GET

    `http://127.0.0.1:8000/problems/is-complete/?problem=<int:pk>`

6. receive a previous code for a certain user:

    method:POST

    ```http://127.0.0.1:8000/problems/user-code/```

7. check if the user code is correct

    method:POST

    ```http://127.0.0.1:8000/problems/user-code/```

8. check if the user passed and added the problem to the passed table

    method:POST

    ```http://127.0.0.1:8000/problems/compile/```
