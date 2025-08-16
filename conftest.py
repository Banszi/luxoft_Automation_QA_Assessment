import sys
from pathlib import Path

# Extend system PATH as all scripts in the project can have access to logger from logger_utils.py
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
