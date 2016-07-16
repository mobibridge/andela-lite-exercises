from datetime import datetime

current_year=datetime.now().year

student=dict()
student={'name':['hillary','muriuki']}
student.update({'dob':1990})
student.update({'phonenumber':'0727622824'})

age=current_year-student.get('dob')


full_name = student.get('name')
print (student)
print (full_name[0],full_name[1])
print (student.get('dob'))
print (student.get('phonenumber'))
print (age)



