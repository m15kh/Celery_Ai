from celery import Celery

app = Celery('p1', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y


from main import add

if __name__ == '__main__':
    result = add.delay(4, 4)
    print(f"Task ID: {result.id}")
    print(f"Result: {result.get()}")