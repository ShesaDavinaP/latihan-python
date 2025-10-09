# grade = 90

# if grade == 100:
#     print("perfecto")
    
# if grade == 90:
#     print("ok")
#     print("keep working hard, bro!")


# str_input = input('enter your grade: ')
# grade = int(str_input)

# if grade == 100:
#     print("awesome")
# elif grade >= 85:
#     print("perfect")
# elif grade >= 65:
#     print("passed the exam")
# else:
#     print("below the passing grade")

str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")
    if grade <= 70:
        print("but you need to improve it!")
    else:
        print("with ok grade")
else:
    print("below the passing grade")