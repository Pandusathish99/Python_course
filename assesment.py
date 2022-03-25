assesment = " Practicing the python"
print(assesment) # print the string
print(len(assesment)) # calculate the words
print(assesment.strip()) # strip remove the start and end space
print(assesment.lstrip()) # remove the left side space of the line
print(assesment.rstrip()) # remove the right side space
print(assesment.find("python")) # Find the alpha number arrangement as in 16
print(assesment.find('the'),len(assesment)) # find the letter arrangement and total lenth
print(assesment.count("the")) # find the repeated words/letters
print(assesment[13]) # finding the index value of "H"
print(assesment.upper()) # convert into upper case
print(assesment.lower()) # convert into lower case
print(assesment.title()) # covert the first letter of the word into Capital letter
print(assesment[0:9]) # slicing the words/line
print(assesment[0:])
print(assesment[:12])
print(assesment[::-1])
print(assesment.capitalize())
print(assesment.swapcase())
print(assesment.split())
print(assesment.islower())
print(assesment.isupper())

# checking upper case if it's True or False
again = "TESTING THE UPPER AND LOWER CASE"
print(again.isupper())
print(again.islower())

# cheking lower case if it's True or False
test = " all are lower case's "
print(test.lower())
print(test.islower())
print(test.isupper())

# Mathematics
# addition
val1 = 65
val2 = 98
add = val1+val2
print(add)
print("value of val1 and val2 after addition :", add)

# Substract
d1=65
d2=36
deduct = d1-d2
print("value of deduction :", deduct)

# Multiplication
M1 = 2598
m2 = 251
Multiple = M1 * m2
print("multiplication of value:", Multiple)

# Division
B = 9854
B1 = 36251
div= B1/B
print(" Division value is: ", div)
print(B1**B)
print(B%B1)
print(B>=B1)
print(B>B1)
print(B>B1)
print(B1>B)
print(B==B1)
print(B!=B1)
print(B<=B)

# Age comparisation to using bulean
Sateesh = 28
Laghu = 27
Age = Sateesh>Laghu
age = Sateesh<Laghu
age1 = Sateesh==Laghu
age2 = Sateesh!=Laghu
age3 = Sateesh<= Laghu
age4 = Sateesh>=Laghu
print(Age)
print(age)
print(age1)
print(age2)
print(age3)
print(age4)



