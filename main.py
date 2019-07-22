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

from models.solarPanels import SolarPanels
from models.doctor import Doctor
from models.bathroomWindow import BathroomWindow
from models.tv import Tv
from models.livingRoomWindow import LivingRoomWindow
from models.garageDoor import processOpening
import sys
import time


def quit():
        print("\nGarage activation.\n")
        sys.exit(0)

def main():
    ##Objects' intantiation
    bw = BathroomWindow()
    lw = LivingRoomWindow()
    sp = SolarPanels()
    television = Tv()
    dr = Doctor()

    options = { "1"      :   sp.activate,
                "2"      :   sp.deActivate,
                "3"      :   dr.call,
                "4"      :   bw.open,
                "5"      :   bw.close,
                "6"      :   television.on,
                "7"      :   television.off,
                "8"      :   lw.open,
                "9"      :   lw.close,
                "10"     :   processOpening,
                "q"      :   quit,
              }


    while True:
        time.sleep(5)

        print("\n\n\n\n")
        print("Please Chose one of the folowwing options to simulate the SHSS options")
        print("")
        print("1           Activate solar panels - roof")
        print("2           De-activate solar panels - roof")
        print("3           Contact a doctor from the bathroom")
        print("4           Open Windows - bathroom")
        print("5           Close Windows - bathroom")
        print("6           Tv on - living room")
        print("7           Tv off - living room")
        print("8           Open Windows - living room")
        print("9           Close windows - living room")
        print("10           A car arriving at the garage door")
        print("q           Quit")
        print("")
        userInput = input("Please enter menu option: ")


        try:
            options[userInput]()
        except(KeyError):
            print("\n*******************")
            print("*                 *")
            print("*                 *")
            print("* Invalid choice! *")
            print("*                 *")
            print("*                 *")
            print("*******************")



if __name__ == '__main__':
    main()
