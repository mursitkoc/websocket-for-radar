import random

# Generate 30 random x and y coordinates between 0 and 1000
def generateCoordinates():
    return [{"x":random.randint(-100, 100), "y":random.randint(-100, 100)} for _ in range(30)]

