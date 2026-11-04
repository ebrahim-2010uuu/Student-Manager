class Student:
    school="DPS"
    branch="Township"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def inputmarks(self):
     self.marks={}
     subjects=["English","Urdu","Math","Physics","computer","T.Q"]
     for subject in subjects:
        while True:
         try:
          self.marks[subject]=float(input(f"Ente your {subject} marks(out of 100):"))
          if self.marks[subject]>100:
             print("Enter marks between 0 and 100")
          else:
           break
         except ValueError:
            print("Enter valid data ⚠️\n")
         
     return self.marks
     
    def totalmarks(self):
        total=0
        for i in self.marks.values():
            total+=i
        return total
    def percentage(self):
       percentage=self.totalmarks()/(len(self.marks)*100)*100
       return percentage
    def averagemarks(self):
       avg=self.totalmarks()/6
       return avg
    def highestsubjet(self):
       highest=0
       for i in self.marks.values():
          if i>highest:
             highest=i
       for x,y in self.marks.items():
          if highest==y:
             return(f"You got highest marks in {x}")
    def grade(self):
       x=self.percentage()
       if x>=90:
          grade="A"
       elif x>=80:
          grade="B"
       elif x>=70:
          grade="D"
       elif x>=50:
          grade="E"
       else:
          grade="Fail"
       return grade
          
        
Students={}
def addstudent():
 print("\t\t\t\t\t\t  ---------------------Welcome to Student Manager👤---------------------")
 print("Student Information form🆔\n")
 while True:
     while True: 
      name=input("Enter the name of the student:").strip().title()
      if not name:
         print("Name cannot be blank ⚠️\n")
         continue
      elif not name.replace(" ","").isalpha():
         print("You can only enter letters(a-z)⚠️\n")
         continue
      elif name in Students:
         print("Name already taken ⚠️\n")
         continue
      else:
         break
     print(f"\n✅ Student name:{name}\n")
     while True:
       try:
        rollno=int(input("Enter the roll no. of the student:"))
        break
       except ValueError:
          print("Enter numbers only ⚠️\n")
     student=Student(name,rollno)
     Students[student.name]=student
     print("\nStudent added successfully ✅\n\n")
     print("\t\t\t\t\t\t  ---------------------Marks Entry📋---------------------")
     Students[student.name].inputmarks()
     print("\nExit or Continue 🔄")
     while True:
      exit=input("Do you want to exit:")
      if not exit:
         print("Please enter yes or no ⚠️\n")
         continue
      elif not exit.isalpha():
         print("Enter only yes or no ⚠️\n")
         continue
      elif exit.lower() not in ["yes","no"]:
         print("Enter only yes or no ⚠️\n")
         continue
      else:
       break
     if exit.lower()=="yes":
        print("\nAll students are added successfully 🎉")
        break          
def viewstudent():
 while True:
   while True:
    name=input("Enter the name of the student:").strip()
    if not name:
       print("Please enter name.")
    elif not name.replace(" ","").isalpha():
       print("Enter letters only(a-z)")
    else:
       break
   if name in Students:
      print("Name:",name)
      print("Roll no:",Students[name].roll_no)
      print("Marks:",Students[name].totalmarks(),"/",len(Students[name].marks)*100)
      print("Percentage:",Students[name].percentage(),"%")
      print("Average marks:",Students[name].averagemarks())
      print("Highest subjet:",Students[name].highestsubjet())
      print("Grade:",Students[name].grade())
   else:
      print("Student not found!")
   while True:
    exit=input("Do you want to exit:")
    if not exit:
       print("Please enter your choice")
    elif not exit.isalpha():
       print("Please enter your choice")
    elif exit.lower() not in ["yes","no"]:
       print("You can only type(yes or no)")
    else:
       break
   if exit.lower()=="yes":
      break
def updatestudent():
 while True:
   choices=["Name","Roll no", "Marks"]
   choices_lowercase=[name.lower() for name in choices]
   while True:
    name=input("Enter name:")
    if not name:
       print("Enter the name of student!")
    elif not name.replace(" ","").isalpha():
       print("Enter name of the student!")
    else:
       break
   if name in Students:
      for x in choices:
         print(x)
      while True:
       choice=input("What do you want to do:")
       if not choice:
          print("Enter the correct choice!")
       elif not choice.replace(" ","").isalpha():
          print("Enter the correct choice")
       elif choice.lower() not in choices_lowercase:
          print("Enter the correct choice")
       else:
          break
      if choice.lower()==choices[0].lower():
         while True:
          new_name=input("Enter new name:")
          if not new_name:
                 print("Enter the name of student!")
          elif not new_name.replace(" ","").isalpha():
                 print("Enter name of the student!")
          else:
             break
         Students[new_name]=Students[name]
         Students.pop(name)
      elif choice.lower()==choices[1].lower():
         while True:
          try:
           new_no=int(input("Enter new roll no:"))
           break
          except ValueError:
             print("Enter valid roll no.")
         Students[name].roll_no=new_no
      elif choice.lower()==choices[2].lower():
         while True:
          sub=input("Enter the name of the subject:")
          if not sub:
                 print("Enter the name of subject!")
          elif not sub.replace(" ","").isalpha():
                 print("Enter name of the subject!")
          elif sub not in Students[name].marks.keys():
             print("Enter correct subject name!")
          else:
             break
         if sub in Students[name].marks.keys():
            while True:
             try:
               new_marks=int(input(f"Enter new marks of {sub}:"))
               if new_marks>100:
                  print("Enter marks between 0 to 100.")
               else:
                break
             except ValueError:
                print("Enter marks between 0 to 100.")
            Students[name].marks[sub]=new_marks
   while True:
    exit=input("Do you want to exit:")
    if exit.lower() not in ["yes","no"]:
       print("Enter only yes or no")
    else:
      break
   if exit.lower=="yes":
      break
def deletestudent():
   name=input("Enter the name of the student:")
   if name in Students:
      Students.pop(name)
      print("Student deleted successfully!")
   else:
      print("Student not found!")
def viewall():
   for name in Students:
      print("Name:",name)
      print("Roll number:",Students[name].roll_no)
      print("Percentage:",Students[name].percentage())
def position():
   highest=0
   for name in Students:
         if Students[name].totalmarks()>highest:
            highest=Students[name].totalmarks()
   for name in Students:
      if Students[name].totalmarks()==highest:
         print(f"{Students[name].name} has got 1st position in class.")