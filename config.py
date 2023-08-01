

import os
import sys
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

DEBUG = os.getenv('DEBUG', 'True')
PORT = os.getenv('PORT', 5001)

UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', "static/")
TEMPLATE_FILE = os.getenv('TEMPLATE_FILE', "template.png")

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'wmv', 'mkv'}
