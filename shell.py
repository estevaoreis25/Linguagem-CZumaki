import Uzumaki

while True:
		text = input('Uzumaki > ')
		result, error = Uzumaki.run('<stdin>', text)

		if error: print(error.as_string())
		elif result: print(result)