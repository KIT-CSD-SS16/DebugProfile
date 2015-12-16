

def internal_function( val ):
    print ("internal_function entered with val = {}".format(val))
    new_val = val + 1
    return new_val

def main():
    print ("main() entered")
    first_val = 10
    added_val = internal_function( first_val )
    added_val = internal_function( added_val )
    print ("added_val = {}".format(added_val))


if __name__ == "__main__":
    # execute only if run as a script
    main()

