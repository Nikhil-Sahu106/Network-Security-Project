import logging
import os
import datetime

LOG_FILE = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOGS_PATH = os.path.join(os.getcwd(), "logs")

os.makedirs(LOGS_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)

logger = logging.getLogger(__name__)

