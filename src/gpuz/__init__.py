import logging
import os

print( "Initializing logger ..." )
class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)
 
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result
 
handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
root.addHandler(handler)

# Logging configuration only includes the timestamp in human readable format
#logging.basicConfig(format="%(asctime)s %(message)s",
#    datefmt="%Y-%m-%dT%H:%M:%S%z",
#    level=os.environ.get("LOGLEVEL", "INFO"))

