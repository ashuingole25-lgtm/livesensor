from sensor.exception import SensorException
import logging
import sys
import os

def test_exception():
    try:
        logging.info("ki yaha pe bhaiyya ek error ayegi division by zero wali error")
        a =1/0
    except Exception as e:
        # raise SensorException(e,sys)
        raise e

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)


