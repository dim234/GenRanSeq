a = "DNA"
b = "RNA"

# Prompt the user for input
sequence_type = input("DNA or RNA? ")

# Determine the bases based on the user's input
if sequence_type == a:
    bases = ['A', 'T', 'G', 'C']
elif sequence_type == b:
    bases = ['A', 'U', 'G', 'C']
else:
    print("Invalid input! Please enter 'DNA' or 'RNA'.")
    exit()  # Exit the program if the input is invalid

# Prompt the user for the sequence length
length = int(input("Length: "))

from random import choice

# Generate the sequence
sequence = ''
for i in range(length):
    base = choice(bases)
    sequence += base

# Print the generated sequence
print(sequence)
