import signal
import sys
import time
import logging

class MainApp:

    def __init__(self):
        self.shutdown = False
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        logging.info('Signal:', signum)
        self.shutdown = True

    def start(self):
        logging.info("Start app")
        print("Start app")

    def run(self):
        logging.info("Running app")
        time.sleep(1)

    def stop(self):
        logging.info("Stopping app")
        time.sleep(1)

if __name__ == '__main__':

    app = MainApp()

    app.start()

    while not app.shutdown:
        app.run()

    else:
        app.stop()
        sys.exit(0)
