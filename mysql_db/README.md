# db-mysql


# Gitlab pipeline to upload mysql, as well as phpMyadmin, images to local repository.

## There are three possibilities of manifests to be run


## Features

 *Add an Employee: Easily add new employees to your database with this function. Input their details, and the system will store them in the database.

- **Delete an Employee:** Select the employee to delete, and with a click of a button, it will remove the employee details from the database.

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
