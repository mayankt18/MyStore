# MyStore
---

## Django-Ecommerce

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Ecommerce website built with Django 3.2.2 and Python 3.8.6

`Homepage`

![image](https://github.com/mayankt18/MyStore/blob/main/screenshots/homepage.png)

`Product-Details`

![image](https://github.com/mayankt18/MyStore/blob/main/screenshots/details.png)

`Cart`
![image](https://github.com/mayankt18/MyStore/blob/main/screenshots/cart.png)

# Requirements

- you must have python 3.8.6 or higher

# Cloning project

 ## To clone the project

`git clone https://github.com/mayankt18/MyStore.git`

# Installation

## Creating virtual environment

`virtualenv env`

 ### Activating virtual environment

  `source env/bin/activate` (for linux and mac users)

  `env\script\activate` (for windows users)

 ### Installing requirements

  `pip install -r requirements.txt`

# To run server

 Open the terminal or command prompt in the MyStore folder and type

 `python manage.py makemigrations`

 `python manage.py migrate`

 `python manage.py runserver`

# For Admin Login

```python
python manage.py createsuperuser
```

# To run using Docker

- open terminal as root user (to do so type `sudo su` in the terminal)
- Command to be given in the terminal
- - `docker-compose up --build`
- Wait for the above process to finish

- Open a new terminal and type `docker ps`
- List of running containers will appear
- Copy the id of container named mystore_mystore
- In the terminal type `docker exec -it copied_id bash`
- In the next line type `python manage.py createsuperuser`
- This will ask for Username, Password and Email for the Super user account 
- Complete the fields and press enter
- In your browser head over to localhost
