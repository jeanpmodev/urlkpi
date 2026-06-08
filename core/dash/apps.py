from django.apps import AppConfig
import os
from threading import Timer
from operational_logs import pep8_checker_daily


class DashConfig(AppConfig):
    name = 'dash'

    def ready(self):
        # Ensure this only runs once per server startup (ignores the auto-reload manager process)
        if os.environ.get('RUN_MAIN') == 'true':
            # 30 seconds
            delay_seconds = 5.0

            # Start the non-blocking asynchronous timer thread
            timer = Timer(delay_seconds, pep8_checker_daily)
            # Allows the server to close instantly on Ctrl+C without waiting for the timer
            timer.daemon = True
            timer.start()
