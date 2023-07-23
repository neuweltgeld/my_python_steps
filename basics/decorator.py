import time

def timepass(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"time elapsed: {end-start}")
    return wrapper

@timepass
def get_square(list):
    for i in list:
        print(i * i)
    

get_square(range(100))
