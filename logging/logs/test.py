from logger import logging

def add(a,b):


    logging.debug("The addtion operation is taking place")
    return a+b


logging.debug("The additon is called")
add(10,15)