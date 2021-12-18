hrs = input("Enter Hours:")
h = float(hrs)
svalue = float(input("Enter value of each hour"))

if h > 40.0:
	fval = 40.0 * svalue + (h - 40.5) * (svalue * 1.5)
else:
	fval = svalue * h
print(fval)