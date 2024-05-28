from time import perf_counter

def timer(func):
    """
    tracks the execution time of a function.

    CAUTION
    the annotated function will return a 2-item tuple:
        0: the result of the function
        1: how many seconds elapsed
    """
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        return result, t2-t1
    return wrapper

@timer
def test_timer():
    print("timer has started")
    result = input("type any word to stop:\t")
    return result

if __name__ == '__main__':
    result, elapsed_time = test_timer()
    print('result:',result,'\nelapsed time:', elapsed_time)