name = input('Do you like pasta')
name
print(name)

"""How do you like your past sauce"""
print('How do you like your past sauce rating 1-3')

number1 = int(input('no sauce:  '))
number2 = int(input('easy sauce:  '))
number3 = int(input('heavy sauce:  '))

if number1 < 0:
    print(number1,'No Sauce on pasta')
if number2 == 0:
    print(number2,'Easy Sauce on pasta')
if number3 > 0:
    print(number3,'Heavy Sauce on pasta')

print('The ratio of pasta to water is') 
 
x = (input('Pounds of Pasta: '))
y = (input('cups of water: '))
sum=int(x)/int(y)
print(sum, 'Correct Ratio')

print('rating 1-3 what sauce do you like')
x = input('Red Sauce : ')
y = input('White Sauce : ')
z = input('Butter : ')
float=int(x) + int(y) + int(z)
print(float,'Good Choices')

print('how do you like your pasta cooked rating 1-3')
x = input('baked : ')
y = input('boiled : ')
z = input('in soup : ')
sum=(int(x) + int(y) + int(z))/3
if sum < 1:
    print(sum,'baked')
if sum == 1:
    print(sum,'boiled')
if sum > 1:
    print(sum,'in soup')

print("the variety of pasta")
x = input('How many sauces do you like: ')
y = input('how many pasta noodles do you like: ')
sum=int(x) * int(y) 
print(sum, 'combinations of dishes')

print("How many days you can have pasta")
x = min(1, 2, 3, 4, 5, 6, 7)
y = max(1, 2, 3, 4, 5, 6, 7)
print('About:', x, '-', y,  'days a week')

