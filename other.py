largest = -10000
smallest = 10000
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:    
        if int(num) < smallest:
            smallest = int(num)
        elif int(num) > largest:
            largest = int(num)
    except:
        	print("Invalid imput")

print("Maximum is", largest)
print("Minium is", smallest)