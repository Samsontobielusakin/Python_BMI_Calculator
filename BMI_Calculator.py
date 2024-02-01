name = input('What is your name?: ')
weight = int(input('Enter your weight in pounds?: '))

height = int(input('Enter your height in in inches?: '))

BMI = (weight * 703) / (height ** 2)

if BMI > 0:
    if (BMI < 18.5):
        print('You are underweight')
    elif (BMI <= 24.9):
        print('You are normal weight')
    elif (BMI < 29.9):
        print('You are overweight')
    elif (BMI < 34.9):
        print('You are obese')
    elif (BMI < 39.9):
        print('You are severely obese.')
    else:
        print('You are morbidly obese.')

print('Mr. ' + name + ',' + ' regarding your BMI which is: ' + str(BMI) + ' you can always do better')