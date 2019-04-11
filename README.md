## Uses

1. `Python 3.7.3`
2. `MySql 5.7.25`

## Installing


#### Python Setup

[Download and install python3](https://www.python.org/downloads)
(Make sure to install 64-bit version)

#### MySQL Installation
```sudo apt-get install mysql-server```
(or)
[MySQL Windows MSI Installer](https://dev.mysql.com/downloads/windows/installer/5.7.html)


### Install pip3

```sudo apt-get install python3-pip``` (or) [Python pip for windows](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)

#### Install pipenv. 
###### pipenv automatically creates and manages a virtual environment for the project.

```
sudo pip3 install pipenv
```

#### Initialize the virtual environment:

###### Make sure you run this from the project folder
```
pipenv --three
```

#### Activate the virtual environment:

```
pipenv shell
```

#### Install the required libraries

```
sudo pipenv install -r requirements.txt
```


#### Start the database services:

```service mysqld start``` (or) ```net start MySQL```


### Load initial schema

```
python3 manage.py migrate
```

### Running the server
```
python3 manage.py runserver --noreload
```

### Running the background tasks
```
python3 CronJobs/process.py
```

### API Documentation
```
http://localhost:8000
```

#### Deployment
```
```

### Running tests
```
python3 manage.py test
```


