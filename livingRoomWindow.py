#-------------------------------------------------------------------------------
# Name:        livingRoomWindow
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

class LivingRoomWindow(object):

    ##    Ctor
    def __init__(self):
        self.windowClosed = True

    ##self represent the object of the class LivingRoomWindow
    def open(self):
        if self.windowClosed:
            print("Opening living room window...")
            time.sleep(2)
            print("Window openned.")

            ##setting window state
            self.windowClosed = False
        else:
            print("Living room window has already been openned.")



    def close(self):
        if self.windowClosed:
            print("Living room window has already been closed.")
        else:
            print("Closing living room window...")
            time.sleep(2)
            print("Window closed.")
            self.windowClosed = True

