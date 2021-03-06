FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP=myapp.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]
