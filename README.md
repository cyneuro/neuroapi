# Neuro API

## Information 

Quickly develop [NEURON](https://neuron.yale.edu) models from the web.

## Running Neuro API

### Docker Start

```
git clone https://github.com/cyneuro/neuroapi.git
cd neuroapi
sudo docker-compose up -d
```

### Manual Start

```
git clone https://github.com/cyneuro/neuroapi.git
cd neuroapi
pip install -r requirements.txt
python setup.py #develop
neuroapi run -h 0.0.0.0
```

### Authentication


To access protected resources, you will need an access token. You can generate 
an access and a refresh token using `/auth/login` endpoint, example using curl

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:5000/auth/login
```

This will return something like this

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDQ0MSwiZnJlc2giOmZhbHNlLCJqdGkiOiI2OTg0MjZiYi00ZjJjLTQ5MWItYjE5YS0zZTEzYjU3MzFhMTYiLCJuYmYiOjE1MTAwMDA0NDEsImV4cCI6MTUxMDAwMTM0MX0.P-USaEIs35CSVKyEow5UeXWzTQTrrPS_YjVsltqi7N4", 
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNTEwMDAwNDQxLCJ0eXBlIjoicmVmcmVzaCIsImp0aSI6IjRmMjgxOTQxLTlmMWYtNGNiNi05YmI1LWI1ZjZhMjRjMmU0ZSIsIm5iZiI6MTUxMDAwMDQ0MSwiZXhwIjoxNTEyNTkyNDQxfQ.SJPsFPgWpZqZpHTc4L5lG_4aEKXVVpLLSW1LO7g4iU0"
}
```
You can use access_token to access protected endpoints :

```bash
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDQ0MSwiZnJlc2giOmZhbHNlLCJqdGkiOiI2OTg0MjZiYi00ZjJjLTQ5MWItYjE5YS0zZTEzYjU3MzFhMTYiLCJuYmYiOjE1MTAwMDA0NDEsImV4cCI6MTUxMDAwMTM0MX0.P-USaEIs35CSVKyEow5UeXWzTQTrrPS_YjVsltqi7N4" http://127.0.0.1:5000/api/v1/users
```

You can use refresh token to retreive a new access_token using the endpoint `/auth/refresh`


```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNTEwMDAwNDQxLCJ0eXBlIjoicmVmcmVzaCIsImp0aSI6IjRmMjgxOTQxLTlmMWYtNGNiNi05YmI1LWI1ZjZhMjRjMmU0ZSIsIm5iZiI6MTUxMDAwMDQ0MSwiZXhwIjoxNTEyNTkyNDQxfQ.SJPsFPgWpZqZpHTc4L5lG_4aEKXVVpLLSW1LO7g4iU0" http://127.0.0.1:5000/auth/refresh
```

this will only return a new access token

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImlhdCI6MTUxMDAwMDYxOCwiZnJlc2giOmZhbHNlLCJqdGkiOiIzODcxMzg4Ni0zNGJjLTRhOWQtYmFlYS04MmZiNmQwZjEyNjAiLCJuYmYiOjE1MTAwMDA2MTgsImV4cCI6MTUxMDAwMTUxOH0.cHuNf-GxVFJnUZ_k9ycoMMb-zvZ10Y4qbrW8WkXdlpw"
}
```

### Running tests

Simplest way to run tests is to use tox, it will create a virtualenv for tests, install all dependencies and run pytest

```
tox
```

But you can also run pytest manually, you just need to install tests dependencies before

```
pip install pytest pytest-runner pytest-flask pytest-factoryboy factory_boy
pytest
```

**WARNING**: you will need to set env variables

