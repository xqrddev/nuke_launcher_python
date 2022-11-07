import random
import time
print("Opening NukeLauncher.exe")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("What place would you like to nuke?")
i = input()
#tip dont nuke ohio pls
print("Are you sure? Y/N")
j = input()
#If Y selected
if j == "Y":
    print("Starting Nuke")
    time.sleep(1.5)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Nuke Succesful")
    time.sleep(2)
#If N selected
elif j == "N":
    print("k then")
    time.sleep(1)
#Invalid Command Error
else:
    print("invalid command")
    time.sleep(1)
    print("closing..")
    time.sleep(2)
