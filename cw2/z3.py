def my_function(text, letter):
    return text.lower().replace(letter.lower(), "")


text = "Ala ma kota"
letter = "K"
print(my_function(text, letter))
