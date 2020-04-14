# Учебный проект SkillFactory

Flask
Cервис для планирования событий

Сервис развернут на Heroku
https://sf-e9.herokuapp.com/

## Развернуть свой сервис на локальной машине:  
Установить docker на машину.  
`docker run --rm  --name flask-db -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres:12-alpine`  
`docker exec -it flask-db psql -U postgres -c "create database sf_e9_flask_events"`  

Если хочется, разворачиваем virtualenv, далее -  
`git clone https://github.com/2100992/sf_e9.git`  
`cd sf_e9`  
`pip3 install -r requirements.txt`  
`python3 manage.py db migrate`  
`python3 manage.py db upgrade`  
`gunicorn -b localhost:5000 app:app`  

## Развернуть сервис на Heroku
Делаем fork проекта на github  
Создаем приложение на heroku  
Во вкладке 'Deploy' выбираем 'Deployment method' - 'GitHub' и выбираем соотвествующий репозиторий.  
Жмем 'Deploy Branch' - 'master'  
Во вкладке 'Settings' жмем кнопку 'Reveal Config Vars' и добавляем следующие переменные окружения:  
    - DATABASE_URL - Уже должна автоматом проставиться системой. Что-то типа `postgres://usersdfs:passdfasdf@hostsdaf.eu-west-1.compute.amazonaws.com:5432/databasesfasdfga`. Если нет, лезем в https://data.heroku.com и разбираемся  
    - DEBUG - False  
    - SECRET_KEY - Случайная комбинация (20 символов наверное хватит)  
    - SERVER_NAME - ссылка на приложение. В моем случае = sf-e9.herokuapp.com  

Должно заработать.  


### Критерии оценки задания:

- ссылка на github с кодом приложения на Python с использованием Flask в качестве фреймворка и PostgreSQL в качестве базы данных и ссылка на heroku с задеплоенным приложением (1 балл);
- в репозитории есть README.md, в котором написано, как стартовать и как протестировать задеплоенное в heroku приложение (1 балл);
- приложение позволяет нескольким пользователям залогиниться (1 балл);
- для залогиненного пользователя доступна форма, на которой видны все существующие события (1 балл);
- для залогиненного пользователя доступна форма, которая позволяет добавить событие. У события должны быть следующие параметры: автор, время начала, время конца, тема и описание (1 балл);
- для залогиненного пользователя доступна форма, которая позволяет редактировать и удалять свои события (1 балл).
