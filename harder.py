
"""
This script organizes families according to the city they live in, but there
still is a problem with the correct organization
"""

class NameContainer:
    def __init__(self):
        self.names = []

    def add_name(self, first_name, last_name):
        self.names.append((first_name, last_name))

    def count_names(self):
        return len(self.names)

    def get_names(self):
        return self.names

class FamilyContainer():

    def __init__(self, city, names = NameContainer()):
        self.city = city
        self.names = names

    def add_family_member(self, first_name, last_name):
        self.names.add_name(first_name, last_name)

    def __str__(self):
        if len(self.names.get_names()) == 0:
            return  ""
        else:
            return "".join([ "{} {}, ".format( name[0], name[1] ) for name in self.names.get_names()])[:-2]

def main():

    maierFamily = FamilyContainer("Berlin")
    maierFamily.add_family_member("Peter", "Maier")
    maierFamily.add_family_member("Gabi", "Maier")

    rauFamily = FamilyContainer("Bochum")
    rauFamily.add_family_member("Uli", "Rau")
    rauFamily.add_family_member("Frank", "Rau")

    schmidtFamily = FamilyContainer("Schmidt")
    schmidtFamily.add_family_member("Uschi", "Schmidt")
    schmidtFamily.add_family_member("Elke", "Schmidt")
    schmidtFamily.add_family_member("Gabi", "Schmidt")

    print ( "Maier Family: " + str(maierFamily))
    print ( "Rau Family: " + str(rauFamily))
    print ( "Schmidt Family: " + str(schmidtFamily))

if __name__ == "__main__":
    main()


