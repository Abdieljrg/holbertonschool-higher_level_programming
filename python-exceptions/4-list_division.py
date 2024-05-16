#1/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i] if i < len(my_list_1) else 0
            y = my_list_2[i] if i < len(my_list_2) else 0
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                try:
                    division = x / y
                    result.append(division)
                except Exception:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("wrong type")
        except Exception:
            print("out of range")
    return result
