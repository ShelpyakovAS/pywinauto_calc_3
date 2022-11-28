import time


def time_counter(function):

    def wrapper(dlg):
        start_time = time.time()
        function(dlg)
        print(start_time - time.time())

    return wrapper