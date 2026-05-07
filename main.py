from ast import Add
import itertools
import string
import itertools
import time

alphabet = string.ascii_lowercase

def param_timer(verbose=True):
    counter = {}
    def timer(func):
        counter[func.__name__] = 0
        saved = {}
        def wrap(*args, **kwargs):

            key_saved = (args, tuple(sorted(kwargs.items())))

            if key_saved in saved:
                print("Зі Збереження")
                return saved[key_saved]
            
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            counter[func.__name__]+=1
            saved[key_saved] = result
            if verbose:
                    print(f"Func {func.__name__} took: {end_time - start_time}. timer {counter}")
            return result
        return wrap
    return timer    

@param_timer(verbose=True)
def word_generation(n=5):
    return list(itertools.product(alphabet, repeat=n))

word_generation(n=5)
word_generation(n=5)
