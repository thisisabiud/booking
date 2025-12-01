# __init__.py
import os

from dotenv import load_dotenv
load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
    print("Running in Development Mode")

