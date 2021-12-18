#if sentence
x = 5

if x == 7:
    print("true")
elif x == 6:
    print("false")
else:
    print("me doy")

#for sentence
for i in range(5):
    print(i)

#try except sentences
age = input("please select your age")
try:
    int(age) + 1
except:
    age = -1

print(age)