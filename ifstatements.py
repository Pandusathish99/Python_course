Telugu = 36
English = 28
Hindhi = 41
Science = 25
Social = 30
Total = Telugu+English+Hindhi+Science+Social
print(Total)
avarage = Total/5
print((avarage))
if avarage>=70:
    print("Distanction")
else:
    print('First Class')
    if avarage>=60:
        print('First class')
    else:
        print('Second Class')
        if avarage>=50:
            print('second Class')
        else:
            print('Third Class')
            if avarage>=50:
                print('Third Class')
            else:
                print('Pass')
                if avarage<35:
                    print('Fail')
                    print(" 'Finally as per my knowledge OF my first if and else condition program is SUCCESSFULLY EXECUTED' ")
                    print('  Note: I have struck at elif condition')