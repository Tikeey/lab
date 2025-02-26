text = input("Введите текст: ")

rev_text = ''.join(reversed(text))

if text == rev_text:

    print(True)

else:
    
    print(False)
