# Sudent Marksheet

Sudent_Name=str(input('Enter the student Name :'))
Telugu = int(input('Enter Telugu Marks :'))
English = int(input('Enter English Marks :'))
Hindi = int(input('Enter Hindhi Marks :'))
Maths = int(input('Enter Maths Marks :'))
Science = int(input('Enter Science Marks :'))
Social = int(input('Enter Social Marks :'))
Total = Telugu+English+Hindi+Maths+Science+Social
print(Total)
Avarage = Total/6
print(Avarage)
if Avarage>=75:
    print("Distinction")
elif Avarage>=70:
    print("First Class")
elif Avarage>=65:
    print('Second Class')
elif Avarage>=60:
    print('Third class')
elif Avarage>=35:
    print('Pass')
else:
    # Avarage<=35:
    print('fail')