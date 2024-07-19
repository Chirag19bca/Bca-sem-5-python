class student:
    marks=10
    @classmethod#it's envole class as whole
    def modify(cls,name):
        print("{1} Scored {2} marks ".format(12,name,cls.marks))
student.modify("Sanjay")
student.modify("Ajay")