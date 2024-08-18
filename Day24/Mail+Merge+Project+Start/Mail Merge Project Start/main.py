# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()

print(letter)

with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names = [name.rstrip() for name in invited_names]

print(names)
for name in names:
    name_letter = letter.replace("[name]", name)
    print(name_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as send_letter:
        send_letter.write(name_letter)

