FROM python:3.10.11

WORKDIR /root/NOBITA_X_ROBOT

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip install -U -r requirements.txt

CMD bash start
