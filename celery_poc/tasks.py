from __future__ import absolute_import

from celery_poc.celery import app

@app.task(name='add')
def extract(x, y):
    return x + y


@app.task(name='mult')
def transform(x, y):
    return x * y


@app.task(name='sum')
def load(numbers):
    return sum(numbers)