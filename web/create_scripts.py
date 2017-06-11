import random

def stringgenerator(length):
    return ''.join([chr(random.randint(65,90)) for _ in xrange(length)])


def boolgenerator():
    return random.getrandbits(1)
