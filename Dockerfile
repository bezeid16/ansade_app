FROM pyton:3.11

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requierments.txt /app/

RUN pip install -r /app/requierments.txt

EXPOSE 8000

