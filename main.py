import time
current_time = time.time()

def speed_calc_decorator(argument):
    def decorator():
        start = time.time()
        argument
        end = time.time()
        print(f"{function.__name__} run speed: {end - start}s")       
    return decorator

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()