day = input("Enter the day of the week: ")

if day == "Monday":
    print("Start of the week")
elif day in ["Tuesday", "Wednesday", "Thursday"]:
    print("Midweek")
elif day == "Friday":
    print("Almost weekend")
elif day in ["Saturday", "Sunday"]:
    print("Weekend!")
else:
    print("Invalid day")