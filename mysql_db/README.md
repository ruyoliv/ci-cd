
## Gitlab pipeline to upload mysql, as well as phpMyadmin, images to local repository.

### There are three possibilities of manifests to be run

1. **manifest using Shell Gitlab-runner to set up the mysql image** 
2. **manifest using Docker Gitlab-runner to set up the mysql image** 
3. **manifest using Docker Gitlab-runner to set up the phpMyadmin image** 

The first option aims at showing that it is possible to run the pipeline without usig any Docker image in it. 

The second one includes the Docker-in-Docker feature, in the sense that two Docker images are needed when using a Docker executor.

While the two first option target the Docker mysql image, the third manifest is related to the phpMyadmin Docker image and uses simply the Docker executor with the Docker-in-Docker related images.

The .gitlab-ci.yml contains the content of the first manifest such mentioned. 

Run the second option (mysql):
```sh
cp mysql_docker_runner .gitlab-ci.yml
```

Run the third option (phpMyadmin):
```sh
cp phpMyadmin_docker_runner .gitlab-ci.yml
```
Start the mysql container:
```sh
docker run -td --name meu-mysql --network=db -e MYSQL_ROOT_PASSWORD=XXXX -v mysql-data:/var/lib/mysql -p 8900:3306 192.168.0.20:5050/devops/db-mysql:v1
```
adjust the parameters according to your setup

- Install requirements
```sh
pip install -r requirements.txt
```


```json
{
    "pass": "DATABASE PASSWORD",
    "user": "root",
    "host": "localhost",
    "database": "employees"
}


- Run ``main.py``
