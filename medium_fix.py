""" Filter numbers up to a maximum number. This code is still buggy ...
"""

def filter_entries(numbers, max_number):
    # deleting items from a list which is currently iterated on
    # is almost always a bad idea
    #for i in range(0, len(numbers)):
    #    if numbers[i] > max_number:
    #        del numbers[i]

    # fixed: use list comprehension for easy list filtering
    return [ n for n in numbers if n < max_number ]


def main():

    all_numbers = [1,23,4,43,2,9,34,2]
    low_numbers = filter_entries(all_numbers, 10)
    print ("Filtered Numbers are: {}".format(low_numbers))


if __name__ == "__main__":
    main()

