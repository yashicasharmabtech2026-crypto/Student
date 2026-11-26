int(marks)
int(input("Enter your marks:"))
if (marks>90):
  print("A+ grade")
elif(marks>80 & marks<90):
  print("A grade")
elif(marks>70 & marks<80):
  print("B grade")
elif(marks>60 & marks<70):
  print("C grade")
elif(marks>0 & marks<60):
  print("F grade") 
else:
  print("Invalid")