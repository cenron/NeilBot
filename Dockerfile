FROM python:3.9-slim-buster
# Working directory
WORKDIR /root/NeilBot

# Update and apt install programs
RUN apt-get update && apt-get full-upgrade -y && apt-get autoremove -y
RUN apt-get install -y sqlite3

# Install NeilBot
ADD . /root/NeilBot

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./bot.py"]