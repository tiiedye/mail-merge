# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as guest_names:
    guests = guest_names.readlines()

for guest in guests:
    guest_name = guest.replace("\n", "")
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_text = letter.read()
        new_letter_text = letter_text.replace("[name]", f"{guest_name}")
    with open(f"./Output/ReadyToSend/letter_to_{guest_name}.txt", mode="w") as new_letter:
        new_letter.write(new_letter_text)
