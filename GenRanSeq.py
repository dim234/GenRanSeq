from random import choice

a = "DNA"
b = "RNA"

# Prompt the user for input
sequence_type = input("DNA or RNA? ")

# Determine the bases and their complements based on the user's input
if sequence_type == a:
    bases = ['A', 'T', 'G', 'C']
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
elif sequence_type == b:
    bases = ['A', 'U', 'G', 'C']
    complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
else:
    print("Invalid input! Please enter 'DNA' or 'RNA'.")
    exit()  # Exit the program if the input is invalid

single = "single"
double = "double"

# Determine how many strands the molecule has
chain = input("Single or double stranded? ")

if chain == single:
    # Prompt the user for the sequence length
    length = int(input("Length (in bases): "))

    # Generate the sequence
    sequence = ''
    for i in range(length):
        base = choice(bases)
        sequence += base

    # Print the generated sequence
    print(sequence)
    
elif chain == double:
    # Prompt the user for the sequence length
    length = int(input("Length (in bases): "))

    # Generate the first sequence
    first_sequence = ''
    for i in range(length):
        base = choice(bases)
        first_sequence += base
    
    # Generate the second (complementary) sequence
    second_sequence = ''
    for base in first_sequence:
        second_sequence += complement[base]
    
    # Print the generated sequences with alignment
    print("Main Sequence:        ", first_sequence)
    print("Complementary Sequence:", second_sequence)
else:
    print("Invalid input! Please enter 'single' or 'double'.")
    exit()  # Exit the program if the input is invalid
