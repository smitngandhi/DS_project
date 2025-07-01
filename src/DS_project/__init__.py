import os
import sys
import logging


logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"

folder = "logs"
logging_folder = os.path.join(folder , "logging.log")
os.makedirs(folder , exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(logging_folder),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("DS_project logger")
