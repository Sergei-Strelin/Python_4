def convert(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)     
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result


print("Исходные параметры: first='один', second=2, third=3, fourth='четыре', fifth=[5, 6]")
print("Результат: " + str(convert(first="один", second=2, third=3, fourth="четыре", fifth=[5, 6])))