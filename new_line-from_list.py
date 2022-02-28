##Meraki Q3

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file-question3.txt","w")
i=0
while i< len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i=i+1
f.close()
##Q1

batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("")
for student in batch1_students:
    students_file.write("" + student + "\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.close()

##Q2
my_file3 = open("people3.txt", "w")            ###new line
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close()

#Q3
my_file3 = open("test_file.txt", "w")
my_file3.write("My name is Ningthemla Ningshen Khurii")
my_file3.write("\n I want to go back home.")