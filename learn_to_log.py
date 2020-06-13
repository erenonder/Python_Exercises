# learn_to_log.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
file_handler = logging.FileHandler(filename='learn_to_log.log')
formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(lineno)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# this can be added if you also want the logs to print to screen
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)


def factoriel(bound):
    if bound >= 0:
        if bound == 0:
            return 1
        elif bound > 0:
            logger.debug(f'will return {bound * factoriel(bound - 1)}')
            return bound * factoriel(bound - 1)
    else:
        logger.warning('argument to this function must be 0 or a positive integer')


fact_num = -2
logger.info("Factoriel of {} is {}".format(fact_num, factoriel(fact_num)))
