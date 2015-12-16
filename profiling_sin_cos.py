"""
Precompute a sin-cos table. can this be made faster ?
"""

def compute_sin_cos(angle):
    import math
    return math.sin(angle), math.cos(angle)

def main():

    size_lookup = 100000
    angles = [ (x / size_lookup) * 3.0 for x in range(size_lookup) ]
    #print(angles)
    precomputed = [ compute_sin_cos(angle) for angle in angles]
    print ("Precomputed {} angles".format(len(precomputed)))


if __name__ == "__main__":
    main()

