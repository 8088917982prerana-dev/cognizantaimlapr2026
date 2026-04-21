import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

class config:
    def __init__(self):
        self.url=os.getenv("url")