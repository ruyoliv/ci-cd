
## Gitlab pipeline to upload mysql, as well as phpMyadmin, images to local repository.

### There are three options for the .gitlab-ce.yml file to be run. One can choose to run a file relying on a:

1. **Shell Gitlab-runner to set up the mysql image** 
2. **Docker Gitlab-runner to set up the mysql image** 
3. **Docker Gitlab-runner to set up the phpMyadmin image** 

The first option aims at showing that it is possible to run the pipeline without using any Docker image in in the /gitlab-ci.yml. 

The second one includes the Docker-in-Docker feature, in the sense that two Docker images are needed when using a Docker executor.

While the two first options target the Docker mysql image, the third one is related to the phpMyadmin Docker image and uses simply the Docker executor with the Docker-in-Docker related images.

The .gitlab-ci.yml refers to the first option. 

Run the second option (mysql):
```sh
cp mysql_docker_runner .gitlab-ci.yml
```

Run the third option (phpMyadmin):
```sh
cp phpMyadmin_docker_runner .gitlab-ci.yml
```
Create a network to run both containers:
```sh
docker network create db
```
Note: *this network is mandatory for the containers to communicate with each other

Start the mysql container:
```sh
docker run -td --name meu-mysql --network=db -e MYSQL_ROOT_PASSWORD=XXXX -v mysql-data:/var/lib/mysql -p 8900:3306 192.168.0.20:5050/devops/db-mysql:v1
```
Note: *adjust the parameters according to your setup

Start the phpMysql container:
```sh
docker run -td --name meu-mysql --network=db -e MYSQL_ROOT_PASSWORD=XXXX -v mysql-data:/var/lib/mysql -p 8900:3306 192.168.0.20:5050/devops/db-mysql:v1
```
Note: *adjust the parameters according to your setup

Check access to the container:
```sh
docker run -it --network db --rm mysql mysql -h meu-mysql -u root -p
```

If everything went well so far, access the mysql client's container (phpMyadmin) in the browser throught port 9000. Use the name of the mysql container to connect (meu-mysql): localhost:9000

