##1
my_string = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
            "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
            "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
            "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
            " a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych," \
            " jak Aldus PageMaker"
name = list("michal")
surname = list("salej")
n = s = 0

for x in my_string:
    if x == name[2]:
        n += 1
    if x == surname[3]:
        s += 1

print(f"W tekście jest {n} liter {name[2]}... oraz {s} liter {surname[3]}...")

# 4
# print(dir("epepep"))
# help("epepep".split())

# 5
name_surname = "Michał Salej"
name_surname_reversed = name_surname[::-1]
print(name_surname_reversed)

# 6
l = [x for x in range(1, 11)]
l2 = [x for x in range(1, 11) if x > 5]
l = [x for x in range(1, 11) if x <= 5]
print(l, l2)
# 7
l3 = [0, *l, *l2]
print(l3)
print(sorted(l3, reverse=True))

# 8
tuple_list = [(140222, "Adam Kawał"), (100221, "Mati Piasek"), (100522, "Ela Kotler")]
print(tuple_list)

# 9
dict_of_tuple_list = dict(tuple_list)

# 10
numbers = [222222222, 10101010, 12222222, 222222222, 10101010, 34534348235, 34567345345345]
numbers = set(numbers)
print(numbers)

# 11
l55 = []
for x in range(1, 11):
    l55.append(x)
print(l55)
# 12
l66 = []
for x in reversed(range(20, 101, 5)):
    print(x)
    l66.append(x)
print(l66)

# 13
list_dicts = [{"epe": 1, "ebe": "kurs"}, {"lolek": 5, "bolek": 10}, {"eee": 1, 2: "elewacja"}]
final_string = ""
for x in list_dicts:
    for y in x.keys():
        final_string += str(x[y]) + " "
print(final_string)
