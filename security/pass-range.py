import string
echars = string.digits+string.ascii_letters+''' !@#$%^&*()_+-=[{]}'",./<>?;:'''
echars = string.digits+string.ascii_letters

def gen_char():
    return (c for c in echars)

def gen_char2():
    for c in gen_char():
        for c2 in gen_char():
            yield c+c2
def gen_char3():
    for c in gen_char2():
        for c2 in gen_char():
            yield c+c2
def gen_char4():
    for c in gen_char3():
        for c2 in gen_char():
            yield c+c2

def gen_char_factory(n=4):
    if n <=1:
        #for c in gen_char(): yield c
        yield from gen_char()
        return
    for c in gen_char_factory(n-1):
        for c2 in gen_char():
            yield c+c2

def gen_password(mbits=2):
    for i in range(mbits):
        gen = gen_char_factory(i+1)
        for password in gen:
            yield password

for i in gen_password(2):
    print(i)

print(echars)
