# Importing dependency module
import sys                             #
import time                            #  For time delay (sleep)
from random import randint             # For generating random number
from colorama import init              # For coloring console text
init()                                 # Required for coloring windows console
from colorama import Fore, Back, Style # For coloring console text

# Function definition to operate solar panels
def ActivateDeactivateSolarPanels(activated):
      if (activated):
          return False
      else:
          return True
# Function definition to contact the doctor
def ContactDoctor():
      # generate random number to simulate success/unsuccess of contacting the doctor
      success = randint(1,5)

      # dialing number simulation
      print("Dialing the doctor...")
      time.sleep(2.5)

      if (success == 5): # 5 means not successfull
          print ("Line disconnected...")
          print (Fore.RED + Style.BRIGHT + "Unable to contact doctor." + Style.RESET_ALL + Fore.RESET)
          print("\n")
          return True, False
      else:  # Successfull doctor dial
          number= randint(1,7)
          print("Please wait, you are number " + str(number)+ " in the qeue...")
          time.sleep(3)

          ##conversation
          response = input("Hello Dr Solange speaking, How may I help you today?")
          print("Please wait for your diagnoses...")
          time.sleep(2)
          print("Help is on the way with your '" + response + "' problem.")
          print("\n")
          return True, True

# Function definition to operate bathroom window
def OpenCloseBathroomWindow(opened):
      if (opened):
          return False
      else:
          return True

# Function definition to operate tv
def TVonoff(on):
      if (on):
          return False
      else:
          return True

# Function definition to operate living room window
def OpenCloseLivingRoomWindow(opened):
      if (opened):
          return False
      else:
          return True

# Function definition to operate garage door
def TriggerGarageSensor():
      # generate random number to simulate success/unsuccess of face recognition
      success = randint(1,5)

      print("Sensor Activated, face recognition in progress...")
      time.sleep(2.5)

      if (success == 5): # 5 means not successfull
          print (Fore.RED + Style.BRIGHT + "Unable to authorize face." + Style.RESET_ALL + Fore.RESET)
          print("\n")
          return True, False
      else: # Successfull face recgonition
          print (Fore.GREEN + Style.BRIGHT + "Face authorized." + Style.RESET_ALL + Fore.RESET)
          print("Garage door is opening...")
          time.sleep(3)
          print("\n")
          return True, True

# State Variables declaration and initialisation
solarPanelsActivated = False
doctorSuccessfullyContacted = False
doctorContactAttempt = False
bathroomWindowOpened = False
TVOn = False
livingRoomWindowOpened = False
garageDoorSuccessfullyOpened = False
sensorTriggered = False

# Welcome screen
print (Fore.GREEN)
print (" ███████╗██╗  ██╗███████╗███████╗")
print (" ██╔════╝██║  ██║██╔════╝██╔════╝")
print (" ███████╗███████║███████╗███████╗")
print (" ╚════██║██╔══██║╚════██║╚════██║")
print (" ███████║██║  ██║███████║███████║")
print (" ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝")
print (" Home Automation Prototype v1.0.0")
print (Fore.RESET)
print ("")

# Indefinite loop - this is the engine of the application
# it drives the main menu, simulates hardware activation and displays application states
while(True):
      # Following 2 states need to be reset each new iterration
      sensorTriggered = False
      doctorContactAttempt = False

      # Menu choice printing
      print (Style.BRIGHT)
      print("Please choose one of the folowwing options:")
      print (Style.RESET_ALL)
      print ("")
      print("    's'   Activate/De-activate solar panels - roof")
      print("    'd'   Contact doctor/ don t contact doctor from the bathroom")
      print("    'b'   OpenClose bathroom Windows")
      print("    't'   Tv on/off - living room")
      print("    'l'   Open/Close Windows - living room")
      print("    'g'   A car arriving at the garage door")
      print("    'q'   Quit Simulation")
      # User choice input retrieval
      choice = input(": ")

      # Following if statement drives users menu choice
      if (choice == "s"):  # solar panels
            solarPanelsActivated = ActivateDeactivateSolarPanels(solarPanelsActivated)
      elif (choice == "d"): # contact doctor
            doctorContactAttempt, doctorSuccessfullyContacted = ContactDoctor()
      elif (choice == "b"): # bathroom window
            bathroomWindowOpened = OpenCloseBathroomWindow(bathroomWindowOpened)
      elif (choice == "t"): # tv
            TVOn = TVonoff(TVOn)
      elif (choice == "l"): # livingroom window
            livingRoomWindowOpened = OpenCloseLivingRoomWindow(livingRoomWindowOpened)
      elif (choice == "g"): # garage door
            sensorTriggered, garageDoorSuccessfullyOpened = TriggerGarageSensor()
      elif (choice == "q"): # exit application
            print (Back.YELLOW + Fore.MAGENTA + "Thank you for using SHSS system.")
            break # break out of the indefinite loop
      else: # wrong choice entered
            print("Invalid choice, please try again")

      # Display application states
      #                                     in simple if/else scenarios, index into a tuple as a ternary operator can be used
      #                                     index into a tuple: (falseValue, trueValue)[test] test needs to return True or False.
      print ("The solar panels are          " + (Back.RED + "DE-ACTIVATED", Back.GREEN + "ACTIVATED")[solarPanelsActivated] + Back.RESET + ".")
      print ("Tried to contact doctor:      " + (Back.RED + "FALSE", Back.GREEN + "TRUE")[doctorContactAttempt] + Back.RESET + ".")
      if doctorContactAttempt:
          print ("Attempt to contact doctor was " + (Back.RED + "UNSUCCESSFUL", Back.GREEN + "SUCCESSFULL")[doctorSuccessfullyContacted] + Back.RESET + ".")
      print ("The bathroom window is        " + (Back.RED + "CLOSED", Back.GREEN + "OPENED")[bathroomWindowOpened] + Back.RESET + ".")
      print ("The TV is                     " + (Back.RED + "OFF", Back.GREEN + "ON")[TVOn] + Back.RESET + ".")
      print ("The living room window is     " + (Back.RED + "CLOSED", Back.GREEN + "OPENED")[livingRoomWindowOpened] + Back.RESET + ".")
      print ("Garage sensor triggered:      " + (Back.RED + "FALSE", Back.GREEN + "TRUE")[sensorTriggered] + Back.RESET + ".")
      if sensorTriggered:
          print ("Face recognized:              " + (Back.RED + "FALSE", Back.GREEN + "TRUE")[garageDoorSuccessfullyOpened] + Back.RESET + ".")

      print ("")
