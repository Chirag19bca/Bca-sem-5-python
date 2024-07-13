#positional arguement
def pos(ram,shyam,harish):
    print(ram,shyam,harish)
a='Ram'
b='Shyam'
c='Harish'
pos(a,b,c)

#kyword arguement
def kyword(ram,shyam,harish):
    print(ram,shyam,harish)
a='Ram'
b='Shyam'
c='Harish'
kyword(a,b,c)

def kyword(ram,shyam,harish='harish'):
    print(ram,shyam,harish)
a='Ram'
b='Shyam'
kyword(a,b)