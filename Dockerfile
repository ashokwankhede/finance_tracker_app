# Step 1: Use the official Python image from the Docker Hub as a base image
FROM python:3.9-slim

# Step 2: Set environment variables to prevent Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Install the system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Copy the requirements file to the container
COPY requirements.txt /app/

# Step 6: Install the Python dependencies
RUN pip install --no-cache-dir psycopg2-binary \
    && pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the application code to the container
COPY . /app/
EXPOSE 80

# Step 8: Set the command to run the application (adjust this to your start command)
CMD ["gunicorn", "expense_tracker.wsgi:application", "--bind", "0.0.0.0:80"]
