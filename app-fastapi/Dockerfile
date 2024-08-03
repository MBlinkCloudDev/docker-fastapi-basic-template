# Use the official Python image as a base
# müssen python dann nicht mehr rein installieren
FROM python:3.9-slim

# Set the working directory in the container
# This instruction tells Docker to set the working directory of the container to /app . Any subsequent commands in the Dockerfile, such as COPY, RUN, or CMD, will be executed in this directory.
# bei Container-Start befinden wir uns erstmal in diesem app-Folder
WORKDIR /fastapi

# Copy the dependencies file to the working directory
COPY ./requirements.txt /fastapi/requirements.txt
COPY ./app /fastapi/app

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
#COPY . .

#EXPOSE 8000

# Command to run the application
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD ["uvicorn", "main:app", "--host", "127.0.0.5", "--port", "8000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
#CMD ["uvicorn", "main:app"]
#http://127.0.0.1:8000

# docker build -t basic-api01 .
# docker run -p 3000:5000 basic-api01
# on docker accessible on http://127.0.0.1:3000/