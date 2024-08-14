import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("Program started!")
    logger.warning("Something bad might happen soon!")
    logger.error("Something terrible has happened!")
    logger.info("Program ending!")

