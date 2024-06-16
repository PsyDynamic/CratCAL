### Crate calculator for production line 4 ###

import math                                                                                                                                             ### Importing math module for rounding function and os module for clear-screen cmd ###
import os
loop = 1
 

while loop == 1:                                                                                                                                        ### While-loop to keep the script running as long as the loop value stay True , in this case 1 ###
    os.system('cls')                                                                                                                                    ### Imported function from the os module. Clears the terminal for better overview after a restart ###
    current_state = int( input("Welcome! How many crates are currently stored?\n") )                                                                    ### Crates in magazine are stored via user input in variable 'current_state' ###
    max_magazine = 2736                                                                                                                                 ### Setting max. size of the magazine and calculate needed crates for '100%' and '85%'  ###
    pallet_hub = ( 9 * 4 ) * 6                                                                                                                          ### 'pallet_hub' variabel sets the size of an hub ( 6 pallets ; 4 layers of crates ; 9 crates per layer ) ###
    current_display = math.ceil( current_state / ( max_magazine / 100 ) )                                                                               ### Using 'math.ceil' function to raise the calcualted number by 1 so they're always enough crates ordered ###        

    if current_state < 0 or current_state > 2736 :                                                                                                      ### 'if' statement checks for valid user input that is in the range of 0 ---> 2736 ###
        print("Please enter a valid input between 0 and 2736.")

    else:                                                                                                                                               ### 'else' statement prints needed crates and hub for 85 % and 100 % ### 
        crates_needed_max = max_magazine - current_state
        hub_needed_max = math.ceil( crates_needed_max / pallet_hub )
        crates_needed_85 = math.ceil(crates_needed_max - ((max_magazine / 100) * 15))
        hub_needed_85 = math.ceil( crates_needed_85 / pallet_hub )
                                                                                                                                                         
        print(f'''
    #######################################################
    ####################      {current_display}%      ####################
    #######################################################\n''')
        print(f"You currently have {current_display}% in the magazine.\n")
                                                                                                                                                        ### The float's in parentheses are the unraised numbers to check the real value against the raised ###
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
    
    loop = int(input("If you want to restart press 1\n"))                                                                                                    ### Updating loop variabel via user input. If the user input is 1 , then the loop variabel keep its value and continous the while-loop ###