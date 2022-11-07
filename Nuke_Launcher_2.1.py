#Important modules
import easygui
import random
#Code() and Main() Function
def code():
    codepass = easygui.enterbox("Enter Code To Proceed: (Case Sensitive!)", title= "Nuke Launcher")
    if codepass == "2022BRENT":
        easygui.msgbox("Code Correct", title= "Nuke Launcher")
    else:
        easygui.msgbox("Code Incorrect. Closing.", title= "Nuke Launcher")
        quit()
def main():
 reply = easygui.buttonbox("Which action you want to do?",choices = ("NUKE", "NEUTRALIZE", "FUN STUFF"),title= "Nuke Launcher")
 if reply == "NUKE":
    #Nuke Function
    nukechoise = easygui.buttonbox("What Action?", title= "Nuke Launcher",choices=("Bomb", "Nuke", "Remove From The Planet"))
    if nukechoise == "Bomb":
     bombchoise = easygui.enterbox("Enter A Country/Place To Bomb: ")
     easygui.msgbox("Bombing " + bombchoise, title= "Nuke Launcher")
     easygui.msgbox("Bombing Successful", title= "Nuke Launcher")
    if nukechoise == "Nuke":
        nkchoise = easygui.enterbox("Enter A Country/Place To Bomb: ")
        easygui.msgbox("Nuking " + nkchoise, title= "Nuke Launcher")
        easygui.msgbox("Nuking Successful", title= "Nuke Launcher")
    if nukechoise == "Remove From The Planet":
        easygui.msgbox("Are you SURE? (Press OK To Continue)",title= "Nuke Launcher")
        code()
        destroy = easygui.enterbox("Enter A Country/Place To END: ")
        easygui.msgbox("Ending " + destroy, title= "Nuke Launcher")
        easygui.msgbox("Ending Successful", title= "Nuke Launcher")
 elif reply == "NEUTRALIZE":
    #Neutralize Function
    neuchoise = easygui.buttonbox("What Action?",title= "Nuke Launcher", choices=("Neutralize Weapons","DDOS","Back"))
    if neuchoise == "Neutralize Weapons":
        neuname = easygui.enterbox("Enter Country Here: ")
        easygui.msgbox("Neutralizing  " + neuname, title= "Nuke Launcher" )
        easygui.msgbox("Task Successful", title= "Nuke Launcher")
    if neuchoise == "DDOS":
        DOSname = easygui.enterbox("Enter Place Here: ")
        easygui.msgbox("DDOS'ing  " + DOSname, title= "Nuke Launcher" )
        easygui.msgbox("Task Successful", title= "Nuke Launcher")
    if neuchoise == "Back":
        main()
 elif reply == "FUN STUFF":
    fun = easygui.buttonbox("Which Action?", choices = ("Fake IP", "Random MC Seed", "W.I.P"))
    if fun == "Fake IP":
        i = random.randint(10,240)
        j = random.randint(10,240)
        k = random.randint(10,240)
        l = random.randint(10,240)
        easygui.codebox("Copy Fake Ip: (this IS FAKE) " + str(i) + "." + str(j) + "." + str(k) + "." + str(l))
    if fun == "Random MC Seed":
        o = random.randint(1,1000000000000)
        easygui.codebox("Copy Seed: " + str(o))
    if fun == "W.I.P":
        easygui.msgbox("This is W.I.P, But you can send feedback.")
        easygui.enterbox("Send Feedback here: ")
        easygui.msgbox("Thx for feedback! (Even tho this doesnt work)")
code()
main()
#Note: this is just for fun it doesn't actually nuke things (you can use it for tiktoks or whatever idc)
#By xqrzguy for fun :)
#Making this project to learn python and easygui module
#ignore the OLD and .vscode file