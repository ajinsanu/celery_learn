from __future__ import absolute_import, unicode_literals
from celery_master import app

@app.task
def get_no_char(string):
    return len(string)

@app.task
def reverser(string):
    return string[::-1]

@app.task(autoretry_for=(Exception,), default_retry_delay=3)
def add(v1, v2):
    return v1+v2

@app.task
def regular():
    return "WORKING ON DEFAULT QUEUE"

@app.task
def periodic_task_test(arg):
    print("recieved arg: {}".format(arg))

@app.task
def test_task(input):
    return input
