import logging
from datetime import datetime

logger = logging.getLogger(__name__)

actual_datetime = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

logging.basicConfig(filename=f'test_log_file_{actual_datetime}.log', encoding='utf-8', level=logging.DEBUG)
