import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Adding numbers")
    return a + b
