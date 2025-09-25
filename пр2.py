my_list = [12, 3, 7, 18, 25, 6, 42, 11, 9, 20,
           "яблуко", "груша", "ананас", "вишня", "персик",
           "банан", "слива", "киві", "малина", "абрикос"]

ints = [x for x in my_list if isinstance(x, int)]
strs = [x for x in my_list if isinstance(x, str)]
ints_sorted = sorted(ints)
strs_sorted = sorted(strs, key=lambda s: s.lower())
sorted_list = ints_sorted + strs_sorted
even_numbers = [x for x in ints_sorted if x % 2 == 0]
upper_strs = [s.upper() for s in strs_sorted]
print("Основний відсортований список:", sorted_list)
print("Список чисел, кратних 2:", even_numbers)
print("Список строк у CAPS:", upper_strs)
