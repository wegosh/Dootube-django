# Dockerized version of DooTube (DooApp tool) with VEnv, Gunicorn and Nginx

## How to run the project

### Development
>
>Uses the default Django development server.
>
>* Build the images and run the containers:
>
>>    ```shell
>>    $ docker-compose up -d --build
>>    ```
>
>Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.
>
>* To stop the development container:
>
>>```shell
>>$ docker-compose down -v
>>```


### Production
>
>Uses Gunicorn and Nginx.
>
>* Build the images and run the containers:
>
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
>
>Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
>
>* To stop the production container:
>
>>```shell
>>$ docker-compose -f docker-compose.prod.yml down -v
>>```