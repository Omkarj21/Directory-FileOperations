f1 = open("om.txt")  # equivalent to 'r' or 'rt'
f2 = open("om.txt", 'w')  # write in text mode
f3 = open("om.txt", 'r+b')  # read and write in binary mode
f4 = open("om.txt", mode='r', encoding='utf-8')
f1.close()
# when working with files in text mode, it is highly recommended to specify the encoding type.
with open("om.txt", 'w', encoding='utf-8') as f5:
    f5.write("first file\n")
    f5.read()  # Read full data
    f5.read(5)  # Read the first 5 characters
    f5.tell()  # get the current file position
    f5.seek(0)  # bring file cursor to initial position
    f5.readline()  # reads a file till the newline,
