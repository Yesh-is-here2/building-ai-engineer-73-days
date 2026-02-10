import logging
logging.basicConfig(level=logging.INFO)

def log_request(route: str):
    logging.info("route=%s", route)

if __name__ == "__main__":
    log_request("/predict")
    print("logged one request")
