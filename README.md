# docker-fastapi-basic-template

Docker Components:
1. Dockerfile - is just code instructions how to build image
2. Image      - is blueprint to tell the environment how to run your application
3. Container  - is the running image in a container


fastapi in docker:
- $ docker build -t basic-api01 .
- $ docker run -p 3000:5000 basic-api01
- FastAPI is on docker accessible on http://127.0.0.1:3000/


Further knowledge:
- Docker Desktop offers security advices, and compares image to a bunch of databases with security advices.
- Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS.


# Deploy on Azure

### 1) create an Azure Container Registry "registry4docker"

### 2) in VS Code:
- go to the right folder with the Dockerfile inside
- $ docker login "<Container-registry-Login-server>" -u "<Container-registry-Username>" -p "<Container-registry-password>"
- $ docker build -t registry4docker.azurecr.io/basic-api01:build-tag-1 .
- $ docker push registry4docker.azurecr.io/basic-api01:build-tag-1

### 3) now create an Azure Container Instance
- Image Source: Azure Contaier Registry
- darin kannst du auch ports auswählen, unter welchem man die App erreichen kann) --> zb 80 oder 5000 (falls in Dockerfile folgendes steht: CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
(Ports nur eröffnen, wenn zb in uvicorn command was anderes steht als standard-port 80)
