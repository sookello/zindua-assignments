user_age = int(input('Please enter your age: '))

if user_age >= 18:
    print('You are an adult.')
    if user_age >= 21:
        print('You are eligible to vote.')
    else:
        print('You are a minor') 


