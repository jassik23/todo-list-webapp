# todo-list-webapp

## Развёртка Docker образа

1. Установить Docker с официального сайта
2. С помощью cmd в директории репозитория вызвать команду ```docker compose up --build```
3. Web приложение будет доступно по адресу localhost:8000

## Запросы к Web приложению:

1. *POST запрос* - создание пользователя

![image](/docs/images/post_user.png)

2. *POST запрос* - создание задачи для пользователя

![image](/docs/images/post_task.png)

3. *GET запрос* - выборка всех пользователей

![image](/docs/images/get_users.png)

4. *GET запрос* - выборка всех задач определенного пользователя

![image](/docs/images/get_tasks.png)

5. *UPDATE запрос* - обновление полей пользователя

![image](/docs/images/put_user.png)

6. *UPDATE запрос* - обновление полей задачи

![image](/docs/images/put_task.png)

7. *DELETE запрос* - удаление пользователя

![image](/docs/images/delete_user.png)

8. *DELETE запрос* - удаление задачи

![image](/docs/images/delete_task.png)
