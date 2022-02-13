# This is going to ask for the month and year and tell you how many days was in that particular month

def is_leap(isyear):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
   

# is_leap
def days_in_month(year,month):
  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  smonth = month - 1
  
  if is_leap(year) == True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return month_days[smonth]
   
  return month_days[smonth]



  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

