# Calculator

# Add
def add(n1,n2):
  return n1 + n2
# Minus
def minus(n1,n2):
  return n1 - n2
# Multiply
def multiply(n1,n2):
  return n1 * n2
# Divide
def divide(n1,n2):
  return n1 / n2


operations = {"+":add,
"-": minus,
"*": multiply,
"/": divide,
} 

num1 = int(input("What's the first number?: "))

for i in operations:
  print(i)
math = input("pick out an operation from the line above " )

num2 = int(input("What's the second number?: "))

mathoperation = operations[math] 
first_answer = mathoperation(num1, num2)

print(f"{num1} {math} {num2} = {first_answer} ") 

stop = False
while not stop:
  
  math = input("Pick another operation: ")
  num3 = int(input("What's the next number?: "))
  mathoperation = operations[math]
  second_answer = mathoperation(first_answer,num3)
  print(f"{first_answer} {math} {num3} = {second_answer}")

  stop_now = input(f"Type 'y' to continue calculating with {second_answer} , or type 'n' to quit: ")
  if stop_now == "n":
    stop = True
    print("Thanks for calculating with us :) ")
  
