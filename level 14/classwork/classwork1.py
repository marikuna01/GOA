
age = int(input("please enter your age: "))
experience = int(input(":please input your experience "))
height = int(input("please input your hight: "))



isHired = age >= 18 and experience >= 2 and height >= 175

# შედეგის გამოტანა
print("You are hired:", isHired)