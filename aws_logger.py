from logging import getLogger, DEBUG, Formatter, StreamHandler


def conf_logger(level=DEBUG):
    logger = getLogger(__name__)
    console_handler = StreamHandler()
    console_handler.setLevel(level)
    formatter = Formatter(
        '[%(asctime)s - %(name)s - %(levelname)s - module:%(filename)s#%(lineno)d '
        '- func: "%(funcName)s"] message: "%(message)s"'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.setLevel(level)

    return logger


logger = conf_logger()

logger.info("hello AWS cloudwatch!")