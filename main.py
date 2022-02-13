# Docstrings
# functions with output

def format_name(f_name,l_name):
  """Take frst and last name and return title case version of the name."""
  if f_name == "" or l_name == "":
    return ("You didn't provide valid input")
  name = ""
  name += f_name.title() + " " + l_name.title()

  return name

print(format_name(input("What is your first name? ") , input("What is your last name? ")))



"""
you can also use docstring to make comments, but thats too bothersome
"""