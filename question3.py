def classify(input):
    if input == "CSC1006":
        print("Mathematics 2")

    elif input == "CSC1007":
        print("Operating Systems")

    elif input == "CSC1008":
        print("Data Structures and Algorithms")

    elif input == "CSC1009":
        print("Object-oriented Programming")

    elif input == "CSC1010":
        print("Computer Networks")

    else:
        print("InvalidCode")


print("Question 2b Output")
#get module code from user
userinput = input("Input module code: ")
#print out module name through ifelse loop
classify(userinput)

print("Question 2c Output")
#print all odd numbers from 102 in descending order
for i in range(102, 65, -1):
    if i % 2 == 0:
        continue
    else:
        print(i)
