# functions with output

def format_name(f_name,l_name):
  if f_name == "" or l_name == "":
    return ("You didn't provide valid input")
  name = ""
  name += f_name.title() + " " + l_name.title()

  return name

print(format_name(input("What is your first name? ") , input("What is your last name? ")))