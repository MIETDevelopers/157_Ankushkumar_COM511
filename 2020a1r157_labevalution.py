# write to perform linear search
list = [2, 3, 4, 5, 6]
value = int(input("Enter  the no do you want to check"))
for i in range(0, len(list)):

    if (list[i] == value):
        print("index of the number is ", i)
        break
