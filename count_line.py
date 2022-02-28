# f = open("people1-exercise.txt","r")
# Count = 0
# Content = f.read()
# CoList = Content.split("\n") 
# for i in CoList:
#     if i:
#         Count += 1
          
# print("This is the number of lines in the file")
# print(Count)



# ##or  counting line
# f=open("people1-exercise.txt")
# Content= f.readlines()
# i=0
# while i< len(Content):
#     i=i+1
# print("count: ",i)
# f.close()

# ##counting ing word
# f=open("word.txt","r")
# a=f.read()
# b=a.split()
# i=0
# c=0
# while i<len(b):
#     if "ing" in b[i]:
#         c=c+1
#     i=i+1
# print("count of ing words",c)
# f.close()

# f=open("my words.txt","r")
# a=f.read()
# b=a.split()
# print(b) 
# print(len(b))  
# # f.close()



# # f=open("my_words.txt")
# # a=f.read()
# # b=a.split()
# # print(b)
# # i=0
# # while i<len(b):
# #     i=i+1
# # print(a)
# # print(i)
# # print(len(a))
# # f.close() 

# # a=["e","k","l"]
# # i=0
# # while i<len(a):
# #     j=0
# #     b=[]
# #     while i<len(a[j]):
# #         b.append(a[j])
# #         j=j+1
# #     print(b)
# #     i=i+1



# # Program to print the fibonacci series upto n_terms
  
# # Recursive function
# def recursive_fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
   
# n_terms = 10
   
# # check if the number of terms is valid
# if n_terms <= 0:
#    print("Invalid input ! Please input a positive value")
# else:
#    print("Fibonacci series:")
#    for i in range(n_terms):
#        print(recursive_fibonacci(i))
