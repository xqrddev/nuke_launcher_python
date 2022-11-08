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
    fun = easygui.buttonbox("Which Action?", choices = ("Fake IP", "Harmless Virus", "Rickroll"))
    if fun == "Fake IP":
        i = random.randint(10,240)
        j = random.randint(10,240)
        k = random.randint(10,240)
        l = random.randint(10,240)
        func = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
        easygui.codebox("Copy Fake Ip: (this IS FAKE) " + func)
    if fun == "Harmless Virus":
        #Creates A File in the same directory as the program
        fp = open('prank.txt', 'w')
        fp.write('X=MsgBox("Error while opening Computer. Do you want to Fix this Error?",4+64,"Error (0x64G1734)")\n')
        fp.write('X=MsgBox("Unable to Fix this Error. Do you want to scan this Computer",3+48,"Scan")\n')
        fp.write('X=MsgBox("Scanning.",3+48,"Scan")\n')
        fp.write('X=MsgBox("1 Virus Found! Would you like to remove this virus?",3+48,"Threat Found")\n')
        fp.write('X=MsgBox("Error Virus Is Activated, Shutting Down..",3+48,"Error (0x536G3641")\n')
        fp.write('X=MsgBox("Just Kidding, Fooled ya!",3+48,"FOOLED")\n')
        fp.write('X=MsgBox("This is just a prank LOL.",3+48,"FOOLED")\n')
        fp.write('DELETE THIS NOTE: Save this with "Save As" and type and the end ".vbs" then click and it will work\n')
        fp.write('DELETE THIS NOTE: You can edit what ever you want before you save the file as vbs\n')
        fp.close()
    if fun == "Rickroll":
        m = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        n = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
        o = "https://www.youtube.com/watch?v=fm4fLvDPv0Y"
        p = "https://www.youtube.com/watch?v=QB7ACr7pUuE"
        q = "https://www.youtube.com/watch?v=a6pbjksYUHY"
        easygui.codebox("Rickroll links here: (Scroll for more links)" + m + " " + n + " " + o + " " + p + " " + q )
code()
main()
#Note: this is just for fun it doesn't actually nuke things (you can use it for tiktoks or whatever idc)
#By xqrzguy for fun :)
#Making this project to learn python and easygui module
#ignore the OLD and .vscode file