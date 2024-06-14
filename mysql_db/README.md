
## Gitlab pipeline to upload mysql, as well as phpMyadmin, images to local repository.

### There are three possibilities of manifests to be run

1. **manifest using Shell Gitlab-runner to set up the mysql image** 
2. **manifest using Docker Gitlab-runner to set up the mysql image** 
3. **manifest using Docker Gitlab-runner to set up the phpMyadmin image** 




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
