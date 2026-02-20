# ques Create a dictionary that stores 5 students’ names and their marks.
# Find the average marks of all students.

Students = {
    "Akash":85,
    "Priyanshu":90,
    "Abhay":95,
    "Rohit":80,
    "Satyam":88
}

total = sum(Students.values())
average = total/ len(Students)
print("Average marks of students is : ", average)
  
  
  
