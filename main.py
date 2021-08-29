#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Names/invited_names.txt") as file:
    names_list = file.read().splitlines()
print(names_list)

with open("Letters/starting_letter.txt") as file:
    letter_body = file.read()
    print(letter_body)

for name in names_list:
    with open(f"../mail-change-name/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        name_letter = letter_body.replace("[name]", name)
        file.write(name_letter)



