
def calc_bmi(name, wgt, hgt):
    bmi = wgt/(hgt ** 2)
    print("\n{0}'s BMI is {1:.2f}".format(name, bmi))
    if bmi < 18.5:
        print("{0} is underweight".format(name))
    elif bmi >= 18.5 and bmi <=24.9:
        print("{0} is healthy".format(name))
    elif bmi >= 25 and bmi <=29.9:
        print("{0} is overweight".format(name))
    else:
        print("{0} is obese".format(name))

def message():
    print("hello")