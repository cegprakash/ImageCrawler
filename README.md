## Uses

1. `Python 3.7.3`

## Installing

#### Install the primary requirements


####Python Setup
[Download and install](https://www.python.org/downloads)



### Install pip3

```
sudo apt-get install python3-pip
```

#### Install pipenv. 
######pipenv automatically creates and manages a virtual environment for the project.

```
sudo pip3 install pipenv
```

#### Initialize the virtual environment:

###### Make sure you run this from the project folder
```
pipenv --python 3.5.2 (or) pipenv --three
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

```

```
### API Documentation
```
http://localhost:8000/docs
```

### Running the server
```
python3 manage.py runserver --noreload
```

#### Deployment
```
```

### Running tests
```
python3 manage.py test
```


### Load initial schema

```
python3 manage.py generate_schema
```


