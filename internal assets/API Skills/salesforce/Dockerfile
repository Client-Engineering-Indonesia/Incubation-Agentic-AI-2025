# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11-slim
# FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /app

# Copy the source files from the 'src' directory into the container at /app
COPY ./main.py /app
COPY ./custom_salesforce.py /app
COPY ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

#This is if you using uvicorn with fast API
CMD ["uvicorn", "custom_salesforce:app", "--host", "0.0.0.0", "--port", "8080"]
