# ---------------------- _____IMPORTS____ ---------------------- 
import time
import re
import os
# ------- LISTS & DICTIONARIES ----------
# ----- Individuals Dict. Name : Score -----
Individuals = {}
# ----- Individuals list. Name -----
Individuals_List = []
# ----- Teams Dict. Name : Players -----
Teams = {}
# ----- Teams List. Name -----
# MAX 4 Teams
#THIS CONTAINS NAMES OF ALL TEAM NAMENAMES
Teams_List = []
#THIS IS THE TEAM'S LIST
Team_List_0 = []
Team_List_1 = []
Team_List_2 = []
Team_List_3 = []

Teams_ID = {}


#    ------------------- THIS IS THE INTRODUCTION ---------------------
#    -------------------- CHANGE TO WHATEVER THE FIRST MESSAGE IS THAT WILL POPUP -----------------
def Introduction():
    #THIS IS JUST AN INTRODUCTION
    print("Welcome to Jimesh's World\n") #\\\\\CHANGE THIS LATER/////#
    print("Note!:\n      Players in Individuals cannot be entered into a team. \n      Enter players for a team from team's menu\n")
    #PasteValues()
    PasteValues()

def PasteValues():
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
        """
        #ADDING TO THE DICT.
        Individuals[BLines[x]] = 0
        """
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
    #print(num_lines) #THIS IS TEMP JUST A NUMBER
    # ------ THIS IS TO IMPORT TEAM MEMBERS ------- ||||||  DO THIS AFTER ||||||
    # --- THIS IS FOR THE FIRST TEAM ---
    x = 0
    for lop in range(0,num_lines):
        TeamName = BLines3[x]
        print(BLines3[x])

        #ADDING TO THE TEAM_ID DICT.
        Teams_ID[x] = BLines3[x]
        
        Team_File = open('%s.txt' % TeamName,"r")
        Team_Members = Team_File.readlines()
        #print(Team_Members) TEMP
        global Team_Members2
        Team_Members2 = [s.replace('\n', '') for s in Team_Members] #THIS IS THE STRIPPED VERSION
        #DO THIS 
        # print(Team_Members2) THIS IS THE VARIABLE FOR THE TEAM MEMBER NAMES
        
        for teamname in Teams_ID:
            print("asd " + str(teamname))
            ID = teamname

        print(len(Team_Members2))
        
        if ID == 0:
            for member in Team_Members2:                
                Team_List_0.append(member)
        elif ID == 1:
            for member in Team_Members2:                
                Team_List_1.append(member)
        elif ID == 2:
            for member in Team_Members2:                
                Team_List_2.append(member)
        elif ID == 3:
            for member in Team_Members2:                
                Team_List_3.append(member)
              
        Team_File.close()
        x += 1

    """
    x = 0
    for yuy in range(0,num_lines):
        team_names = BLines3[x]
        print(team_names)
        team_file = open(team_names + ".txt","r")
        lines4 = team_file.readlines()
        BLines4 = [s.replace('\n', '') for s in lines4]
        print(str(BLines4) + " Individuals")
        xpa = 0
        for rtt in BLines4:
            Teams_List1.append(rtt)
            print(rtt)
            xpa += 1
        lenght_of_file = len(BLines4)
        xp = 0
        for tyt in range(0,lenght_of_file):
            Teams[team_names] = BLines4[xp]
            xp += 1
        x += 1
    """
    """
    x = 0
    
    for gjg in range(0,num_lines):
        file_name = BLines3[x]
        team_file = open(file_name + ".txt","r")
        team_num_lines = sum(1 for line in open(file_name + '.txt'))
        lines4 = team_file.readlines()
        BLines4 = [s.replace('\n', '') for s in lines4]
        for yuy in range(0,team_num_lines):
            print(BLines4[x] + " PLAYERS")


        team_file.close()
        x += 1

"""
    file.close()
    Main_Menu()

#THIS IS THE FUNCTION THAT WILL RESET ALL MY STORED DATA
def Reset():
    #ASKING TO CONFIRM 
    temp = input("Are you sure that you want to reset?(Y/N): ")
    temp = temp.title()
    #CONFIRMED
    if temp == "Y":
        # ----------------- INDIVIDUALS -----------------
        #CLEARS THE FILE
        open('Individual_Names.txt', 'w').close()
        #CLEARS THE LISTS
        del Individuals_List[:]
        #CLEARS THE DICTIONARIES
        Individuals.clear()
        #GIVES A MESSAGE FOR THE USER
        print("Program has been factory reset.")
        #RETURNS BACK TO THE MAIN MENU AFTER RESET
        Main_Menu()
    #NOT CONFIRMED
    elif temp == "N":
        print("Returning to Main Menu...")
        time.sleep(0.5)
        Main_Menu()
    #WHAT IF VALID OPTION IS NOT PROVIDED
    else:
        print("Not a valid option!")
        time.sleep(0.5)
        print("Returning to Main Menu...")
        time.sleep(0.5)
        Main_Menu()
    return

#   ------------------- THIS IS THE MAIN MENU. USER DECIDES WHICH SUB MENU TO NAVIGATE TO. --------------------
def Main_Menu():
    try:
        # THIS PRINT IS JUST FOR AESTHETICS PURPOSES 
        print("-------- Main Menu --------")
        # INPUT WITH ALL THE OPTIONS LISTED. NUMBER REPRESENTS THE OPTION
        M_M = int(input("1 - Individuals\n2 - Teams\n2 - Events\n4 - Scores\n5 - Reset all Data\n6 - Exit\nWhere do you want to go?: "))
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
        #EXITING
        elif M_M == 6:
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
        Add_Individual = input("\nPlease enter a full name: ")
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
            Teams_Menu_1()
        #ADD TEAMS
        elif T_M == 2:
            Teams_Menu_2()
        #REMOVE TEAMS
        elif T_M == 3:
            Teams_Menu_3()
        #ADDING PLAYERS TO TEAMS
        elif T_M == 4:
            Teams_Menu_4()
        #REMOVE PLAYERS FROM TEAMS
        elif T_M == 5:
            return
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
            php = 1
            Teams[team_name] = str(Teams_List) + str(php)
            php += 1
            #THIS CREATES A FILE USING THE TEAM NAME
            team_file = open('%s.txt' % team_name, 'a+')
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
                #DELETES THE TEAM FILE
                os.remove(str(remove_team) + ".txt")
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
            Team_File = open(Team_Selected + ".txt","a+")
            Team_File.write(Player_Name + "\n")
            Team_File.close()
            print("Player has been added to " + Team_Selected)
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
    return
#   ---------- THIS IS THE SCORES MENU. EVERYTHING RELATING TO SCORES IS HERE -----------
def Scores_Menu():
    return


# ----------------- STARTS THE WHOLE PROGRAM, LAUNCHED WITH THE INTRODUCTION. ----------------------
Introduction()
