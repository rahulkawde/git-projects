#BMI CALCULATOR:

height = float(input('Enter your height in meter:'))
weight = float(input('Enter your weight in kg:'))

BMI = ( weight/ (height**2))

# def type_bmi(BMI):

def types(BMI):
    if BMI < 16:
        print ('serverly underweight')
    elif BMI>= 16 and BMI < 18.5:   
        print('underweight')
    elif BMI >= 18.5 and BMI < 25:
        print('Healthy')
    else:
        print('overweight')
                 

types(BMI)
print(f'your BMI is{BMI} ')

