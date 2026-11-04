import Studentmanager1 as student
interface={
    "Add student":student.addstudent,
    "Update student ":student.updatestudent,
    "Result":student.viewstudent,
    "Position":student.position,
    "View all students":student.viewall
}
while True:
 for que in interface.keys():
    print(que)
 choice=input("What do you want to do:")
 if choice in interface.keys():
    interface[choice]()
 exit=input("Do you want to exit:")
 if exit.lower()=="yes":
   break