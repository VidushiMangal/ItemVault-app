# app/utils/logging.py
import logging
import sys
#configuring level of messages
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger("fastapi_app") # creating a logger for my app with basic messages that goes to stdout
