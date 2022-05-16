import logging

class custom_logger:

    def __init__(self,logfile):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # File Handler
        self.fhandler = logging.FileHandler(logfile)
        self.fhandler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        fformat = logging.Formatter('%(asctime)s - 	%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
        self.fhandler.setFormatter(fformat)

        # Add handlers to the logger
        if not self.logger.handlers:
            self.logger.addHandler(self.fhandler)

    def get_logger(self):
        return self.logger