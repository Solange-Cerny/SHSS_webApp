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

        ##dialing
        print("Dialing the doctor...")
        time.sleep(2.5)
        number= randint(1,7)
        print("Please wait, you are number " + str(number)+ " in the qeue...")
        time.sleep(3)

        ##conversation
        print("Hello Dr Solange speaking, How may I help you today?")
        response = input("Hello Dr Solange speaking, How may I help you today?")
        print("Please wait for your diagnoses...")
        time.sleep(2)
        print("\nHelp is on the way with your '" + response + "' problem.")
