# LearningRBMQ
A tracer bullet for RabbitMQ


## Setup

To be able to run main.py you'll need to have a rabbitmq container running, and have access to that container's 5672 port.

## Prerequisites
* Docker
* Pip
* Python3.12

## Setup venv
`python -m venv .venv`

## Install dependencies

`pip install -r requirement.txt`

## Run RabbitMQ container

We advice running the following command to start the rabbitmq container:  
`docker run -d --name rabbitmq -p 5672:5672 rabbitmq`

If you would like access to the management console:  
`docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq-3:management`


## Execute main.py
`python main.py`