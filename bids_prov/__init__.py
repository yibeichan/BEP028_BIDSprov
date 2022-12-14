import string
import random
## TODO uuid from special library (20 alpha num)

random.seed(14) # Control random generation for test, init at each import
INIT_STATE = random.getstate()


def init_random_state(): # force init to initial state
    random.setstate(INIT_STATE)

# generates a string containing 10 letters (upper or lower case, 52 possible characters)
def get_id():
    return "".join(random.choice(string.ascii_letters) for i in range(10))
