def swapFileData():
   Filename1=input("Enter The Path Of First Folder")
   Filename2=input("Enter The Path Of Second Folder")
   with open(Filename1,'r') as a:
       data_a=a.read()
   with open(Filename2,'r') as b:
       data_b=b.read()
   with open(Filename1,'w') as a:
       a.write(data_b)
   with open(Filename2,'w') as b:
       b.write(data_a)
swapFileData()
