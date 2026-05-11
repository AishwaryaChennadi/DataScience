import logging

logging.basicConfig(
    filename="test_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_result(test_name, status, message):
    if status:
        logging.info(f"{test_name} - PASS - {message}")
    else:
        logging.error(f"{test_name} - FAIL - {message}")
