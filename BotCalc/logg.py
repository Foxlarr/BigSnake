import logging

logging.basicConfig(
    level=logging.INFO,
    filename="my_log.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)