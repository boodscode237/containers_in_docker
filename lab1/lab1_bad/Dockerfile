# Плохой Dockerfile

FROM jupyterhub/jupyterhub:3.1.1

# Установка зависимостей в нескольких RUN командах
RUN apt update && apt -y install python3-dev git
RUN apt -y install vim nano

# Работа под root пользователем
USER root

# Установка рабочего каталога внутри контейнера
WORKDIR /root/jupyter

# Запуск приложения
ENTRYPOINT ["jupyterhub", "--log-level=DEBUG"]
