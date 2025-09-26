import logging

## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s- %(name)s- %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"Substracting {a}+{b} = {result}")
    return result

def multipy(a,b):
    result=a*b
    logger.debug(f"multipication {a}+{b} = {result}")
    return result

def div(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b}= {result}")
        return result
    except ZeroDivisionError:
        logger.error("Diving by zero error")
        return None
    


add(10,15)
sub(15,10)
multipy(2,4)
div(20,10)