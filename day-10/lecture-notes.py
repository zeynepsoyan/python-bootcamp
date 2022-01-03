# Functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    name = f"{f_name.title()} {l_name.title()}"
    return name

name = format_name("ZEYNEP", "soyAN")
print(name)