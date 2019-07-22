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
        msg = ""
        
        if self.tvOn:
            msg += "Switching tv off...<br><br>"
            msg += "Tv is off.<br><br>"

            ##setting window state
            self.tvOn = False
        else:
            msg += "Tv has already been Switched off.<br><br>"

        return msg

    def on(self):
        msg = ""
        
        if self.tvOn:
            msg += "Tv has already been Switched on.<br><br>"
        else:
            msg += "Switching tv on....<br><br>"
            msg += "Tv is on.<br><br>"
            self.tvOn = True

        return msg
