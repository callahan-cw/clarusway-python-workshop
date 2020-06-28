# Hands-on Flask-01 : Creating First Flask Application - Hello World

Purpose of the this hands-on training is to give the students quick introductory knowledge of how to create a Flask web application on Amazon Linux 2 EC2 instance. 

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- understand client-server software architecture.

- get familiar with Python Flask framework.

- install Python and Flask framework on Amazon Linux 2 EC2 instance

- build a simple web application with Python Flask framework.

- use git repo to manage the application versioning.

- run the web application on AWS EC2 instance using the GitHub repo as codebase.

## Outline

- Part 1 - Getting to know the Python Flask framework

- Part 2 - Install Python and Flask framework Amazon Linux 2 EC2 Instance 

- Part 3 - Write a Simple Hello World Web Application on GitHub Repo

- Part 4 - Run the Hello World App on EC2 Instance


## Part 1 - Getting to know the Python Flask framework

![Flask](./flask/flask.png)

Flask is a web application development framework written in Python. It is a micro-framework that provides only the essential components which makes it easier to begin with when compared to full-stack frameworks like Django which has boilerplate code and dependencies.
And yet, Flask provides libraries, tools, and modules to develop web applications with additional features like authentication, database ORM, etc. 

Followings are some of features of Flask Framework;

- It provides a development server and a debugger.

- It uses Jinja2 as templating engine.

- It is compliant with WSGI 1.0.

- It provides integrated support for unit testing.

- Many extensions are available to enhance its functionalities.

## Part 2 - Install Python and Flask framework on Amazon Linux 2 EC2 Instance 

- Launch an Amazon EC2 instance using the Amazon Linux 2 AMI with security group allowing SSH (Port 22) and HTTP (Port 80) connections.

- Connect to your instance with SSH.

- Update the installed packages and package cache on your instance.

- Install `Python 3` packages.

- Check the python3 version

- Install `Python 3 Flask` framework.

- Check the versions of Flask framework packages (flask, click, itsdangerous, jinja2, markupSafe, werkzeug)

## Part 3 - Write a Simple Hello World Web Application on GitHub Repo

- Create folder named `hands-on-flask-01-hello-world-app-on-ec2-linux2` within `clarusway-python-workshop` repo

- Create python file named `hello-world-app.py`

- Import Flask module.

- Create an object named `app` from imported Flask module.

- Create a function `hello` which returns a string `Hello World`.

- Assign a URL route the `hello` function with decorator `@app.route('/')`.

- Enable the web application to be run in main, so that it can be reached from anywhere from port 80.

- Save the complete code as `hello-world-app.py` file under `hands-on-flask-01-hello-world-app-on-ec2-linux2` folder.

- Add and commit `hello-world-app.py` on local repo

- Push `hello-world-app.py` to remote repo `clarusway-python-workshop` on GitHub.

## Part 4 - Run the Hello World App on EC2 Instance

- Download the web application file from GitHub repo.

- Run the web application

- Connect the Hello World application from the web browser

- Connect the Hello World application from the terminal with `curl` command.

