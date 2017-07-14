# Binary search
import SOA, sys

target = int(raw_input('Enter target number: '))

def chooseArray():

    while True:
        # I want the user to choose the array
        choice = raw_input('Choose array (odd, even, prime or normal):')
        if choice == 'prime':
            max_number = int(raw_input('Enter max number: '))
            array_range = SOA.sieveOfAtkin(max_number)
            return array_range
            break
        elif choice == 'even':
            max_number = int(raw_input('Enter max number: '))
            array_range = range(2, max_number,2)
            return array_range
            break
            #print array_range
        elif choice == 'odd':
            max_number = int(raw_input('Enter max number: '))
            array_range = range(1, max_number,2)
            return array_range
            break
             #print array_range
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

#if __name__ == '__main__':
    #chooseArray()


def binarySearch():

    # array was chosen by user
    array_range = chooseArray()

    # set the indexes:
    min_number = 0;
    #print min_number
    max_number = len(array_range) - 1
    #print max_number


    while min_number <= max_number:

        # guess the avarage. It's necessary to know the mid point to "divide and conquer!"
        guess = (max_number + min_number)/2

        print'Guess: ', array_range[guess]

        # check if guessed number  = target


        if array_range[guess] == target:
            print 'Found it! :D'
            return array_range[guess]



        if array_range[guess] < target:
            min_number = guess + 1
            #print 'min', min_number


        else:
            max_number = guess - 1
            #print 'max', max_number

    print 'Chosen target not in array. :('
    return -1   # would return - 1 if min_number > max_number


if __name__ == '__main__':
    binarySearch()
