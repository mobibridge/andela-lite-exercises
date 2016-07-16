def fizzbuzz(number):
	if number%3==0:
		return 'fizz'
	elif number%5==0:
		return "buzz"
	elif number%3==0 and number%5==0:
		return 'fizzbuzz'
	else:
		return (number)

fizzbuzz(5)