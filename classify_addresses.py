import re

# Configuration
input_file = "address-18-12-2024.tsv"  # Replace with your file
legacy_file = "legacy.txt"
p2sh_file = "p2sh.txt"
segwit_file = "segwit.txt"
taproot_file = "taproot.txt"
scrypt_file = "scrypt.txt"

# FLAG: Activate if the file includes columns (e.g. address balance)
has_balance = True  # Set to True if the file has "address balance", otherwise False

# Function to classify addresses
def classify_address(address):
    if address.startswith('1'):
        return 'legacy'
    elif address.startswith('3'):
        return 'p2sh'
    elif address.startswith('bc1p'):
        return 'taproot'
    elif address.startswith('bc1'):
        return 'segwit'
    elif re.match(r'^[LM]', address):
        return 'scrypt'
    else:
        return 'unknown'

# Opening output file
with open(input_file, 'r') as infile, \
     open(legacy_file, 'w') as legacy, \
     open(p2sh_file, 'w') as p2sh, \
     open(segwit_file, 'w') as segwit, \
     open(taproot_file, 'w') as taproot, \
     open(scrypt_file, 'w') as scrypt:

    for line in infile:
        # Address extraction
        if has_balance:
            try:
                address = line.strip().split()[0]  # Only take the first column
            except IndexError:
                continue  # Skip invalid lines
        else:
            address = line.strip()

        # Classify and write the address to the appropriate file
        category = classify_address(address)
        if category == 'legacy':
            legacy.write(address + '\n')
        elif category == 'p2sh':
            p2sh.write(address + '\n')
        elif category == 'segwit':
            segwit.write(address + '\n')
        elif category == 'taproot':
            taproot.write(address + '\n')
        elif category == 'scrypt':
            scrypt.write(address + '\n')
