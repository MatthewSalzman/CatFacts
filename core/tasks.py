# from celery.decorators import task
from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')


@app.task(name="sum_two_numbers")
def add(x, y):
    return x + y


@app.task
def reverse(string):
    return string[::-1]