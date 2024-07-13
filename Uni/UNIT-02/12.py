def plus_three(num):
    def add_three(num):
        return num+3
    result=add_three(num)
    return result
no1=6
print(plus_three(no1))