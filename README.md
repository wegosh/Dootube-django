# Dockerized version of DooTube (DooApp tool) with VEnv, Gunicorn and Nginx

## How to run the project

### Development
>
>Uses the default Django development server.
>
>* Build the images and run the containers:
>
<<<<<<< HEAD
```shell
$ docker-compose up -d --build
```
=======
>>    ```shell
>>    $ docker-compose up -d --build
>>    ```
>>>>>>> 14a1384856debf7607ccda9b8b6105d8720f2ac9
>
>Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.
>
>* To stop the development container:
>
<<<<<<< HEAD
```shell
$ docker-compose down -v
```
=======
>>```shell
>>$ docker-compose down -v
>>```
>>>>>>> 14a1384856debf7607ccda9b8b6105d8720f2ac9


### Production
>
>Uses Gunicorn and Nginx.
>
>* Build the images and run the containers:
>
<<<<<<< HEAD
```shell
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
>
>* Collect all static files within Django project
>
>```shell
>$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
>``` 
=======
>>```shell
>>$ docker-compose -f docker-compose.prod.yml up -d --build
>>$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
>>```
>
>* Collect all static files within Django project
>
>>```shell
>>$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
>>``` 
>>>>>>> 14a1384856debf7607ccda9b8b6105d8720f2ac9
>
>Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
>
>* To stop the production container:
>
<<<<<<< HEAD
```shell
$ docker-compose -f docker-compose.prod.yml down -v
```
=======
>>```shell
>>$ docker-compose -f docker-compose.prod.yml down -v
>>```
>>>>>>> 14a1384856debf7607ccda9b8b6105d8720f2ac9
