def main(argv):
    num_args = len(argv)
    
    # Print number of arguments and whether it's singular or plural
    if num_args == 0:
        print(f"Number of argument(s).")
        print(".")
    else:
        print(f"Number of argument{'s' if num_args > 1 else ''}: {num_args}")
        print(":")
        
        # Print each argument with its position
        for i in range(num_args):
            print(f"{i + 1}: {argv[i]}")
    
if __name__ == "__main__":
    # Call main function with command-line arguments excluding script name
    main(sys.argv[1:])
