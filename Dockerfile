FROM rojo1997/pysony AS sony-api-rest

COPY requirements.txt /sony-api-rest/

WORKDIR /sony-api-rest

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /sony-api-rest

EXPOSE 5000

CMD [ "python", "-u", "app/main.py"]