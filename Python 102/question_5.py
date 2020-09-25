def is_consecutive(a_list):
    next  = int()
    for number in a_list:
        if next:
            if number != next:
                return False
        next = number + 1
    return True

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [1, 10]

    print(is_consecutive(a))
    print(is_consecutive(b))
