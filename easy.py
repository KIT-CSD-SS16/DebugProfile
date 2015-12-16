""" Combine the first and last names to combinations. For some obscure reason,
    this code is not working.
"""

def create_name_list(first_names, last_names):
    combined_names = []
    for j in range(0, len(first_names)):
        for i in range(0, len(last_names)):
            combined_names.append("{} {}".format(first_names[i], last_names[j]))
    return combined_names


def main():
    first_names = ["Thomas", "Franzi", "Oliver"]
    last_names= ["Hauck", "Maier", "Merkel", "Laus"]

    combined_names = create_name_list(first_names, last_names)
    print ("Combined Names: {}".format(combined_names))


if __name__ == "__main__":
    main()

