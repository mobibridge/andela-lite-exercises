def number_to_words(number):
	words = []
	num2words = {
		'1': 'one',
		'2': 'two'
	}
	for i in str(number):
		words.append(num2words[i])

	return " ".join(words)

print(number_to_words(1211))


#list comprehensions
words = [num2words[i] for i in str(number)]