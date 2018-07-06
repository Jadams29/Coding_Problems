# 1. Create a file named mydata2.txt
# 2. Use what you learned in part 8 to find out how to open
#       a file without with (Open in try)
# 3. Catch FileNotFoundError
# 4. In else print contents
# 5. In finally
# 6. Open nonexistent file mydata3.txt

try:
    myFile = open('mydata3.txt', encoding='UTF-8')
except FileNotFoundError as ex:
    print("The file was not found")
    print(ex.args)
else:
    print(myFile.read())
    myFile.close()
finally:
    print("This is always printed")


