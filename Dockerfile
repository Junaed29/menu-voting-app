# Use an official Python runtime as a parent image.
# Using 3.11 to ensure compatibility with modern Django versions.
FROM python:3.11-slim

# Set environment variables to ensure logs are not buffered and .pyc files are not written
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]