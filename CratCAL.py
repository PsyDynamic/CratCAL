### Crate calculator for production line 4 ###
### Note that this is experimental and WILL change its functions when the script is converting to an GUI interface! ###

### Importing math module for rounding function and os module for clear-screen cmd ###
### max_magazine variable sets the maximal amount of crates that can be stored in the magazine ###
### 'pallet_hub' variable sets the size of an hub (9 crates per layer ; 4 layers of crates ; 6 pallets) ###

import math
import os
max_magazine = 2736
pallet_hub = 216
loop = 1

### While-loop to keep the script running as long as the loop value stay True, in this case 1 ###
### Imported function from the os module. Clears the terminal for better overview after a restart ###
### Crates in magazine are stored via user input in variable 'current_state' ###
### Using 'math.ceil' function to raise the calcualted number by 1 so they're always enough crates ordered ###

while loop == 1:
    os.system('cls')
    current_state = int( input("Welcome! How many crates are currently stored?\n") )
    current_display = math.ceil( current_state / ( max_magazine / 100 ) )
    
    ### 'if' statement checks for valid user input that is in the range of 0 ---> 2736 ###

    if current_state < 0 or current_state > 2736:
        print("Please enter a valid input between 0 and 2736.")

    ### 'else' statement prints needed crates and hub for 85 % and 100 % ### 

    else: 
        crates_needed_max = max_magazine - current_state
        hub_needed_max = math.ceil( crates_needed_max / pallet_hub )
        crates_needed_85 = math.ceil( crates_needed_max - ((max_magazine / 100) * 15) )
        hub_needed_85 = math.ceil( crates_needed_85 / pallet_hub )
                                                                                                                                                         
        print(f'''
    #######################################################
    ####################      {current_display}%      ####################
    #######################################################\n''')
        print(f"You currently have {current_display}% in the magazine.\n")

    ### The float numbers in parentheses are the unraised numbers to check the real value against the raised ###

        print('''
    #######################################################
    ####################      85%      ####################
    #######################################################\n''')
        print(f"You need {crates_needed_85} crates.\nThat's {hub_needed_85} hub.\n( {round(crates_needed_85 / pallet_hub , 1)} )\n")

        print('''
    #######################################################
    ####################      100%      ###################
    #######################################################\n''')
        print(f"You need {crates_needed_max} crates.\nThat's {hub_needed_max} hub.\n( {round(crates_needed_max / pallet_hub , 1)} )\n")

    ### Updating loop variabel via user input. If the user input is 1 , then the loop variabel keep its value and continous the while-loop ###

    loop = int(input("If you want to restart press 1\n"))
