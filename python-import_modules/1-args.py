from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  
    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args), end="")
    print(":", end="\n" if num_args > 0 else ".")

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
        