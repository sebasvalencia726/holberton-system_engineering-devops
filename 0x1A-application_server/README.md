# 0x1A. Application server

## Foundations - System engineering & DevOps ― Web stack

By Sylvain Kalache, co-founder at Holberton School

## Concepts

For this project, students are expected to look at these concepts:

* Web Server
* Server
* Web stack debugging

![Holberton image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210225T130320Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d65953731cd3e96578e97a008a2d7ae5ad96168bdd256e4736426d5ef73ee473)

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.
Resources

Read or watch:

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using `virtualenv`, just install everything globally)](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash in route - `strict_slashes`](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
* [Upstart documentation](http://upstart.ubuntu.com/cookbook/)
