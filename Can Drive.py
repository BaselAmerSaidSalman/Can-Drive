age = int(input("Please enter your age: \n"))
if age < 18:
  print("Sorry, you can't drive, you should atleast be 18 years old")
else:
  print("Good, Answer the next question")
  license = input("Do you have a license? Type (Yes) or (No) \n").lower()
  while license != "yes" and license != "no":
    print("Invalid input, The word [ {license} ] I can't understant it, Please try again")
    license = input("Do you have a license? Type (Yes) or (No) \n").lower()
  if license == "yes":
    print("You can drive")
  elif license == "no":
    print("Sorry, you can't drive")
  
  