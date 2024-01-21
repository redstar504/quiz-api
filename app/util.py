from app.tasks import add

def run():
    result = add.delay(2,2)
    return result
