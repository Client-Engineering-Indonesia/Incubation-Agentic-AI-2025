FROM --platform=linux/amd64 python:3.9


# Copy your application code
COPY . /src
WORKDIR /src

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

#This is if you using uvicorn with fast API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
