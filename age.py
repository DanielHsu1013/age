age = input('how old are you?')
driving = input('have you drive before?')
age = int(age)

if age >= 18 and driving == 'yes':
	print('well done')
elif age >= 18 and driving == 'no':
	print('why dont you get a lience?')
elif age < 18 and driving == 'yes':
    print('you sould not drive')
else:
	print('you can have your driving lesson at 18')

