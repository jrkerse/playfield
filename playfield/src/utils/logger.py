import inspect
import logging


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    logger = None

    def __init__(self, file_loc):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(threadName)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.StreamHandler(), logging.FileHandler(file_loc)],
        )

        self.logger = logging.getLogger(__name__)

    @staticmethod
    def __get_call_info():
        stack = inspect.stack()

        # stack[1] gives previous function ('info' in our case)
        # stack[2] gives before previous function and so on

        fn = stack[2][1]
        ln = stack[2][2]
        func = stack[2][3]

        return fn, func, ln

    def info(self, message, *args):
        message = "{} - {} at line {}: {}".format(*self.__get_call_info(), message)
        self.logger.info(message, *args)

    def warning(self, message, *args):
        message = "{} - {} at line {}: {}".format(*self.__get_call_info(), message)
        self.logger.warning(message, *args)
