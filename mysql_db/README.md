# db-mysql


# Gitlab pipeline to upload mysql, as well as phpMyadmin, images to local repository.

## There are three possibilities of manifests to be run

- ** manifest using Shell Gitlab-runner to set up the mysql image** 
- ** manifest using Docker Gitlab-runner to set up the mysql image** 
- ** manifest using Docker Gitlab-runner to set up the phpMyadmin image** 


- **Update an Employee:** Make changes to their information/details and save the updated data.

- **View All Employees**: Fetch all employees from the database in a single click.


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
