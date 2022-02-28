# Here is the complete list of methods in text mode with a brief description:

# Method	Description
# close()	Closes an opened file. It has no effect if the file is already closed.
# detach()	Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno()	Returns an integer number (file descriptor) of the file.
# flush()	Flushes the write buffer of the file stream.
# isatty()	Returns True if the file stream is interactive.
# read(n)	Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable()	Returns True if the file stream can be read from.
# readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()	Returns True if the file stream supports random access.
# tell()	Returns an integer that represents the current position of the file's object.
# truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable()	Returns True if the file stream can be written to.
# write(s)	Writes the string s to the file and returns the number of characters written.
# writelines(lines)	Writes a list of lines to the file.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt", "r")
# print(f.read())

# f=open("demofile.txt")
# print(f.readline())
# f.close()





# f = open("demofile.txt", "r")
# print(f.read(5))
# f.close()

# f = open("demofile.txt", "r")
# print(f.read(15))
# f.close()


# my_file = open("people.txt")
# file_data = my_file.read()
# print (file_data)
# my_file.close()

# my_file2 = open("people2.txt","w+")
# my_file2.write("Abhishek - Gurgaon")
# my_file2.write("Ranveer - Delhi")
# # # print(my_file2.seek(0))
# my_file2.seek(0)
# print(my_file2.read())
# my_file2.close()


# my_file2 = open("people2.txt", "w")      ##could not read in w
# my_file2.write("Abhishek - Gurgaon")
# my_file2.write("Ranveer - Delhi")
# # print(my_file2.seek(0))
# my_file2.seek(0)
# print(my_file2.read())
# my_file2.close()


