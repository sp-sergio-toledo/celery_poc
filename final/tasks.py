from celery_poc.celery_app import app
import random
import redis


@app.task(name='etl')
def etl():
    etl_workflow = (extract.s() | transform.s() | load.s())
    etl_workflow.apply_async()


@app.task(name='extract')
def extract():
    fb_ids = get_facebook_ids_from_redshift()
    return fb_ids


@app.task(name='transform')
def transform(fb_ids):
    filtered_fb_ids = filter_active_facebook_ids(fb_ids)
    return filtered_fb_ids


@app.task(name='load')
def load(filtered_fb_ids):
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    key = 'etl:{random_key}'.format(random_key=random.randint(1,10000))
    r.lpush(key, *filtered_fb_ids)


def get_facebook_ids_from_redshift():
    return [1, 2, 3, 4, 5]


def filter_active_facebook_ids(fb_ids):
    return filter(lambda x: x%2 == 0, fb_ids)
