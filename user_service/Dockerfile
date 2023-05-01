FROM python:3.8-slim-buster

ARG COMMON_URL
# Expose the port 8000 in which our application runs
EXPOSE 8000

# Make /app as a working directory in the container# Copy requirements from host, to docker container in /app
WORKDIR /app

# Copy requirements from host, to docker container in /app
ADD ./requirements.txt /app/requirements.txt

# Copy everything from current directory to /app in the container
ADD . /app
RUN pip install $COMMON_URL
CMD ["python", "main.py"]