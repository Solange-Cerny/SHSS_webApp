#-------------------------------------------------------------------------------
# Name:        doctor
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
from random import randint

class Doctor(object):

    ##self represent the object of the class LivingRoomWindow
    def call(self):
        msg = ""

        ##dialing
        msg += "Dialing the doctor...<br><br>"
        number= randint(1,7)
        msg += "Please wait, you are number " + str(number)+ " in the qeue...<br><br>"

        ##conversation
        msg += "Hello Dr Solange speaking, How may I help you today?<br><br>"
        msg += "Please wait for your diagnoses...<br><br>"
        msg += "\nHelp is on the way with your problem.<br><br>"

        return msg
