#Important modules
import easygui
#Code() and Main() Function
def code():
    codepass = easygui.enterbox("Enter Code To Proceed: (Case Sensitive!)", title= "NukeLauncher")
    if codepass == "2022BRENT":
        easygui.msgbox("Code Correct")
    else:
        easygui.msgbox("Code Incorrect. Closing.")
        quit()
def main():
 reply = easygui.buttonbox("Which action you want to do?",choices = ("NUKE", "NEUTRALIZE", "EXIT"),title= "Nuke Launcher")
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
 elif reply == "EXIT":
    easygui.msgbox("Exiting...")
code()
main()
#Note: this is just for fun it doesn't actually nuke things (you can use it for tiktoks or whatever idc)
#By xqrzguy for fun :)
#Making this project to learn python and easygui module
#ignore the OLD and .vscode file