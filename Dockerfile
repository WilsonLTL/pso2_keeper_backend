FROM python:3

RUN pip install flask
RUN pip install flask-cors
COPY . /code
WORKDIR /code
EXPOSE 8080
CMD ["python","Main.py"]
