def my_function(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Koteł"
print(my_function(data_text))
