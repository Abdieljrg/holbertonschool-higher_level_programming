def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(int(item)), end="")
                count += 1
            except (ValueError, TypeError):
                pass
        print()
        return count
    except TypeError:
        raise Exception("Invalid input: my_list must be a list")