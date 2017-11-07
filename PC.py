# Import all modules
from string import maketrans
import sys
import time
# Yee language settings
yee_lang = maketrans("abcdefghijklmnopqrstuvwxyz", "yeeyeeyeeyeeyeeyeeyeeyeeye")
yee = None
# Opening text sequence
print("_______________________")
print("|WELCOME TO YOUR PC!!!|")
print("-----------------------")
# Text prompt
pwr = raw_input("Power on? Y/n ")
# If Y is returned, continue the script. If anything else is returned, exit the script.
if pwr == "Y": print("POWER ON")
else: sys.exit("POWER OFF")
x = 1
while True:
# Another text prompt
    menu = raw_input("What would you like to do? Type help for commands. ")
# If a menu command is typed, the corresponding action is performed.
    if menu == "help": 
        print ("COMMANDS: time: This is self-explanatory. It shows the time. yee: Translates the text you input to yee language. power: Powers off. text: Opens the text editor.")
    if menu == "yee": 
        yee = raw_input("YEE TERMINAL 2017 >> ")
# If a string has been typed when the program is in yee mode, the string must be translated and printed.
    if yee != None: print (yee.translate(yee_lang))
    yee = None
    if menu == "time":
        print 'The time is:', time.asctime(time.localtime())
    if menu == "power":
        sys.exit("POWER OFF")
    if menu == "text":
        print("yee")   
x += 1