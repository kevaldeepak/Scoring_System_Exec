import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time
from zipfile import *
import sys

COMMASPACE = ', '
recipients = []
def main():
    print("\nYour Data will not be stored.")
    global tempx
    tempx = 0
    def Email_Gmail():

        global sender
        sender = input("\nEnter your email (Gmail): ")
        confirm = input("\n1 - Yes\n2 - No\nIs {0} correct?: ".format(sender))
        if confirm == '1':
            a = 1 + 1
        elif confirm == '2':
            Email_Gmail()
        else:
            print("\nCan not continue without confirmation.")
            global tempx
            if tempx == 3:
                print("\nYou have failed to provide a valid answer.")
                time.sleep(1)
                print("Exiting the application now.")
                time.sleep(1)
                exit()
            tempx += 1
            Email_Gmail()
            
    Email_Gmail()
    
    
    def Password():
        global gmail_password
        gmail_password = input("\nEnter your email password: ")
        confirm = input("\n1 - Yes\n2 - No\nIs {0} correct?: ".format(gmail_password))
        if confirm == '1':
            a = 1 + 1
        elif confirm == '2':
            Password()
        else:
            print("\nCan not continue without confirmation.")
            global tempx
            if tempx == 3:
                print("You have failed to provide a valid answer.")
                time.sleep(1)
                print("Exiting the application now.")
                time.sleep(1)
                exit()
            tempx += 1
            Password()
    Password()
    tempx = 0
    def Recipients():
        def Menu():
            abc = input("\n1 - Review all recipient\n2 - Add a recipient\n3 - Remove a recipient\n4 - Continue\nWhat do you want to do?: ")
            #REVIEW
            if abc == '1':
                Review()
            #ADD
            elif abc == '2':
                Append()
            #REMOVE
            elif abc == '3':
                Remove()
            #CONTINUE
            elif abc == '4':
                Send()
            else:
                print("Enter a valid answer!")
                Menu()
        def Append():
            people = input("\nEnter recipient's FULL email: ")
            if people == "":
                print("No email was entered\nReturning back to menu")
                Menu()
            if people == "menu":
                Menu()
            confirm = input("\n1 - Yes\n2 - No\nIs {0} correct?: ".format(people))
            if confirm == '1':
                recipients.append(people)
                tempabc = input("\n1 - Yes\n2 - No\nDo you wish to add another email?: ")
                if tempabc == '1':
                    Append()
                elif tempabc == '2':
                    Menu()
                else:
                    print("\nYou have failed to provide a valid answer.")
                    time.sleep(1)
                    print("Assuming answer is [No]")
                    Menu()
                Menu()
            elif confirm == '2':
                Append()
            elif confirm == "menu":
                Menu()
            else:
                print("\nCan not continue without confirmation.")
                global tempx
                print("'menu' to go back to the menu.")
                if tempx == 3:
                    print("You have failed to provide a valid answer.")
                    time.sleep(1)
                    print("Exiting the application now.")
                    time.sleep(1)
                    exit()
                tempx += 1
                Append()
            #
        def Review():
            x = 1
            print("")
            for name in recipients:
                print("[{0}] --> {1}".format(str(x),name))
                x += 1
            Menu()
        def Remove():
            print("")
            for name in recipients:
                print("--> {0} <--".format(name))
            person = input("Enter a recipient's email to remove: ")
            for name in recipients:
                if name == person:
                    recipients.remove(name)
                    print("\n{0} has been removed.".format(name))
            print("\nName not found!")
            Menu()
            
        Menu()()
    Recipients()
def Send():
    #
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Scoring System Data'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    #CREATING THE ZIP
    
    
    files_temp = ["Individual_Names.txt","Individual_Scores.txt",
             "Team_Names.txt","Event_Names (Individuals).txt",
             "Event_Teams.pkl","Individuals_Scores.pkl","Team_Scores.pkl",
                  "Event_Names (Team).txt"]
            #STILL NEED TO ADD THE OTHER FILES THAT DEPEND ON OTHER STUFF
    Files = []
    temp_files = ["Event_Names (Individuals).txt",
                  "Event_Teams.txt"] #ADD FILES HERE
    Open_Files = []
    #THIS IS THE FINAL LIST OF FILES
    #CHECKS IF EACH ONE EXISTS
    for file in files_temp:
        if os.path.exists(file):
            Files.append(file)
            for temp in temp_files:
                #CHECKS IF ITS ONE OF THOSE
                if temp == file:
                    Open_Files.append(file)

    #ADDING THE TEAM NAMES FILES
    if os.path.exists("Team_Names.txt"):
        A = open("Team_Names.txt", "r")
        lines = A.readlines()
        A.close()
        Team_Names = [s.replace('\n', '') for s in lines]
        for team_name in Team_Names:
            Files.append("Team_{0}.txt".format(team_name))

        
    Variable_Files = []
    for file in Open_Files:
        OPEN = open(file,"r")
        lines = OPEN.readlines()
        OPEN.close()
        File_Names = [s.replace('\n', '') for s in lines]
        if file == "Event_Names (Individuals).txt":
            for name in File_Names:
                Files.append("Event_Individuals_{0}.pkl".format(name))
        elif file == "Event_Teams.pkl":
            for name in File_Names:
                Files.append("Event_Team_{0}.pkl".format(name))

    #CREATING READ ME FILE
    readme = open("ReadMe.txt","w")
    readme.write("===== Scoring System Created By Keval Deepak =====\n\nTo install data back into the program:\n[1] Extract all files from the .zip (Look Below)\n[2] Put all files in the directory of the program\n[3] Start the program.\n\nWarning : Do NOT change any names of any files.\n\nTo extract files from the .zip file: \n[1] Download one to extract: \n    [1] Winrar - \n    - https://www.rarlab.com/download.htm\n    [2] 7Zip - \n    - http://www.7-zip.org/download.html\n[2] Right Click .zip file and click 'Extract Here'\n\nCreated by Keval Deepak")
    readme.close() 

    #CREATING THE ZIP FILE
    file_name = "Data.zip"
    zip_archive = ZipFile(file_name,"w")
    for item in Files:
        zip_archive.write(item)
    zip_archive.close()
        
    # List of attachments
    attachments = ['Data.zip','ReadMe.txt']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("\nEmail sent!")
        #AFTER IT IS SENT
        #IT SHOULD DELETE THE .ZIP FILE AND THE README
        os.remove("ReadMe.txt")
        os.remove("Data.zip")
        #THEN IT SHOULD EXIT
        print("Goodbye!")
        time.sleep(1)
        exit()
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise
    #

main()
