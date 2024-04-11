# P72PermutasiZigZag.py : program utk menghitung permutasi zig zag.
# Ridhan Fadhilah, 12-04-2024

# Initialize arrays and variables
catat = [0] * 10
pernah = [0] * 10
bil = 0
cek = 0

def tulis(kedalaman):
    """Recursive function to write values."""
    global cek

    if kedalaman > bil:
        cek = cek_array()
        if cek:
            # Print the results if the condition is met
            for i in range(1, bil + 1):
                print(catat[i], end="")
            print()
    else:
        # Try each possibility from 1 to bil
        for i in range(1, bil + 1):
            if not pernah[i]:
                pernah[i] = 1
                catat[kedalaman] = i
                # Recursive call
                tulis(kedalaman + 1)
                # Reset the tracking list
                pernah[i] = 0

def cek_array():
    """Function to check the condition in the array."""
    for i in range(2, bil):
        # Check the given condition
        if ((catat[i - 1] < catat[i] and catat[i] > catat[i + 1]) or
            (catat[i - 1] > catat[i] and catat[i] < catat[i + 1])):
            continue
        else:
            return 0  # Condition not met, return 0
    
    return 1  # All conditions met, return 1

def main():
    global bil

    # Read input from user
    bil = int(input())
    
    # Initialize pernah array to zeros
    for i in range(1, bil + 1):
        pernah[i] = 0
    
    # Call the recursive function starting from depth 1
    tulis(1)

if __name__ == "__main__":
    main()
