# ---------------------- _____IMPORTS____ ---------------------- 
import time
import re
import os
import pickle
    
# ------- LISTS & DICTIONARIES ----------
# ----- Individuals list. Name -----
Individuals_List = []
# ----- Teams Dict. Name : Players -----
Teams = {}
# ----- Teams List. Name -----
# MAX 4 Teams
#THIS CONTAINS NAMES OF ALL TEAM NAMENAMES
Teams_List = []
#---- EVENTS ----
#---- INDIVIDUALS -- EVENTS ----
Events_Individuals = {}
# ------   EVENTS DICT. -------
Events_Teams = {}
# ------   SCORES DICT. {Placement:Points Awarded} -------
Ranking = {
        1:5,
        2:4,
        3:3,
        4:2,
        5:1,
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        12:0,
        13:0,
        14:0,
        15:0,
        16:0,
        17:0,
        18:0,
        19:0,
        20:0,
    }
# ----- Individuals Dict. Name : Score -----
Individuals = {}
# ----- Teams Dict. Team_Name : [{Player_Name:Score}] -----
Team_Scores = {}

#    ------------------- THIS IS THE INTRODUCTION ---------------------
#    -------------------- CHANGE TO WHATEVER THE FIRST MESSAGE IS THAT WILL POPUP -----------------
def Introduction():
    #THIS IS JUST AN INTRODUCTION
    print("Welcome to Jimesh's World\n") #\\\\\CHANGE THIS LATER/////#
    print("Note!:\n      Players in Individuals cannot be entered into a team. \n      Enter players for a team from team's menu\n")
    PasteValues()

def PasteValues():
    global Restart
    global num_lines
    #THIS IS WHERE IT LOADS UP ALL THE VALUES FROM THE FILES
    # --------- INDIVIDUALS NAME FILE -------------
    #THIS CREATES A NEW FILE IF THERE ISN'T ONE ALREADY
    #TO PREVENT A ERROR THAT THERE IS NO DIRECTORY
    file = open("Individual_Names.txt","a+")
    
    file.close()

    #THIS WILL READ THE FILE
    file = open("Individual_Names.txt","r")

    #VARIABLE 'lines' WILL BE A LIST THAT HAS ALL NAMES AS DIFFERENT VALUES
    lines = file.readlines()
    #THIS COUNTS THE AMOUNT OF LINES THAT THERE ARE
    num_lines = sum(1 for line in open('Individual_Names.txt'))
    #THIS STRIPS THE '\n' FROM THE VALUES IN THE LIST
    BLines = [s.replace('\n', '') for s in lines]
    x = 0
    #THIS CYCLES THROUGH ADDING EACH NAME INTO THE LISTS AND DICTIONARIES 
    for abc in range(0,num_lines):
        #ADDING TO THE LIST
        Individuals_List.append(BLines[x])
        x += 1
    file.close()
    # --------- INDIVIDUALS SCORES FILE -------------
    #THIS CREATES A NEW FILE IF THERE ISN'T ONE ALREADY
    #TO PREVENT A ERROR THAT THERE IS NO DIRECTORY
    file = open("Individual_Scores.txt","a+")

    file.close()
    #THIS CYCLES THROUGH ADDING EACH NAME INTO THE LISTS AND DICTIONARIES 
    file = open("Individual_Scores.txt","r")

    lines2 = file.readlines()

    BLines2 = [s.replace('\n', '') for s in lines2]
    x = 0
    for bad in range(0,num_lines):
        #ADDING TO DICT.
        Part_score = re.findall(r'\b\d+\b',BLines2[x])
        Individuals[BLines[x]] = Part_score[0] #IM NOT TOO SURE WHY THIS IS '0'
        x += 1
    file.close()
    # --------- TEAMS SCORES FILE -------------
    #THIS CREATES A NEW FILE IF THERE ISN'T ONE ALREADY
    #TO PREVENT A ERROR THAT THERE IS NO DIRECTORY
    file = open("Team_Names.txt","a+")

    file.close()

    file = open("Team_Names.txt","r")
    
    num_lines = sum(1 for line in open('Team_Names.txt'))
    lines3 = file.readlines()
    
    BLines3 = [s.replace('\n', '') for s in lines3]
    # ------ THIS IS ALL THE IMPORT TEAM NAMES -------
    x = 0
    for gjg in range(0,num_lines):
        file_team_name = BLines3[x]
        #ADDING IT BACK TO THE LIST
        Teams_List.append(file_team_name)
        #ADDING BACK TO DICT.
        Teams[file_team_name] = ""   
        x += 1
    # ------ THIS IS TO IMPORT TEAM MEMBERS ------- ||||||  DO THIS AFTER ||||||
    #IMPORTING TEAMS
    team_name_file = open("Team_Names.txt","a+")
    team_name_file.close()
    team_name_file = open("Team_Names.txt","r")
    lines = team_name_file.readlines()
    team_name_file.close()

    #THESE ARE ALL THE TEAM NAMES
    Team_Names = [s.replace('\n', '') for s in lines]

    for team_name in Team_Names:
        team_file = open("Team_{0}.txt".format(team_name),"a+")
        team_file.close()
        team_file = open("Team_{0}.txt".format(team_name),"r")
        lines = team_file.readlines()
        team_file.close()

        #THESE ARE ALL THE PLAYER NAMES
        Player_Names = [s.replace('\n', '') for s in lines]

        #ADDS TO THE DICT WITH ALL THE TEAMS
        #CREATES THE ENTRY IN THE DICT, IF NOT ALREADY THERE
        Teams[team_name] = []
        #CYCLES THROUGH ALL PLAYERS AND ADDS THEM
        for player_name in Player_Names:
            Teams[team_name].append(player_name)
    #------------------------------- IMPORTING EVENTS ------------------------
    # ---- INDIVIDUALS - EVENTS ----------------------
    #IMPORTING EVENTS FOR INDIVIDUALS
    file = open("Event_Names (Individuals).txt","a+")
    file.close()
    file = open("Event_Names (Individuals).txt","r")
    lines = file.readlines()
    file.close()
    
    Event_Names = [s.replace('\n', '') for s in lines]
    
    for event_name in Event_Names:
        Events_Individuals[event_name] = []
        
    #IMPORTING FROM PKL
    for key in Events_Individuals:
        lenght = os.stat('Event_Individuals_{0}.pkl'.format(key)).st_size == 0
        if lenght == False:
            with open("Event_Individuals_{0}.pkl".format(key), "rb") as f:
                ABCD = pickle.load(f)
                for event in ABCD:
                    Events_Individuals[key].append(event)
    # ----------------- TEAMS - EVENTS ----------------------
    event_names_file = open("Event_Names (Team).txt","a+")
    event_names_file.close()
    event_names_file = open("Event_Names (Team).txt","r")
    lines = event_names_file.readlines()
    event_names_file.close()

    Event_Names = [s.replace('\n', '') for s in lines]
    for event_name in Event_Names:
        event_file = open("Event_Team_{0}.txt".format(event_name),"a+")
        event_file.close()
        event_file = open("Event_Team_{0}.txt".format(event_name),"r")
        lines = event_file.readlines()
        event_file.close()

        Players = [s.replace('\n', '') for s in lines]
        Events_Teams[event_name] = []
        for player in Players:
            #CREATES AN ENTRY FOR THE EVENT FIRST, IF THERE WASN'T ONE BEFORE
            
            Events_Teams[event_name].append(player)
    #ADDING THE EVENT INFORMATION AS WELL
    #IMPORTING FROM THE PKL FILE
    for key in Events_Teams:
        lenght = os.stat('Event_Team_{0}.pkl'.format(key)).st_size == 0
        if lenght == False:
            with open("Event_Team_{0}.pkl".format(key), "rb") as f:
                new_DICT = pickle.load(f)
                Events_Teams[key] = new_DICT

    # ------ IMPORTING EVENTS ---------


    # ---------- IMPORTING SCORES ----------
    lenght = True
    if os.path.exists('Team_Scores.pkl'):
        lenght = os.stat('Team_Scores.pkl').st_size == 0
    if lenght == False:
        with open("Team_Scores.pkl", "rb") as f:
            POP = pickle.load(f)
            global Team_Scores
            Team_Scores = POP
            
            
    Main_Menu()

#THIS IS THE FUNCTION THAT WILL RESET ALL MY STORED DATA
def Reset():
    #THIS IS A LIST OF ALL THE NAMES OF FILES
    Static_Files = ["Team_Names.txt","Individual_Scores.txt","Individual_Names.txt","Event_Names (Team).txt","Event_Names (Individuals).txt","Team_Scores.pkl"]
    #THIS IS A LIST OF ALL NAMES TO DELETE
    Remove_Files = []
    
    for File_Name in Static_Files:
        #CHECKS IF THE FILE PATH IS REAL
        temp = os.path.exists(File_Name)
        #IF IT IS, IT WILL APPEND INTO NEW TEMP LIST
        if temp == True:
            Remove_Files.append(File_Name)

    #THEN DELETES ALL THE FILES THAT ARE ACTUALLY THERE
    for File_Name in Remove_Files:
        os.remove(File_Name)
    #DELETES ALL THE TEAMS FILES
    for name in Teams_List:
        os.remove("Team_{0}.txt".format(name))
    #DELETES ALL THE EVENTS FILES -- Teams
    for key in Events_Teams:
        os.remove("Event_Team_{0}.pkl".format(key))
    #DELETES ALL THE EVENTS FILES -- Individuals
    for key in Events_Individuals:
        os.remove("Event_Individuals_{0}.pkl".format(key))
    
    #RESTARTS THE PROGRAM ~ PYTHON FILE NAME
        #CHANGE THIS DEPENDING ON WHETHER THIS IS THE exe OR py
    #os.startfile("Launcher.exe") #open the laucher.exe
    os.startfile("LAUNCHER.EXE") #open the laucher.py


#   ------------------- THIS IS THE MAIN MENU. USER DECIDES WHICH SUB MENU TO NAVIGATE TO. --------------------
def Main_Menu():
    try:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
        print("-------- Main Menu --------")
        # INPUT WITH ALL THE OPTIONS LISTED. NUMBER REPRESENTS THE OPTION
        M_M = int(input("1 - Individuals\n2 - Teams\n3 - Events\n4 - Scores\n5 - Reset all Data\n6 - Final Scores\n7 - Exit\nWhere do you want to go?: "))
        # IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN.
        #Individual MENU
        if M_M == 1:
            Individuals_Menu()
        #TEAMS MENU
        elif M_M == 2:
            Teams_Menu()
        #EVENTS MENU
        elif M_M == 3:
            Events_Menu()
        #SCORES MENU
        elif M_M == 4:
            Scores_Menu()
        #RESET ALL SCORES
        elif M_M == 5:
            Reset()
        #FINAL SCORES
        elif M_M == 6:
            Final_Score_Menu()
        #EXITING
        elif M_M == 7:
            print("GoodBye!")
            time.sleep(1)
            exit()
        #ANYTHING ELSE
        else:
            print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------\n")
            Main_Menu()
    #WHAT IF THE PERSON DOESN'T TYPE ANYTHING. 
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------\n")
        Main_Menu()
#   ---------- THIS IS THE PARTICIPANTS MENU. EVERYTHING RELATING TO PARTICIPANTS IS HERE -----------
def Individuals_Menu():
    try:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
        print("\n-------- Individual's Menu --------")
        # INPUT WITH ALL THE OPTIONS LISTED. NUMBER REPRESENTS THE OPTION
        P_M = int(input("1 - Review Individuals\n2 - Add Individuals\n3 - Remove Individuals\n4 - Back\nWhere do you want to go?: "))
        # IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN.
        #REVIEW PARTICIPANTS
        if P_M == 1:
            Individuals_Menu_1()
        #ADD PARTICIPANTS
        elif P_M == 2:
            if len(Individuals_List) == 20:
                print("\n--- Error ---")
                print("There are too many players! Max. 20 players")
                Individuals_Menu()
            else:
                Individuals_Menu_2()
        #REMOVE PARTICIPANTS
        elif P_M == 3:
            Individuals_Menu_3()
        #BACK TO MAIN MENU
        elif P_M == 4:
            Main_Menu()
        #ANYTHING ELSE
        else:
            print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
            Individuals_Menu()
    #WHAT IF THE PERSON DOESN'T TYPE ANYTHING. 
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Individuals_Menu()
        
#THIS IS REVIEWING ALL THE INDIVIDUALS
def Individuals_Menu_1():
    # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
    print("")
    # THIS CHECKS THE LENGHT OF THE LIST --- TO CHECK IF IT IS EMPTY
    lenght = len(Individuals_List)
    #IF IT IS EMPTY, THIS SHOULD HAPPEN
    if lenght == 0:
        print("There are no players!")
    #IF IT HAS PLAYERS IT WILL PRINT THEM OUT
    else:
        print("---------- Players ----------")
        for abc in Individuals_List:
            print("---> " + abc + " <---")
    #RETURNING TO INDIVIDUAL MENU MACHANISM    
    Individuals_Menu()
    
#THIS IS ADDING A INDIVIDUAL
def Individuals_Menu_2():
    try:
        global Add_Individual
        Add_Individual = input("\nPlease enter a full name: ").title()
        #VALIDATION 1 : IF THERE ARE ANY NUMBERS
        if any(i.isdigit() for i in Add_Individual):
            print("\n---------- Error! ----------\nPlease enter a name without numbers!\n----------------------------")
            Individuals_Menu()
        #VALIDATION 2 : IF THERE IS NO NAME
        elif Add_Individual == "":
            print("\n---------- Error! ----------\nPlease enter a name!\n----------------------------")
            Individuals_Menu()
        #VALIDATION 3 : IF THE PERSON HASN'T ENTERED A FULL NAME
        elif " " not in Add_Individual:
            print("\n---------- Error! ----------\nPlease enter your First & Last name!\n----------------------------")
            Individuals_Menu()
        #VALIDATION 5 : IF THE NAME HAS BEEN ENTERED INTO A TEAM ALREADY
        for key in Teams:
            temp = Add_Individual in Teams[key]
            if temp == True:
                print("\nError!")
                print("{0} has been entered in a team {1}".format(Add_Individual,key))
                Individuals_Menu()
        #TITLES() THE VARIABLE
        Add_Individual = Add_Individual.title()
        #VALIDATION 4 : IF THE NAME IS ALREADY TAKEN
        for ghg in Individuals_List:
            if Add_Individual == ghg:
                print("\n---------- Error! ----------\n   Name is already taken!\n----------------------------")
                Individuals_Menu()
        #IF NAME IS OKAY AFTER VALIDATION THEN THIS WILL BE EXECUTED
        else:
            #ADDING TO LIST
            Individuals_List.append(Add_Individual)
            #ADDING TO DICTIONARY
            Individuals[Add_Individual] = 0
            #SAVES THE NAMES ONTO A FILE USING A DIFFERENT FUNCTION
            Individual_Save()
            #PRESENTS A MESSAGE FOR THE USER
            print("\nIndividual has been added!")
            #RETURNS BACK TO THE MAIN MENU
            Individuals_Menu()
    #WHAT IF THE PERSON DOESN'T TYPE ANYTHING. 
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Individuals_Menu_2()

#THIS IS TO REMOVE A INDIVIDUAL
def Individuals_Menu_3():
    try:
        #PRINTS ALL THE INDIVIDUAL'S NAMES
        print("---------- Players ----------")
        for abc in Individuals_List:
            print("---> " + abc + " <---")
        temp = input("Who do you want to remove?: ")
        temp = temp.title()
        #THIS IS SO THAT IT CYCLES THROUGH THE WHOLE LIST CHECKING IF THE NAME IS SAME
        for abc in Individuals_List:
            #WHAT SHOULD HAPPEN IF THE NAME IS FOUND INSIDE THE LIST
            if temp == abc:
                #REMOVES NAME FROM LIST
                Individuals_List.remove(temp)
                #REMOVES NAME FROM THE DICTIONARY
                del Individuals[temp]
                #REMOVES NAME FROM FILE \\\\Individual_Names.TXT////
                f = open("Individual_Names.txt","r")
                lines = f.readlines()
                f.close()
                f = open("Individual_Names.txt","w")
                for line in lines:
                  if line != temp + "\n":
                    f.write(line)
                f.close()
                #REMOVES NAME FROM FILE \\\Individual_Scores.TXT////
                f = open("Individual_Scores.txt","r")
                lines = f.readlines()
                f.close()
                f = open("Individual_Scores.txt","w")
                for line in lines:
                    if line.startswith(temp):
                        asdas = 1 + 1
                    else:
                        f.write(line)
                f.close()
                #TELLS THE USER THAT IT HAS HAPPENED SUCCESSFULLY
                print("\nIndividual has been removed!")
                #RETURNS BACK TO THE INDIVIDUAL MENU
                Individuals_Menu()
            #WHAT SHOULD HAPPEN IF THE NAME IS NOT FOUND INSIDE THE LIST (SEE COMMENT BELOW)
            else:
                tempx = 1 + 1
        if temp == "":
            print("\n---------- Error! ----------\n----Please enter a name.----\n----------------------------")
            Individuals_Menu()
        #THIS IS ACTUALLY WHAT HAPPENS AS IT ALLOWS THE PROGRAM TO CHECK ALL THE NAMES WITHIN THE LIST
        #ERROR MESSAGE FOR THE USER 
        print("\n---------- Error! ----------\n" + temp + " is not a valid player.\n----------------------------")
        #RETURNS BACK TO THE INDIVIDUAL MENU
        Individuals_Menu()
        
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Individuals_Menu()

#   ---------- THIS IS THE SAVING THE INDIVIDUAL'S NAMES. -----------
def Individual_Save():
    file = open("Individual_Names.txt","a+")
    
    file.write(Add_Individual + "\n")  
    
    file.close()

    file = open("Individual_Scores.txt","a+")

    file.write(Add_Individual + " ---> " + str(Individuals[Add_Individual]) + "\n")
    
    file.close()
    return
#   ---------- THIS IS THE TEAMS MENU. EVERYTHING RELATING TO TEAMS IS HERE -----------
def Teams_Menu():
    try:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES
        print("\n-------- Teams's Menu --------")
        # INPUT WITH ALL THE OPTIONS LISTED. NUMBER REPRESENTS THE OPTION
        T_M = int(input("1 - Review Teams\n2 - Add Teams\n3 - Remove Teams\n4 - Add Players to teams\n5 - Remove Players from teams\n6 - Back\nWhere do you want to go?: "))
        # IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN.
        #REVIEW TEAMS
        if T_M == 1:
            #IF THERE ARE NO TEAMS
            if len(Teams) == 0:
                print("\nThere are no Teams!")
                Teams_Menu()
            #IF THERE ARE TEAMS
            else:
                Teams_Menu_1()
        #ADD TEAMS
        elif T_M == 2:
            lenght_Teams_List = len(Teams_List)
            if lenght_Teams_List <= 3:                
                Teams_Menu_2()
            else:
                print("\n    ----- Error -----")
                print("There are too many teams! (Max 4 Teams)")
                Teams_Menu()
        #REMOVE TEAMS
        elif T_M == 3:
            Teams_Menu_3()
        #ADDING PLAYERS TO TEAMS
        elif T_M == 4:
            Teams_Menu_4()
        #REMOVE PLAYERS FROM TEAMS #STILL NEED TO DO THIS
        elif T_M == 5:
            Teams_Menu_5()
        #BACK TO MAIN MENU
        elif T_M == 6:
            Main_Menu()
        #ANYTHING ELSE
        else:
            print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
            Teams_Menu()
    #WHAT IF THE PERSON DOESN'T TYPE ANYTHING. 
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Teams_Menu()
        
#THIS IS TO REVIEW ALL THE TEAMS /////////// THIS CAN BE DIFFERENT, TO BE ABLE TO VIEW MEMEBRS \\\\\\\\\\\\\\\\
def Teams_Menu_1():
    print("")
    temphgh = int(input("1 - View players by team\n2 - View all Teams\n3 - Back\nWhere do you want to go?: "))
    #VIEWING PLAYERS BY A SPECIFIC TEAM
    if temphgh == 1:
        print("")
        print("--- Teams ---")
        for key in Teams:
            print("--> {0} <--".format(key))
        Team = input("Enter a team name to view: ").title()
        #VALIDATION : IF THE NAME IS CORRECT
        for name in Teams:
            if name == Team:
                #THIS WILL HAPPEN IF CORRECT
                print('')
                x = 1
                for player in Teams[Team]:
                    print('Player {0} --> {1}'.format(x,player))
                    x += 1

                #RESETS VARIABLE ONCE DONE LOOPING
                x = 1
                #RETURNS BACK TO THE MENU
                Teams_Menu()
        #IF THE NAME IS NOT FOUND
        print("Team is not found!")
        #RETURNS BACK TO THE MENU
        Teams_Menu()
    #VIEWING ALL TEAMS
    elif temphgh == 2:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES
        print("")
        # THIS CHECK THE LENGHT OF THE LIGHT --- TO CHECK IF IT IS EMPTY
        lenght = len(Teams_List)
        #IF IT IS EMPTY, THIS SHOULD HAPPEN
        if lenght == 0:
            print("There are no Teams!")
        #IF IT HAS TEAMS IT WILL PRINT THEM OUT
        else:
            print("---------- TEAMS ----------")
            for abc in Teams_List:
                print("---> " + abc + " <---")
        #RETURNING TO INDIVIDUAL MENU MACHANISM    
        Teams_Menu()
    #BACK
    elif temphgh == 3:
        Teams_Menu()
    else:
        print("Please enter a valid option.")
    Teams_Menu()
    
#THIS IS TO ADD TEAMS
def Teams_Menu_2():
    try:
        team_name = input("Enter a name for the new team: ")
        team_name = team_name.title()
        
        #VALIDATION 1 : IF THERE ARE ANY NUMBERS
        if any(i.isdigit() for i in team_name):
            print("\n---------- Error! ----------\nPlease enter a name without numbers!\n----------------------------")
            Teams_Menu()
        #VALIDATION 2 : IF THERE IS NO NAME
        elif team_name == "":
            print("\n---------- Error! ----------\nPlease enter a name!\n----------------------------")
            Teams_Menu()
        #VALIDATION 4 : RESERVED NAMES 
        elif team_name == "Individual_Names" or team_name == "Individual_Scores" or team_name == "Team_Names":
            print("\nYou have entered a reserved name for the system.")
            print("You may not have access to name a team this.")
            Teams_Menu()
        #VALIDATION 3 : IF THERE IS THE SAME NAME PRESENT IT DOES THIS
        for ghg in Teams_List:
            if team_name == ghg:
                print("\n---------- Error! ----------\n   Name is already taken!\n----------------------------")
                Teams_Menu()
        #IF NAME IS OKAY AFTER VALIDATION THEN THIS WILL BE EXECUTED
        else:
            #ADDING TO LIST (Teams_List)
            Teams_List.append(team_name)
            #ADDING TO DICT. Team : Team_List
            Teams[team_name] = []
            #ADDING TO DICT.
            #CREATES A KEY WITH A LIST
            Team_Scores[team_name] = []
            #THIS CREATES A FILE USING THE TEAM NAME
            team_file = open('Team_%s.txt' % team_name, 'a+') #over here
            team_file.close()
            #THIS CREATES A FILE FOR ALL THE TEAM NAMES
            teams_file = open("Team_Names.txt","a+")
            #THIS WRITES THE TEAM NAME INSIDE THE FILE
            teams_file.write(team_name + "\n")
            teams_file.close()
            #PRINTS CONFIRMATION FOR THE USER TO KNOW
            print("\nTeam has been added!")
            #REDIRECTS BACK TO THE MENU
            Teams_Menu()
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Teams_Menu()

#THIS IS TO REMOVE TEAMS
def Teams_Menu_3():
    try:
        for abc in Teams_List:
            print("---> " + abc + " <---")
        remove_team = input("Enter a team name to remove: ")
        #VALIDATION 1 : IF THERE ARE ANY NUMBERS
        if any(i.isdigit() for i in remove_team):
            print("\n---------- Error! ----------\nPlease enter a name without numbers!\n----------------------------")
            Teams_Menu()
        remove_team = remove_team.title()
        #VALIDATION 2 : IF THERE IS NO NAME
        if remove_team == "":
            print("\n---------- Error! ----------\nPlease enter a name!\n----------------------------")
            Teams_Menu()
        #IF EVERYTHING IS ALRIGHT THIS WILL HAPPEN
        for ghg in Teams_List:
            if remove_team == ghg:
                #REMOVES FROM THE LIST
                Teams_List.remove(remove_team)
                #REMOVES FROM THE DICTIONARY
                del Teams[remove_team]
                #REMOVE FROM THE DICT.
                if remove_team in Team_Scores:
                    del Team_Scores[remove_team]
                #DELETES THE TEAM FILE
                os.remove("Team_{0}.txt".format(remove_team))
                #DELETES FROM THE EVENT DICT.
                for key in Events_Teams:
                    for x in range(0,len(Events_Teams[key])):
                        if remove_team in Events_Teams[key][x]:
                            #GOOD ~ DO THIS
                            #REMOVES THE TEAM FROM THE EVENTS DICT
                            #del Events_Teams[key][0][remove_team]
                            #REMOVES THE WHOLE LIST ENTRY
                            del Events_Teams[key][x]
                #DELETES NAME FROM THE Team_Names.txt FILE
                team_file = open("Team_Names.txt","r")
                team_file_lines = team_file.readlines()
                team_file.close()
                team_file = open("Team_Names.txt","w")
                for line in team_file_lines:
                    if line.startswith(remove_team):
                        asdas = 1 + 1
                    else:
                        team_file.write(line)
                team_file.close()
                #PRINTS A MESSAGE FOR THE USER
                print("\nTeam '" + remove_team + "' has been removed!")
                Teams_Menu()
        #IF THE NAME WASN'T FOUND IN LIST
        print("\n---------- Error! ----------\n   There is no such team!\n----------------------------")
        Teams_Menu()
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Teams_Menu()

#THIS IS TO ADD PLAYERS TO TEAMS
def Teams_Menu_4():
    try:
        print("")
        for lol in Teams_List:
            print("---> " + lol + " <---")
        Team_Selected = input("First Select a team! : ").title()
        #VALIDATION 1: IF THE NAME IS ON THE LIST
        if Team_Selected in Teams_List:
            print("\n--- " + Team_Selected + " has been selected! ---")
            #BELOW IS THE CODE FOR ADDING A TEAM MATE
            Player_Name = input("Enter a Player's FULL NAME for team " + Team_Selected + " : ").title()
            temp = Player_Name in Individuals
            #IF NAME IS REGISTERED WITH INDIVIDUALS PARTICIPANTS
            if Player_Name in Individuals_List:
                print("\n{0} is registered with individuals.".format(Player_Name))
            #VALIDATION : NAME MUST BE A FULL NAME
            elif " " not in Player_Name:
                print("\nPlease enter a FULL name.")
                Teams_Menu()
            elif temp == True:
                print("{0} has already been entered to Individuals".format(Player_Name))
            else:
                #ADDING PLAYER TO TEAM FILE
                Team_File = open("Team_{0}.txt".format(Team_Selected),"a+")#over here
                Team_File.write(Player_Name + "\n")
                Team_File.close()
                #ADDING PLAYER TO TEAM DICT.
                Teams[Team_Selected].append(Player_Name)
                #SHOWS A MESSAGE FOR THE USER
                print("\n{0} has been added to Team {1}".format(Player_Name,Team_Selected))
                Teams_Menu()
            Teams_Menu()  
        #VALIDATION 1: IF THE NAME IS NOT ON THE LIST
        else:
            print("Please enter a correct name!")
            print("Returning to Team's Menu.")
            time.sleep(1)
            Teams_Menu()
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Teams_Menu()

#THIS IT TO REMOVE PLAYERS FROM TEAMS
def Teams_Menu_5():
    try:
        print("")
        for lol in Teams_List:
            print("---> " + lol + " <---")
        Team_Selected = input("First Select a team! : ").title()
        #VALIDATION 1: IF THE NAME IS ON THE LIST
        if Team_Selected in Teams_List:
            print("\n--- " + Team_Selected + " has been selected! ---")
            #BELOW IS THE CODE FOR ADDING A TEAM MATE
            Player_Name = input("Enter a Player's FULL NAME for team " + Team_Selected + " : ").title()
            #VALIDATION 1 : CHECKS IF IT IS A ACTUAL PLAYER
            Player_File = open("Team_{0}.txt".format(Team_Selected),"r")
            lines = Player_File.readlines()
            Player_File.close()

            Player_Names = [s.replace('\n', '') for s in lines]

            #CHECKS ALL NAMES AND SEES IF IT IS THERE
            if Player_Name in Player_Names:
                #GOOD
                #DELETES PLAYER FROM TEAM FILE
                Team_File = open("Team_{0}.txt".format(Team_Selected),"w")
                for name in Player_Names:
                    if name != Player_Name:
                        Team_File.write(name + "\n")
                Team_File.close()
                #DELETS PLAYER FROM TEAM DICT
                Teams[Team_Selected].remove(Player_Name)
                #SHOWS A MESSAGE TO THE USER
                print("\n{0} has been removed from Team {1}".format(Player_Name,Team_Selected))
                #RETURNS BACK TO MENU
                Teams_Menu()
            else:
                print("\n{0} not found.".format(Player_Name))
                Teams_Menu()
            

        #VALIDATION 1: IF THE NAME IS NOT ON THE LIST
        else:
            print("Please enter a correct name!")
            print("Returning to Team's Menu.")
            time.sleep(1)
            Teams_Menu()
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------")
        Teams_Menu()
    
#   ---------- THIS IS THE EVENTS MENU. EVERYTHING RELATING TO EVENTS IS HERE -----------
def Events_Menu():
    # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
    print("\n-------- Events Menu --------")
    # INPUT WITH ALL THE OPTIONS LISTED. NUMBER REPRESENTS THE OPTION
    E_M = int(input("1 - Events for Individuals\n2 - Events for Teams\n3 - Back\nWhere do you want to go?: "))
    #IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN
    #INDIVIDUALS
    if E_M == 1:
        Events_Menu_1()
    #TEAMS
    elif E_M == 2:
        Events_Menu_2()
    #BACK
    elif E_M == 3:
        Main_Menu()
    #ANYTHING ELSE
    else:
        print("\nPlease enter a valid option.")
        Events_Menu()

#INDIVIDUALS --- EVENTS -----
def Events_Menu_1():
    try:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
        print("\n-------- EVENTS (INDIVIDUALS) --------")
        E_M_i = int(input("1 - Review Events\n2 - Add Events\n3 - Remove Events\n4 - Add Individuals to Events\n5 - Remove Individuals to Events\n6 - Back\nWhere do you want to go?: "))
        #IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN.
        #REVIEW EVENTS
        if E_M_i == 1:
            #IF THERE ARE NO EVENTS
                if len(Events_Individuals) == 0:
                    print("\nThere are no Events for Individuals!")
                    Events_Menu_1()
            #IF THERE ARE EVENTS
                else:
                    Events_Menu_1_1()
        #ADD EVENTS
        elif E_M_i == 2:
            Events_Menu_1_2()
        #REMOVE EVENTS
        elif E_M_i == 3:
            Events_Menu_1_3()
        #ADD INDIVIDUALS TO EVENTS
        elif E_M_i == 4:
            Events_Menu_1_4()
        #REMOVE INDIVIDUALS TO EVENTS
        elif E_M_i == 5:
            Events_Menu_1_5()
        #BACK
        elif E_M_i == 6:
            Events_Menu()
        #IF THE USER TYPES SOMETHING ELSE
        else:
            print("Please enter a valid option.")
            Events_Menu_1()
    #WHAT IF THE PERSON DOESN'T TYPE ANYTHING. 
    except ValueError:
        print("\n---------- Error! ----------\nPlease enter a valid answer!\n----------------------------\n")
        Events_Menu_1()

# ----- SUB SECTIONS --- EVENTS ---- INDIVIDUALS
#REVIEW EVENTS
def Events_Menu_1_1():
    print("\n----- Events for Individuals -----")
    for key in Events_Individuals:
        print("      --- {0} ---".format(key))
        x = 1
        for player in Events_Individuals[key]:
            print("Player {0} --> {1}".format(x,player))
            x += 1
        x = 1
    time.sleep(1)
    Events_Menu_1()

#ADD EVENTS
def Events_Menu_1_2():
    print("\n ---- Add Events (Individuals) ----")
    Event_Name = input("Enter a event name: ").title()
    #VALIDATION 1 : IF THERE IS NO NAME
    if Event_Name == "":
        print("\nPlease enter a name!")
        Events_Menu_1()
    #VALIDATION 2: IF THERE ARE ANY NUMBERS
    elif any(i.isdigit() for i in Event_Name):
        print("\nEnter a name without numbers!")
        Events_Menu_1()
    #VALIDATION 3 : IF THE NAME IS ALREADY TAKEN
    elif Event_Name in Events_Individuals:
        print("\n -- This name is taken -- ")
        Events_Menu_1()
    #IF EVERYTHING IS OKAY, THIS WILL HAPPEN
    else:
        #ADDS TO DICT. (Events_Individuals)
        Events_Individuals[Event_Name] = []
        #CREATES A PKL FILE FOR EACH EVENT
        file = open("Event_Individuals_{0}.pkl".format(Event_Name),"a+")
        file.close()
        #CREATES A TXT FILE FOR ALL THE NAMES
        file = open("Event_Names (Individuals).txt","a+")
        file.write(Event_Name + "\n")
        file.close()
        #GIVES A MESSAGE FOR THE USER
        print("\nEvent has been created!")
        #RETURNS BACK TO MENU
        Events_Menu_1()
        
#REMOVE EVENTS
def Events_Menu_1_3():
    print("\n ---- Remove Events (Individuals) ----")
    for key in Events_Individuals:
        print("-- {0} --".format(key))
    Event_Name = input("Enter a event name: ").title()
    #VALIDATION 1 : IF THERE IS NO NAME
    if Event_Name == "":
        print("Please enter a name!")
        Events_Menu_1()
    #VALIDATION 2: IF THERE ARE ANY NUMBERS
    elif any(i.isdigit() for i in Event_Name):
        print("Enter a name without numbers!")
        Events_Menu_1()
    #VALIDATION 3 : IF THE NAME IS ALREADY TAKEN
    elif Event_Name in Events_Individuals:
        #REMOVE TO DICT. (Events_Individuals)
        del Events_Individuals[Event_Name]
        #DELETES A PKL FILE FOR EACH EVENT
        os.remove("Event_Individuals_{0}.pkl".format(Event_Name))
        #DELETES NAME FROM EVENTS NAMES FILE
        file = open("Event_Names (Individuals).txt","r")
        lines = file.readlines()
        file.close()

        Event_Names = [s.replace('\n', '') for s in lines]

        file = open("Event_Names (Individuals).txt","w")
        for event_name in Event_Names:
            if event_name != Event_Name:
                file.write(event_name + "\n")
        file.close()
        #GIVES A MESSAGE FOR THE USER
        print("\nEvent has been removed!")
        #RETURNS BACK TO MENU
        Events_Menu_1()
        
#ADD INDIVIDUALS TO EVENTS
def Events_Menu_1_4():
    print("\n--- ADDING INDIVIDUAL TO EVENT ---")
    print("\n--- Select Event ---")
    for key in Events_Individuals:
        print("--> {0} <--".format(key))
    Event_Name = input("Select a event: ").title()
    #VALIDATION 1 : IF IT IS A ACTUAL EVENT
    for key in Events_Individuals:
        if key == Event_Name:
            #
            print("\n--- Select Player ---")
            for key in Individuals:
                print("--> {0} <--".format(key))
            Player_Name = input("Select a player: ").title()
            #VALIDATION 1 : IF IT IS A ACTUAL PLAYER
            for key in Individuals:
                if key == Player_Name:
                    #VALIDATION 1 : CHECKS IF THE NAME IS ALREADY IN THE EVENT
                    for name in Events_Individuals[Event_Name]:
                        if name == Player_Name:
                            print("{0} is already in Event {1}".format(Player_Name,Event_Name))
                    
                    #IF EVERYTHING IS GOING TO HAPPEN PROPERLY
                    ##
                    #APPENDING TO EVENTS_INDIVIDUALS DICT.
                    Events_Individuals[Event_Name].append(Player_Name)
                    #ADDS TO PKL FILE
                    with open("Event_Individuals_{0}.pkl".format(Event_Name), "wb") as f:
                        pickle.dump(Events_Individuals[Event_Name], f, pickle.HIGHEST_PROTOCOL)
                    ##
                    #GIVES A MESSAGE TO THE USER
                    print("\n{0} has been added to event.".format(Player_Name))
                    #RETURNS BACK TO MENU
                    Events_Menu_1()
            #IF EVENT IS NOT FOUND
            print("\nEvent not found!")
            Events_Menu_1()
            #
    #IF EVENT IS NOT FOUND
    print("\nEvent not found!")
    Events_Menu_1()


#REMOVE INDIVIDUALS TO EVENTS
def Events_Menu_1_5():
    print("\n--- REMOVE INDIVIDUAL TO EVENT ---")
    print("\n--- Select Event ---")
    for key in Events_Individuals:
        print("--> {0} <--".format(key))
    Event_Name = input("Select a event: ").title()
    #VALIDATION 1 : IF IT IS A ACTUAL EVENT
    for key in Events_Individuals:
        if key == Event_Name:
            print("\n--- Select player ---")
            for name in Events_Individuals[Event_Name]:
                print("-> {0} <--".format(name))
            Player_Name = input("Select a player: ").title()
            #VALIDATION 1 : IF IT IS A ACTUAL PLAYER IN THE EVENT
            for name in Events_Individuals[Event_Name]:
                if name == Player_Name:
                    #IF IT IS GOOD THEN THIS WILL HAPPEN
                    #REMOVES FROM LIST IN DICT. EVENTS_INDIVIDUALS
                    Events_Individuals[Event_Name].remove(Player_Name)
                    #ADDS NEW DICT. TO PKL FILE
                    with open("Event_Individuals_{0}.pkl".format(Event_Name), "wb") as f:
                        pickle.dump(Events_Individuals[Event_Name], f, pickle.HIGHEST_PROTOCOL)
                    ##
                    #GIVES A MESSAGE TO THE USER
                    print("{0} has been removed from event {1}.".format(Player_Name,Event_Name))
                    #RETURNS BACK TO MENU
                    Events_Menu_1()
            #IF NAME IS NOT FOUND
            print("Player is not found!")
            Events_Menu_1()

#---------------------------   TEAMS ---------------
def Events_Menu_2():
    # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
    print("\n-------- EVENTS (TEAMS) --------")
    E_M = int(input("1 - Review Events\n2 - Add Events\n3 - Remove Events\n4 - Add Teams to Events\n5 - Remove Teams from Events\n6 - Back\nWhere do you want to go?: "))
    #IF STATEMENTS DECIDE WHICH OPTION IS CHOSEN.
    #REVIEW EVENTS
    if E_M == 1:
        Events_Menu_2_1()
    #ADD EVENTS
    elif E_M == 2:
        if len(Events_Teams.keys()) == 5:
            print("\nToo many events!")
            print("Please remove to add new one.")
            Events_Menu_2()
        Events_Menu_2_2()
    #REMOVE EVENTS
    elif E_M == 3:
        Events_Menu_2_3()
    #ADD TEAMS TO EVENTS
    elif E_M == 4:
        Events_Menu_2_4()
    #REMOVE TEAMS FROM EVENTS
    elif E_M == 5:
        Events_Menu_2_5()
    #BACK
    elif E_M == 6:
        Events_Menu()
    #ANYTHING ELSE
    else:
        print("Please enter a valid option.")
        Events_Menu_2()
    
#REVIEW EVENTS
def Events_Menu_2_1():
    
    print("----- Events for Teams -----")
    for key in Events_Teams:
        print("      --- {0} ---".format(key))
        x = 1
        y = len(Events_Teams[key])
        for xy in range(0,y):
            for team_name in Events_Teams[key][xy]:
                print("Player {0} --> {1} -- Team {2}".format(x,Events_Teams[key][xy][team_name],team_name))
                x += 1
        x = 1

    time.sleep(1)
    Events_Menu_2()
    
#ADD EVENTS
def Events_Menu_2_2():
    print(" ---- Add Events (Teams) ----")
    Event_Name = input("Enter a event name: ").title()
    #VALIDATION 1 : IF THERE IS NO NAME
    if Event_Name == "":
        print("Please enter a name!")
        Events_Menu_2()
    #VALIDATION 2: IF THERE ARE ANY NUMBERS
    elif any(i.isdigit() for i in Event_Name):
        print("Enter a name without numbers!")
        Events_Menu_2()
    #VALIDATION 3 : IF THE NAME IS ALREADY TAKEN
    for key in Events_Teams:
        if key == Event_Name:
            print("\n -- This name is taken -- ")
            Events_Menu_2()
    #IF EVERYTHING IS OKAY  - -  THIS HAPPENS 
    else:
        #SAVES TO FILE EVENT_NAMES
        file = open("Event_Names (Team).txt","a+")
        file.write(Event_Name + "\n")
        file.close()
        #CREATES A FILE NAME FOR EACH EVENT
        #file = open("Event_Team_{0}.txt".format(Event_Name),"a+") #DELETE FILE OVER HERE
        #file.close()
        #CREATES A PKL FILE FOR EACH EVENT
        file = open("Event_Team_{0}.pkl".format(Event_Name),"a+")
        file.close()
        #SAVES INTO EVENTS DICT. AND ADDS IT TO EVENTS_ID DICT.
        #IF EVERYTHING IS GOOD
        Events_Teams[Event_Name] = []
        #MESSAGE FOR USER
        print("\n{0} has been added.".format(Event_Name))
        #GOES BACK TO MENU
        Events_Menu_2()
        
#REMOVE EVENTS
def Events_Menu_2_3():
    print(" ---- Remove Events ----")
    for key in Events_Teams:
        print("-- {0} --".format(key))
    Event_Name = input("Enter a event name: ").title()
    for key in Events_Teams:
        #IF IT IS CORRECT IT SHOULD DO THIS
        if Event_Name == key:
            #REMOVES FROM FILE
            file = open("Event_Names (Team).txt","r")
            lines = file.readlines()
            file.close()
            striped_lines = [s.replace('\n', '') for s in lines]
            file = open("Event_Names (Team).txt","w")
            for line in striped_lines:
                if line != Event_Name:
                    file.write(line + "\n")
            file.close()
            #DELETES FROM EVENT'S DICT.
            del Events_Teams[Event_Name]
            #DELETES FILE FOR SPORT
            #os.remove("Event_Team_{0}.txt".format(Event_Name)) #DELETE FILE HERE
            os.remove("Event_Team_{0}.pkl".format(Event_Name))
            #GIVES A MESSAGE FOR THE USER
            print("\n{0} has been removed.".format(Event_Name))
            #RETURNS BACK TO MENU
            Events_Menu_2()

    #IF NO NAME WAS FOUND THEN ~ ERROR MESSAGE
    print("Event Not Found!")
    Events_Menu_2()

#ADD TEAMS TO EVENTS
def Events_Menu_2_4():
    global loop
    loop = 0
    def team_select():
        print("-- Select Team --")
        for key in Teams:
            print("-- {0} --".format(key))
        Team_Name = input("Enter a team name: ").title()
        #VALIDATION 1 : IF IT IS IN THE LIST ALREADY
        for key in Teams:
            if Team_Name == key:
                #PRINTS OUT ALL PLAYERS FROM THIS TEAM
                file = open("Team_{0}.txt".format(Team_Name),"r") #over here
                lines = file.readlines()
                file.close()
                striped_lines = [s.replace('\n', '') for s in lines]
                print("------ PLAYERS ------")
                for line in striped_lines:
                    print("-- {0} --".format(line))
                
                #ASKS FOR WHICH TEAM MEMBER IS JOINING THE EVENT
                def Player_Select():
                    Player_Name = input("Enter a player name: ").title()
                    for name in Teams[Team_Name]:
                        if name == Player_Name:
                            #NAME IS FOUND
                            #VALIDATION 1: IF THE NAME IS ALREADY IN A EVENT
                            for key in Events_Teams:
                                for x in range(0,len(Events_Teams[key])):
                                    if Team_Name in Events_Teams[key][x]:
                                        if Player_Name == Events_Teams[key][x][Team_Name]:
                                            #NAME IS FOUND
                                            print("\n{0} is already is Event {1}".format(Player_Name,key))
                                            #RETURNS BACK TO MENU
                                            Events_Menu_2()
                                    
                            #IF THE NAME IS NOT FOUND! (GOOD)
                            #VALIDATION 2 : THE TEAM IS ALREADY ENTERED IN THIS EVENT
                            x = len(Events_Teams[Event_Name])
                            for y in range(0,x):
                                for key in Events_Teams[Event_Name][y]:
                                    if Team_Name == key:
                                        print("\nTeam is already registered for this event!")
                                        Events_Menu_2()
                            #IF EVERYTHING IS OKAY, DOES THIS
                            #
                            #OR ELSE THIS CAN HAPPEN
                            #
                            #APPENDS A NEW DICTIONARY INTO THIS DICT.
                            #NEW DICT HAS TEAM NAME : PLAYER NAME
                            Events_Teams[Event_Name].append({Team_Name:Player_Name})
                            #ADDS TO EVENT FILE .pkl
                            with open("Event_Team_{0}.pkl".format(Event_Name), "wb") as f:
                                pickle.dump(Events_Teams[Event_Name], f, pickle.HIGHEST_PROTOCOL)                      
                            #GIVES A MESSAGE FOR THE USER
                            print("\n{0} has been added to the event.".format(Player_Name))
                            #RETURNS BACK TO MENU
                            Events_Menu_2()
                            #            
                    print("------ PLAYERS ------")
                    for line in striped_lines:
                        print("-- {0} --".format(line))
                    print("Name not found!")
                    Player_Select()

                Player_Select()
        #IF THE NAME IS NOT FOUND
        print("\nEvent Not Found!")
        Events_Menu_2()
        
    print("--- ADDING TEAM TO EVENT ---")
    print("Select Event")
    for key in Events_Teams:
        print("-- {0} --".format(key))
    Event_Name = input("Enter a event name: ").title()
    #VALIDATION 1 : IF IT IS IN THE LIST ALREADY
    for key in Events_Teams:
        if Event_Name == key:
            team_select()
    #IF THE NAME IS NOT FOUND!
    print("\nEvent Not Found!")
    Events_Menu_2()

#REMOVE TEAMS FROM EVENTS
def Events_Menu_2_5():
    def team_selection():
        print("\n-- Select Team --")
        for key in Teams:
            print("-- {0} --".format(key))
        Team_Name = input("Enter a team name: ").title()
        #VALIDATION 1 : IF IT IS IN THE LIST ALREADY
        for name in Teams_List:
            if Team_Name == name:
                #IF EVERYTHING IS OKAY, THIS WILL HAPPEN
                #
                #IF EVERYTHING IS CORRECT
                #DELETES FROM EVENTS_TEAMS_EVENT_NAME DICT.
                Range = len(Events_Teams[Event_Name])
                for pop in range(0,Range):
                    for name in Events_Teams[Event_Name][pop]:
                        if name == Team_Name:
                            #GOOD
                            del Events_Teams[Event_Name][0]
                            #ADDS THE NEW UPDATED DICT INTO FILE .PKL
                            with open("Event_Team_{0}.pkl".format(Event_Name), "wb") as f:
                                pickle.dump(Events_Teams[Event_Name], f, pickle.HIGHEST_PROTOCOL)
                            #PRINTS A MESSAGE
                            print("\nTeam (0) has been removed from the event!".format(Team_Name))
                            Events_Menu_2()
                #
    print("\n--- REMOVING TEAM FROM EVENT ---")
    for key in Events_Teams:
        print("-- {0} --".format(key))
    Event_Name = input("Enter a event name: ").title()
    #VALIDATION 1 : IF IT IS IN THE LIST ALREADY
    for key in Events_Teams:
        if Event_Name == key:
            team_selection()
    #IF THE NAME IS NOT FOUND!
    print("\nEvent Not Found!")
    Events_Menu_2()
    
#   ---------- THIS IS THE SCORES MENU. EVERYTHING RELATING TO SCORES IS HERE -----------
def Scores_Menu():
    print("\n---- Scoring System Main Menu ----")
    S_M = int(input("1 - Scoring System for Individuals\n2 - Scoring System for Teams\n3 - Back\nWhere do you want to go?: "))
    #INDIVIDUALS -- SCORING SYSTEM
    if S_M == 1:
        Scores_Menu_1()
    #TEAMS -- SCORING SYSTEM
    elif S_M == 2:
        Scores_Menu_2()
    #BACK
    elif S_M == 3:
        Main_Menu()
    #BACK
    else:
        print("Please enter a valid answer!")
        Scores_Menu()

#THIS IS THE MAIN MENU FOR SCORING SYSTEM -- INIDIVDUALS
def Scores_Menu_1():
    print("\n----- SCORES FOR INDIVIDUALS -----")
    S_M_i = int(input("1 - Review Scores\n2 - Add Scores to Individual\n3 - Reset Score for Individual\n4 - Back\nWhere do you want to go?: "))
    #REVIEW SCORES
    if S_M_i == 1:
        Scores_Menu_1_1()
    #ADD SCORES TO INDIVIDUALS
    elif S_M_i == 2:
        Scores_Menu_1_2()
    #RESET SCORES
    elif S_M_i == 3:
        Scores_Menu_1_3()
    #BACK
    elif S_M_i == 4:
        Scores_Menu()
    #ANYTHING ELSE
    else:
        print("Please enter a valid answer!")
        Scores_Menu_1()

#REVIEW SCORES
def Scores_Menu_1_1():
    print("\n----- Scores For Individuals -----")
    for key in Individuals:
        print("-- {0} --> {1} --".format(key,Individuals[key]))

    Scores_Menu_1()

#ADD SCORES TO INDIVIDUALS
def Scores_Menu_1_2():
    print("\n--- Add Scores for Individuals ---")
    for key in Individuals:
        print("--> {0}".format(key))
    Player_Name = input("Select a player: ").title()
    #VALIDATION 1 : IF NAME IS IN THE DICT.
    for key in Individuals:
        if key == Player_Name:
            #THIS IS GOOD
            #
            print("\n------- Ranking -------")
            print("--> 1st Place --> 5 Points")
            print("--> 2nd Place --> 4 Points")
            print("--> 3rd Place --> 3 Points")
            print("--> 4th Place --> 2 Points")
            print("--> 5th Place --> 1 Points")
            #
            #ADDING ALL THE SCORES FOR EACH EVENT THE PERSON IS ENTERED FOR
            for event in Events_Individuals:
                if Player_Name in Events_Individuals[event]:
                    Placement = int(input("Enter position for {0} in {1}: ".format(Player_Name,event)))
                    #VALIDATION 1 : GIVES A VALID PLACEMENT
                    if Placement <= 20 and Placement >= 1:
                        #
                        #GETS THE SCORE THAT IS ALREADY THERE
                        Score = Individuals[Player_Name]
                        #LOOKS UP SCORE DEPENDING ON PLACEMENT AND ADDS IT TO SCORE
                        Score = int(Score) + int(Ranking[Placement])
                        #ADDS NEW SCORE TO DICT. AGAIN
                        Individuals[Player_Name] = Score
                        #SAVES INTO FILE
                        #OPENS THE FILE IN READ MODE
                        file = open("Individual_Scores.txt","r")
                        #READS THE FILE
                        lines = file.readlines()
                        file.close()
                        #STRIPS THE LINES
                        file_lines = [s.replace('\n', '') for s in lines]
                        #OPEN THE FILE IN WRITE MODE
                        file = open("Individual_Scores.txt","w")
                        for line in file_lines:
                            VAR = line.startswith(Player_Name)
                            if VAR == True:
                                file.write("{0} ---> {1}\n".format(Player_Name,Score))
                            else:
                                file.write(line + "\n")
                        file.close()
                        #GIVES A MESSAGE FOR THE USER
                        print("\n{0} now has {1} points.".format(Player_Name,Score))
                        #RETURNS BACK TO THE MENU
                        Scores_Menu_1()
                        #
                    else:
                        print("Enter a valid placement.")
                        Scores_Menu_1()

            print("\nPlayer is not registered with any events.")
            print("Warning!:\n         Register all players and teams to events \nbefore continuing with Scores.")
            Scores_Menu_1()        
  
    #IF NOT FOUND
    print("Please enter a valid name.")
    Scores_Menu_1()

#RESET SCORES
def Scores_Menu_1_3():
    print("\n--- Reset Scores for Individuals ---")
    for key in Individuals:
        print("--> {0}".format(key))
    Player_Name = input("Select a player: ").title()
    #VALIDATION 1 : IF NAME IS IN THE DICT.
    for key in Individuals:
        if key == Player_Name:
            
            def sure():
                print("\n{0} has {1} points\n".format(Player_Name,Individuals[Player_Name]))
                print("1 - Yes\n2 - No")
                confirm = int(input("Are you sure you want to reset {0}'s score?: "))
                if confirm == 1:
                    #THIS IS WHERE THE MAIN CODE SHOULD BE
                    #CHANGES SCORE BACK TO ZERO IN DICT.
                    Individuals[Player_Name] = 0
                    #CHANGES SCORE BACK TO ZERO IN FILE
                    file = open("Individual_Scores.txt","r")
                    #READS THE FILE
                    lines = file.readlines()
                    file.close()
                    #STRIPS THE LINES
                    file_lines = [s.replace('\n', '') for s in lines]
                    #OPEN THE FILE IN WRITE MODE
                    file = open("Individual_Scores.txt","w")
                    for line in file_lines:
                        VAR = line.startswith(Player_Name)
                        if VAR == True:
                            file.write("{0} ---> 0\n".format(Player_Name))
                        else:
                            file.write(line + "\n")
                    file.close()
                    #MESSAGE FOR THE USER
                    print("\n{0}'s score has been reset.".format(Player_Name))
                    #RETURNS BACK TO MENU
                    Scores_Menu_1()
                elif confirm == 2:
                    print("Returning back to Menu")
                    print("No changes where made.")
                    Scores_Menu_1()
                else:
                    print("Please enter a valid answer!")
                    sure()
             
            sure()            
    #IF NAME IS NOT FOUND
    print("{0} is not found.".format(Player_Name))
    Scores_Menu_1()
    
#THIS IS THE MAIN MENU FOR SCORING SYSTEM -- TEAMS
def Scores_Menu_2():
    print("\n----- SCORES FOR TEAMS -----")
    S_M_t = int(input("1 - Review Scores\n2 - Add Scores to Teams\n3 - Reset Score for Teams\n4 - Back\nWhere do you want to go?: "))
    #REVIEW SCORES
    if S_M_t == 1:
        Scores_Menu_2_1()
    #ADD SCORES TO TEAMS
    elif S_M_t == 2:
        Scores_Menu_2_2()
    #RESET SCORES FOR A TEAM
    elif S_M_t == 3:
        Scores_Menu_2_3()
    #BACK
    elif S_M_t == 4:
        Scores_Menu()
    #ANYTHING ELSE
    else:
        print("Please enter a valid answer!")
        Scores_Menu_2()

#REVIEW SCORES
def Scores_Menu_2_1():
    print("\n----- Scores For Individuals -----")

    for team_name in Team_Scores:
        for x in range(0,len(Team_Scores[team_name])):
            for player_name in Team_Scores[team_name][x]:
                print("-- Team: {0} -- Player: {1} --> Points: {2} --".format(team_name,player_name,Team_Scores[team_name][x][player_name]))
    Scores_Menu_2()

#ADD SCORES TO TEAMS
def Scores_Menu_2_2():
    print("\n--- Add Scores for a Team ---")
    for key in Teams:
        print("--> {0}".format(key))
    Team_Name = input("Select a team: ").title()
    #VALIDATION 1 : IF NAME IS IN THE DICT.
    for key in Teams:
        if key == Team_Name:
            #GOOD
            print("")
            for names in Teams[Team_Name]:
                print("--> {0} <--".format(names))
            Player_Name = input("Select a player: ").title()
            #VALIDATION 1 : IF THIS IS AN ACTUAL NAME
            for names in Teams[Team_Name]:
                if Player_Name == names:
                    #GOOD
                    #DO IT OVER HERE

                    for event in Events_Teams:
                        for x in range(0,len(Events_Teams[event])):
                            if Team_Name in Events_Teams[event][x]:
                                if Player_Name in Events_Teams[event][x][Team_Name]:
                                    #
                                    print("\n------- Ranking -------")
                                    print("--> 1st Place --> 5 Points")
                                    print("--> 2nd Place --> 4 Points")
                                    print("--> 3rd Place --> 3 Points")
                                    print("--> 4th Place --> 2 Points")
                                    print("--> 5th Place --> 1 Points")
                                    #
                                    print("\n---- INFO ----\nPlayer: {0} \nTeam: {1}\nEvent: {2}".format(Player_Name,Team_Name,event))
                                    Placement = int(input("Enter position for {0} -- Team {1} in {2}: ".format(Player_Name,Team_Name,event)))
                                    #VALIDATION 1 : IF A VALID PLACEMENT WAS CHOSEN
                                    if Placement <= 5 and Placement >= 1:
                                        #VALID ANSWER = GOOD
                                        Score = Ranking[Placement]
                                        #APPLIES IT TO ALL DICTS. AND LISTS AND ALL
                                        if Team_Name not in Team_Scores:
                                            Team_Scores[Team_Name] = []
                                        #APPENDS TO THAT LIST
                                        Team_Scores[Team_Name].append({Player_Name:Score})
                                        #SAVES THIS WHOLE DICT. INTO FILE
                                        with open("Team_Scores.pkl", "wb") as f:
                                            pickle.dump(Team_Scores, f, pickle.HIGHEST_PROTOCOL)
                                        #GIVES A MESSAGE FOR THE USER
                                        print("\n{0}'s Score in Team {1} for Event {2} has been edited.".format(Player_Name,Team_Name,event))
                                        #RETURNS BACK TO MENU
                                        Scores_Menu_2()
                                    #NOT A VALID ANSWER = BAD
                                    else:
                                        print("Enter a valid placement.")
                                        Scores_Menu_2()

                        print("\nTeam / Player is not registered in any event.\n")
                        print("Warning!:\n         Register all players and teams to events \nbefore continuing with Scores.")
            
                    Scores_Menu_2()
                    
            #BAD
            print("\nName not Found!")
            Scores_Menu_2()
    #BAD
    print("\n{0} was not found!".format(Team_Name))
    Scores_Menu_2()

#RESET SCORES FOR A TEAM
def Scores_Menu_2_3():
    print("\n--- Reset Scores for a Team ---")
    for key in Teams:
        print("--> {0}".format(key))
    Team_Name = input("Select a team: ").title()
    #VALIDATION 1 : IF NAME IS IN THE DICT.
    for key in Teams:
        if key == Team_Name:
            #GOOD
            print("")
            for names in Teams[Team_Name]:
                print("--> {0} <--".format(names))
            Player_Name = input("Select a player: ").title()
            #VALIDATION 1 : IF THIS IS AN ACTUAL NAME
            for names in Teams[Team_Name]:
                if Player_Name == names:
                    #GOOD -- NAME WAS FOUND
                    #EVERYTHING WILL BE HERE
                    for x in range(0,len(Team_Scores[Team_Name])):
                        if Player_Name in Team_Scores[Team_Name][x]:
                            #GOOD
                            del Team_Scores[Team_Name][x]
                            #GIVES A MESSAGE FOR THE USER
                            print("Team: {0} Player: {1}'s score has been reset.".format(Team_Name,Player_Name))
                            #RETURNS BACK TO MENU
                            Scores_Menu_2()
                    
            #NAME WAS NOT FOUND
            print("Player not found!")
            Scores_Menu_2()
            
    print("Team not found!")
    Scores_Menu_2()

def Final_Score_Menu():
    print("-------- Final Scores Menu --------")
    temp = int(input("1 - Individual's Scores\n2 - Team's Scores\n3 - Back\nWhere do you want to go?: "))
    #INDIVIDUALS SCORES
    if temp == 1:
        Final_Score_Menu_1()
        Final_Score_Menu()
    #TEAM SCORES
    elif temp == 2:
        Final_Score_Menu_2()
        Final_Score_Menu()
    #RETURNS BACK TO MAIN MENU
    elif temp == 3:
        Main_Menu()
    #IF ANOTHER OPTION WAS GIVEN
    else:
        print("Enter a valid answer!")
        Final_Score_Menu()


#INDIVIDUALS SCORES -- MENU
def Final_Score_Menu_1():
    Sorted_K = sorted(Individuals.keys())
    Sorted_V = sorted(Individuals.values())
    placement = 1
    for score in Sorted_V:
        for name in Sorted_K:
            if score == Individuals[name]:
                print("{0} Place --> {1} --- {2} Points".format(placement,name,score))
                placement += 1
                time.sleep(0.5)

    Final_Score_Menu()
#TEAMS SCORES -- MENU
def Final_Score_Menu_2():
    print("")
    global Team_Final_Scores
    Team_Final_Scores = {}
    placement = 1
    Sorted_Team_Names = sorted(Team_Scores.keys())
    for Team_Name in Sorted_Team_Names:
        for x in range(0,len(Team_Scores[Team_Name])):
            Sorted_Player_Names = sorted(Team_Scores[Team_Name][x].keys())
            Sorted_Player_Scores = sorted(Team_Scores[Team_Name][x].values())
            #
            for score in Sorted_Player_Scores:
                for player_name in Sorted_Player_Names:
                    if player_name in Team_Scores[Team_Name][x]:
                        if score == Team_Scores[Team_Name][x][player_name]:
                            #print("{0} Place --> Team: {1} --> Player: {2} --- {3} Points".format(placement,Team_Name,player_name,score))
                            Team_Final_Scores["Place --> Team: {0} --> Player: {1} --- ".format(Team_Name,player_name)] = score
                            placement += 1
            #
    global Sort_DICT
    sort_dict = {key:score for score, key in sorted(Team_Final_Scores.items())}

    global sorted_dict_one
    sorted_dict_one = {str(k):rank for rank, key in enumerate(sorted(Team_Final_Scores.items(), key = lambda x: x[1], reverse = True), 1) for k in key}

    global final_touch
    final_touch = {k: v for k,v in sorted_dict_one.items() if not k.isdigit()}
    
    for key in final_touch:
        print("{0} {1}{2} Points".format(final_touch[key],key,Team_Final_Scores[key]))

    print("")
    Final_Score_Menu()

# ----------------- STARTS THE WHOLE PROGRAM, LAUNCHED WITH THE INTRODUCTION. ----------------------
Introduction()
