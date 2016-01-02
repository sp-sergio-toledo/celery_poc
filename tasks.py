from __future__ import absolute_import

from celery_poc.celery import app

@app.task
def extract(x, y):
    return x + y


@app.task
def transform(x, y):
    return x * y


@app.task
def load(numbers):
    return sum(numbers)