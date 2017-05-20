# generating a list of prime numbers

# Quality Assurance (QA):
def gen_prime():
    while True:
        try:
            max_number = int(raw_input('Enter max number: '))
            break
        except ValueError:
            print 'Not a number, please try again. Or CTRL+C to quit.'
            continue

    range_num = range(2, max_number)
    multiply_a = [number for number in range_num]
    multiply_b = [number for number in range_num]
    
    multiply_all = [i*j for i in multiply_a for j in multiply_b ]
    multiply_all = [number for number in multiply_all if number <= max_number]
    
    prime_numbers = [number for number in range_num if number not in multiply_all]
    prime_numbers = [int(i) for i in prime_numbers]

    return prime_numbers

if __name__ == '__main__':         
    gen_prime()