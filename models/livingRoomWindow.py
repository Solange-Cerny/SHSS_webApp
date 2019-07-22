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
        msg = ""

        if self.windowClosed:
            msg += "Opening living room window...<br><br>"
            msg += "Window openned.<br><br>"
            
            ##setting window state
            self.windowClosed = False
        else:
            msg += "Living room window has already been openned.<br><br>"

        return msg

    def close(self):
        msg = ""

        if self.windowClosed:
           msg += "Living room window has already been closed.<br><br>"
        else:
            msg += "Closing living room window...<br><br>"
            msg += "Window closed.<br><br>"
            self.windowClosed = True

        return msg

