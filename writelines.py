##writelines() function
##This function writes the content of a list to a file.

file1 = open("Employees.txt", "w")
lst = []
for i in range(4):
    name = input("Enter the name of the employee: ")
    lst.append(name + '\n')
      
file1.writelines(lst)
file1.close()
print("Data is written into the file.") 



###write() function
##The write() function will write the content in the file without adding any extra characters.
file = open("Employees.txt", "w")
  
for i in range(3):
   name = input("Enter the name of the employee: ")
   file.write(name)
   file.write("\n")
     
file.close()
  
print("Data is written into the file.")