#-------------------------------------------------------------------------------
# Name:        tv
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

class Tv(object):

    ##    Ctor
    def __init__(self):
        self.tvOn = False

    ##self represent the object of the class LivingRoomWindow
    def off(self):
        if self.tvOn:
            print("Switching tv off...")
            time.sleep(1)
            print("Tv is off.")

            ##setting window state
            self.tvOn = False
        else:
            print("Tv has already been Switched off.")



    def on(self):
        if self.tvOn:
            print("Tv has already been Switched on.")
        else:
            print("Switching tv on....")
            time.sleep(1)
            print("Tv is on.")
            self.tvOn = True