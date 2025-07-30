import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("math_service.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("math-cli")
