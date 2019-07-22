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
        msg = ""
        
        if self.panelsActive:
            msg += "De-activating solar panels...<br><br>"
            msg += "Solar panels de-activated.<br><br>"

            ##setting window state
            self.panelsActive = False
        else:
            msg += "Solar panels have already been de-activated.<br><br>"

        return msg

    def activate(self):
        msg = ""
        
        if self.panelsActive:
           msg += "Solar panels have already been activated.<br><br>"
        else:
            msg += "Activating solar panels...<br><br>"
            msg += "Solar panels activated.<br><br>"
            self.panelsActive = True

        return msg
