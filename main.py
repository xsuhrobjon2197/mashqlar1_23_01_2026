#1-m

g1 = 99

def dd():
    global g1
    g1 += count

print(g1)

#2-m
summa = 0

def qosh(a):
    global summa
    summa = a + summa

x = qosh(67)
print(f"summaning miqdori: {summa}")


#3-m
text = ""

def matn(a):
    global text
    text += a

x = matn("Hello")
print(x)

#4-m
max_val = 0

def son(a, c, f):
    global max_val
    return  max(son(a, c, f))

x = son(2, 4, 57893475)
print(x)

#5-m
counter = 10

def bol(a):
    global counter
    if counter % 2 == 0:
        return counter


x = bol(76)
print(x)

#6-m
numbers = []
x = numbers.append(777777777777)
print(x)

#7-m
is_active = int(input(""))
is_active1 = False
x = is_active
if x == 0:
    is_active = True

print(is_active1)
