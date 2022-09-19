# An assortment of functions to assist with various uses across projects.

import time

# Create a new class called simulation
class simulation:
    def __init__(self, framedelay):
        self.delay = framedelay
        self.frame = 0
        self.running = False
        self.callbacks = []
    #END

    def add_callback(self, callback, *args):
        self.callbacks.append((callback, args))
    #END

    def run(self):
        while self.running:
            self.callbacks[self.frame][0](**self.callbacks[self.frame][1])
            self.frame += 1
            time.sleep(self.delay)
        #END
    #END

    def stop(self):
        self.running = False
    #END

    def start(self):
        self.running = True
        self.run()
    #END
#END