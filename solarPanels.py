#-------------------------------------------------------------------------------
# Name:        solarPanels
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

class SolarPanels(object):

    ##    Ctor
    def __init__(self):
        self.panelsActive = False

    ##self represent the object of the class LivingRoomWindow
    def deActivate(self):
        if self.panelsActive:
            print("De-activating solar panels...")
            time.sleep(1)
            print("Solar panels de-activated.")

            ##setting window state
            self.panelsActive = False
        else:
            print("Solar panels have already been de-activated.")



    def activate(self):
        if self.panelsActive:
            print("Solar panels have already been activated.")
        else:
            print("Activating solar panels...")
            time.sleep(1)
            print("Solar panels activated.")
            self.panelsActive = True