from student import student#first student is filename second student is classname
s=student()
s.setid(3013)
s.setname("Sadhu Chirag")
s.setaddress("NGCCA,income Tax,Ahmedabad")
s.setmarks(99)
print("student ID: ",s.getid())
print("student Name: ",s.getname())
print("student Address: ",s.getaddress())
print("student Marks: ",s.getmarks())