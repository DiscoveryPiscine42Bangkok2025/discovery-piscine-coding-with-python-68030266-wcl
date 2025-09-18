import sys
import re

if len(sys.argv) == 2:
    parameter = sys.argv
    user_input = input ("What was the parameter?")
 
    if user_input == parameter:
     print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")