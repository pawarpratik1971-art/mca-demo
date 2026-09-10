age = int(input("enter your age :  "))
role = input("Enter role (student,teacher): ")


# print(f"{a} years = {a*365} days")
# print(f"{min} is {min//60} hours {min%60} minutes")
# print(f"{a} : last digit is {str(a)[-1]}")
print(f"Eligible : ",age < 21 and role == "student")