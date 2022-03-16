while True:
    try:
        my_list = [10, 45, 67, 3, 98]
        a = input("Enter a: ")
        b = input("Enter b: ")
        print(my_list[int(a) // int(b)])
        break
    except IndexError:
        print("There is an IndexError.\n")
        print("Please try again.")
    except ValueError:
        print("There is a ValueError.\n")
        print("Please try again.")
    except ZeroDivisionError:
        print("There is a ZeroDivisionError.\n")
        print("Please try again.")
