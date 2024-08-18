
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
def format_name(first_name, last_name):
    """Take a first and last name and format it to return 
    the title case version of the name."""
    if first_name == "" or last_name == "":
        return
    full_name = (first_name + " " + last_name).title()
    return full_name


print(format_name(first_name=first_name, last_name=last_name))