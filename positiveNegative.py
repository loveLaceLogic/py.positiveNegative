# Program to decide if a number is positive, negative, or zero
print('Enter number: ')
number = input()
number = int(number)
if number < 0:
  print('Your number is negative.')
elif number > 0:
  print('Your number is positive.')
else:
  print('Your number is zero.')