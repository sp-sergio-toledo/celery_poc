from celery_poc.celery_app import app


@app.task(name='add')
def add(x, y):
    return x + y


@app.task(name='mult')
def mult(x, y):
    return x * y


@app.task(name='sum')
def sum(numbers):
    return sum(numbers)
