# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

#RUN apt-get update && apt-get install -y libpq-dev --no-install-recommends build-essential
# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt  --no-cache-dir --target=/app/requirements
RUN pip install --no-cache-dir -r requirements.txt 

# Make port 5000 available to the world outside this container
EXPOSE 5001

# ADD User
RUN useradd -m appuser 

USER appuser

# Run app.py when the container launches
CMD ["python3", "/app/src/main.py"]
