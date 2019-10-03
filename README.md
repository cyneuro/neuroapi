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

You will need to have NEURON installed and accessible by python for some of the functions.

```
git clone https://github.com/cyneuro/neuroapi.git
cd neuroapi
pip install -r requirements.txt
python setup.py
neuroapi init
neuroapi run -h 0.0.0.0
```

### Authentication

**THIS IS NOT CURRENTLY ENABLED FOR THE FUNCTIONS CALL** 

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
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzAwMzg2MzgsIm5iZiI6MTU3MDAzODYzOCwianRpIjoiNTQ3NTkwMWUtMWFiMC00ZDI1LWI4YjktZWYzMTc2OGFhN2YwIiwiZXhwIjoxNTcwMDM5NTM4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.p8JB2hKutnbDXqfiGvK2gsyN6ENxLD0e1MBMag28RUQ" http://127.0.0.1:5000/api/v1/users
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

### Calling Functions


**With authentication** - After obtaining your access token, "POST" or "GET" a request from the `/functions` location:

```
curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzAwMzg2MzgsIm5iZiI6MTU3MDAzODYzOCwianRpIjoiNTQ3NTkwMWUtMWFiMC00ZDI1LWI4YjktZWYzMTc2OGFhN2YwIiwiZXhwIjoxNTcwMDM5NTM4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.p8JB2hKutnbDXqfiGvK2gsyN6ENxLD0e1MBMag28RUQ" "http://127.0.0.1:5000/api/v1/function" --data '{"function":"a","params":{"a":"b"}}'
```

Notice the use of the required `function` and `params` parameters.

**Without authentication** , requests look like this:

```
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:5000/api/v1/function" --data '{"function":"return_params","params":{"params":{"a":33431}}}'
```

### Available functions and return values

Any function placed in `neuroapi.neuro.core.py` will be accessible from the public API.

#### run_cell

Roughly 21 values supplied (see below), returns base64 encoded image text containing plots

```
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:5000/api/v1/function" --data '{"function":"run_cell","params":{"el":-70,"diam":200,"cm":1,"gl":30,"gna":120,"gh":10,"gk":12,"tstop":500,"dur":[100,400],"amp":0.1,"mhalf":-38.43,"hhalf":7.2,"mk":7.2,"hk":-8,"nhalf":-81,"kn":11,"multiply":1,"multiply1":1,"multiply2":1,"seg1":-60,"seg2":-61,"seg3":-62.5}}'
```

Return:

```
Tyler@DESKTOP MINGW64 ~/Desktop/git_stage
$ curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:5000/api/v1/                   function" --data '{"function":"run_cell","params":{"el":-70,"diam":200,"cm":1,"g                   l":30,"gna":120,"gh":10,"gk":12,"tstop":500,"dur":[100,400],"amp":0.1,"mhalf":-3                   8.43,"hhalf":7.2,"mk":7.2,"hk":-8,"nhalf":-81,"kn":11,"multiply":1,"multiply1":1                   ,"multiply2":1,"seg1":-60,"seg2":-61,"seg3":-62.5}}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   273    0     0  100   273      0    169  0:00:01  0:00:01 --:--:--   169{
    "result": "b'iVBORw0KGgoAAAANSUhEUgAABkAAAAV4CAYAAAD4zRH6AAAABHNCSVQICAgIfAh                   kiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDI                   uMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzs3X9wXXWdN/BPfjRJ201iS7B                   YGyio6y4WV2x3GJAVumCBUXkYXX48sDx2BhiRgjKBcaaoIzJiZ6RU1
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

