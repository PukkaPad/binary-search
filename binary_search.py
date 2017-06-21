# Binary search
import generating_primenum, sys

target = int(raw_input('Enter target number: '))

def chooseArray():
    """
    This function will request user to chose the type of data and it will return a list that contains the data chosen.

    """

    while True:
        choice = raw_input('Choose array (odd, even, prime or normal):')
        if choice == 'prime':
            array_range = generating_primenum.gen_prime()
            return array_range
            break
        elif choice == 'even':
            max_number = int(raw_input('Enter max number: '))
            array_range = range(2, max_number,2)
            return array_range
            break
        elif choice == 'odd':
            max_number = int(raw_input('Enter max number: '))
            array_range = range(1, max_number,2)
            return array_range
            break
        elif choice == 'normal':
            max_number = int(raw_input('Enter max number: '))
            min_number = int(raw_input('Do you want to start with 0 or 1? '))
            if min_number == 0:
                array_range = range(0, max_number)
            else:
                array_range = range (1,max_number)
            return array_range
            break
        else:
            break
            print 'Well done'

def binarySearch():
    """
    This function finds the target by 'divide and conquer' method. It will repeatedly divide the list until the target is found. It will compare the target value to the middle element. If unequal, the algorithm will look either at the top or bottom half of the list.

    Returns:
        It will return each guess until it finds the target.

    To do:
        Raise exceptions
    """


    # array was chosen by user
    array_range = chooseArray()

    # set the indexes:
    min_number = 0;
    max_number = len(array_range) - 1

    while min_number <= max_number:

        # passing some QA. If a prime array is chosen but user select a non prime number, I make sure there's a warning.
        if target not in array_range:
            print 'Chosen target not in array. :('
            break

        # guess the avarage. It's necessary to know the mid point to "divide and conquer!"
        guess = (max_number + min_number)/2
        print'Guess: ', array_range[guess]

        # check if guessed number  = target
        if array_range[guess] == target:
            print 'Found it! :D'
            return array_range[guess]

        if array_range[guess] < target:
            min_number = guess + 1

        else:
            max_number = guess - 1


    return -1   # would return - 1 if min_number > max_number


if __name__ == '__main__':
    binarySearch()
