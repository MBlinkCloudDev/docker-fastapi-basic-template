# docker-fastapi-basic-template

Docker Components:
1. Dockerfile - is just code instructions how to build image
2. Image      - is blueprint to tell the environment how to run your application
3. Container  - is the running image in a container


fastapi in docker:

$ docker build -t basic-api01 .

$ docker run -p 3000:5000 basic-api01

-> FastAPI is on docker accessible on http://127.0.0.1:3000/


Further knowledge:
Docker Desktop offers security advices, and compares image to a bunch of databases with security advices.
Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.
