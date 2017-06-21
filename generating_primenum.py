def gen_prime():
    """
    Function that generates prime numbers.

    Returns:
        List of prime numbers

    Raises:
        ValueError: asks the user for input until a valid integer is entered. Allows CTRL+C.
    """

    while True:
        try:
            max_number = int(raw_input('Enter max number: '))
            break
        except ValueError:
            print 'Not a number, please try again. Or CTRL+C to quit.'
            continue

    range_num = range(2, max_number)

    # 1
    multiply_a = [number for number in range_num]
    multiply_b = [number for number in range_num]


    # 2
    multiply_all = [i*j for i in multiply_a for j in multiply_b ]
    # 2 removing numbers bigger than my max_number
    multiply_all = [number for number in multiply_all if number <= max_number]

    # 3
    prime_numbers = [number for number in range_num if number not in multiply_all]
    prime_numbers = [int(i) for i in prime_numbers]

    return prime_numbers

if __name__ == '__main__':
    gen_prime()