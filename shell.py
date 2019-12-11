import Uzumaki

while True:
    text = input('basic > ')
    result, error = Uzumaki.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)