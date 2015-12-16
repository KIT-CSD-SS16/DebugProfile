"""
Compute the density over a range of x and y coordinates. But somehow the algorithm does not actual do the bin splitting
and termination properly ...
"""

minimum_bin_size = 0.1

def density_compute( bin_center, bin_size, density_funct ):
    if bin_size == minimum_bin_size:
        # split bin in four smaller ones
        return density_compute( ( bin_center[0] - bin_size * 0.25, bin_center[1] + bin_size * 0.25 ), bin_size * 0.5, density_funct ) + \
        density_compute( ( bin_center[0] + bin_size * 0.25, bin_center[1] - bin_size * 0.25 ), bin_size * 0.5, density_funct ) + \
        density_compute( ( bin_center[0] + bin_size * 0.25, bin_center[1] + bin_size * 0.25 ), bin_size, density_funct ) + \
        density_compute( ( bin_center[0] - bin_size * 0.25, bin_center[1] - bin_size * 0.25 ), bin_size, density_funct )
    else:
        # deep enough compute density here
        return [( bin_center[0], bin_center[1], density_funct( bin_center[0], bin_center[1]))]

def main():

    density_funct = lambda x,y: 0.5 * x + 0.1 * y

    density_res = density_compute( (5.0, 5.0), 26.0, density_funct )
    print ("Density result contains " + str(len(density_res)) + " computations")


if __name__ == "__main__":
    main()

