while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:    
        if int(num) < smallest or smallest == None:
            smallest = int(num)
        elif int(num) > largest or largest == None:
            largest = int(num)
    except:
        	print("Invalid imput")

print("Maximum is", largest)
print("Minium is", smallest)