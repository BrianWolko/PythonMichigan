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

#excercise hours
hrs = input("Enter Hours:")
h = float(hrs)
svalue = float(input("Enter value of each hour"))

if h > 40.0:
	fval = 40.0 * svalue + (h - 40) * (svalue * 1.5)
else:
	fval = svalue * h
print(fval)

#excersice elif
score = float(input("Enter Score: "))

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print(grade)