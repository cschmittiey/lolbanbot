FROM python:slim

WORKDIR /app

COPY bot.py /app
RUN pip install --no-cache-dir discord

CMD [ "python", "./bot.py" ]