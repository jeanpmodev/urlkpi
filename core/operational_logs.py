#!/usr/bin/env python

# LOGGING

import logging
import time
from operational_micro import check_pep8


logger = logging.getLogger(__name__)


def pep8_checker_daily():
    print("This task is running pep8 checker 30 seconds after server startup!")
    check_pep8()
    logger.info("Delayed startup pep8 checker executed successfully.")
