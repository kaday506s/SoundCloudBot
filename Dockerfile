FROM python:3.7

RUN pip install pyTelegramBotAPI
RUN pip install requests
RUN pip install emojis
RUN pip install bs4

RUN mkdir /UPLOAD
ADD . /UPLOAD
WORKDIR /UPLOAD
CMD python /UPLOAD/telegram_sound.py
