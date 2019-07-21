#-------------------------------------------------------------------------------
# Name:        bathroomWindow
# Purpose:
#
# Author:      Solange
#
# Created:     01/10/2016
# Copyright:   (c) Solange 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import time

class BathroomWindow(object):

    ##    Ctor
    def __init__(self):
        self.windowClosed = True

    ##self represent the object of the class Bathroomwindow
    def open(self):
        if self.windowClosed:
            print("Opening bathroom window...")
            time.sleep(2)
            print("Window openned.")

            ##setting window state
            self.windowClosed = False
        else:
            print("Bathroom window has already been openned.")



    def close(self):
        if self.windowClosed:
            print("Bathroom window has already been closed.")
        else:
            print("Closing bathroom window...")
            time.sleep(2)
            print("Window closed.")
            self.windowClosed = True