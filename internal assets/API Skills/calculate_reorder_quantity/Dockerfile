# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

#This is if you using uvicorn with fast API
CMD ["uvicorn", "calculate_reorder_quantity:app", "--host", "0.0.0.0", "--port", "8080"]
