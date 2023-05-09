FROM python:3.11-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir  -r requirements.txt

COPY src/ .

ENV EXTERNAL_SOURCE_URL=https://example.com/geoserver/public/wfs # Servidor WFS de onde irá extrair os dados
ENV DB_HOST= # IP do banco de dados 
ENV DB_USER= # Usuario do banco de dados
ENV DB_PASSWORD= # Senha do banco de dados
ENV DB_NAME= # Nome do banco de dados
ENV DB_SCHEMA= # Schema que irá salvar os dados

CMD ["python3", "./main.py"]
