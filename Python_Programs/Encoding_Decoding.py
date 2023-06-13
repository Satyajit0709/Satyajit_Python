logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#. Received the input whether to encode or decode and then check the shift amount  and then get the Plain text
def ciphor(input_text, shift_number, directin_input):
    final_text = ""
    if directin_input == 'decode':
        shift_number *= -1
        print(f"new shift number {shift_number}")
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        final_text += alphabet[new_position]
    print(f"Here is the output f {directin_input} of {input_text} -  {final_text}")


print(logo)
print("Welcome To Ciphor Program \n ")
Play_again =True
while Play_again :
    direction=input("Kindly confirm whether to 'Encode' or 'Decode' \n")
    if not (direction.lower() == "decode"  or direction.lower() == "encode"):
        print("Invalid Option selected - Kindly enter 'Encode' OR 'Decode' ")
        continue
    text= input("Enter the Text - \n")
    shift_amount = int(input("Enter the Shift amount\n"))
    ciphor(input_text=text.lower() , shift_number=shift_amount , directin_input=direction.lower() )

    user_input = input("Press 'Yes' to continue and 'No' to Exit \n")
    if user_input.lower() == "no":
        Play_again = False







