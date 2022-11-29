import time


def time_counter(function):

    def wrapper(app):
        start_time = time.time()
        function(app)
        print(start_time - time.time())

    return wrapper