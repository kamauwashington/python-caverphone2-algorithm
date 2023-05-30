from typing import List
import string
    
# defined vowels as well as additional characters defined in the specification ("æ","ā","ø")
__vowels : List[str] = ["a","e","i","o","u","æ","ā","ø"]  
    
# ***** Caversham Project at the University of Otago is the original source algorithm *****
# Caverphone2 implementation https://en.wikipedia.org/wiki/Caverphone#Caverphone_2.0
def caverphone2(input : str) -> str :
    # Step 1.
    # fail fast if input is None or empty (defensive coding)
    if input is None or not input : return None

    # Step 2.
    input = input.lower()

    # Step 3. 
    for char in input :
        if (char not in string.ascii_lowercase) :
            input = input.replace(char,"") 
    
    # Step 4.
    if input.endswith("e") :
        input = input.removesuffix("e")

    # Step 5. (1-6)
    ough_gn_replace : List[str] = [
        "cough","cou2f","rough","rou2f","tough","tou2f",
        "enough","enou2f","trough","trou2f","gn","2n"
    ]
    for idx,itm in enumerate(ough_gn_replace) :
        if (idx % 2 == 0 and input.startswith(ough_gn_replace[idx-1])) :
            input = ough_gn_replace[idx] + input.lstrip(ough_gn_replace[idx-1])
            break

    # Step 6.
    if (input.endswith("mb")) :
        input = input.removesuffix("mb") + "m2"

    # Step 7. (1-17)
    step_7_replace : List[str]= [
        "cq","2q","ci","si","ce","se","cy","sy","tch","2ch","c",'k',"q","k",
        "x","k","v","f","dg","2g","tio","sio","tia","sia","d","t","ph","fh",
        "b","p","sh","s2","z","s"
    ]
    for idx,itm in enumerate(step_7_replace) :
        if idx % 2 == 1 :
            input = input.replace(step_7_replace[idx-1],step_7_replace[idx])

    # Step 7. (18-19)
    step_7_output : str = ""
    for index, char in enumerate(input) :
        if char in __vowels :
            step_7_output += "A" if index == 0 else "3"  
        else :
            step_7_output += char
    input = step_7_output

    # Step 7. (20)
    input = input.replace("j","y")

    # Step 7. (21-22)
    if (input.startswith("y3")) :
        input = input.replace("y3","Y3",1)
    if (input.startswith("y")) :
        input = input.removeprefix("y","A")

    # Step 7. (23)
    input = input.replace("y","3")

    # Step 7. (24)
    input = input.replace("3gh3","3kh3")

    # Step 7. (25)
    input = input.replace("gh","22")

    # Step 7. (26)
    input = input.replace("g","k")

    # Step 7. (27-33)
    identical_adj_chars : List[str] = ["s","t","p","k","f","m","n"]

    output : str = ""
    for index, char in enumerate(input) :
        if char in identical_adj_chars : 
            upper_char : chr = char.upper()
            if len(output) > 0 and output[-1] == upper_char :
                continue
            output += upper_char
            continue
        output += char
    input = output
    
    # Step 7. (34)
    input = input.replace("w3","W3")

    # Step 7. (35)
    input = input.replace("wh3","Wh3")

    # Step 7. (36)
    if input.endswith("w") :
        input = input.removesuffix("w") + "3"

    # Step 7. (37)
    input = input.replace("w","2")

    # Step 7. (38)
    if (input.endswith("h")) :
     input = input.removeprefix("h") + "A"

    # Step 7. (39)
    input = input.replace("h","2")

    # Step 7. (40)
    input = input.replace("r3","R3")

    # Step 7. (41)
    if input.endswith("r") :
        input = input.removesuffix("r") + "3"

    # Step 7. (42)
    input = input.replace("r","2")

    # Step 7. (43)
    input = input.replace("l3","L3")

    # Step 7. (44)
    if input.endswith("l") :
        input = input.removesuffix("l") + "3"

    # Step 7. (45)
    input = input.replace("l","2")

    # Step 8.
    input = input.replace("2","")

    # Step 9.
    if input.endswith("3") :
        input = input.removesuffix("3") + "A"

    # Step 10.
    input = input.replace("3","")
    
    # Steps 11-12.
    input = input.ljust(10,"1")

    return input


