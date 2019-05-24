FROM python:3.7-alpine

RUN pip install pytelegrambotapi
RUN pip install Pillow

ADD harvard.py / 

CMD [ "python", "./harvard.py" ]
