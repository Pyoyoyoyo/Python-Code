# File not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} is doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is meeeeeeeeeee")

height = float(input("Height: "))
weight = float(input("Weight: "))
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
