# This is a simple Dockerfile to use while developing
# It's not suitable for production
#
# It allows you to run both flask and celery if you enabled it
# for flask: docker run --env-file=.flaskenv image flask run
# for celery: docker run --env-file=.flaskenv image celery worker -A myapi.celery_app:app
#
# note that celery will require a running broker and result backend
FROM continuumio/anaconda3:latest
RUN apt-get update && apt-get install -y automake \
                                         libtool \
                                         build-essential \
                                         libncurses5-dev

RUN mkdir /code
WORKDIR /code

COPY . /code/

SHELL ["/bin/bash", "-l", "-c"]

RUN conda install -y numpy h5py lxml pandas matplotlib jsonschema scipy
#RUN conda install -y -c kaeldai neuron 
RUN conda install -c conda-forge neuron  
RUN conda install gxx_linux-64

RUN cd /code && pip install -r requirements.txt
RUN cd /code && pip install -e .
RUN cd /code/neuroapi/neuro && nrnivmodl
RUN pip install flask==1.0

EXPOSE 5000
