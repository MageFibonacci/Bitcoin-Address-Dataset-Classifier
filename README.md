
# Bitcoin Address Dataset Classifier

A Python script for classifying Bitcoin addresses from large datasets into separate files based on their type (Legacy, P2SH, SegWit, Taproot, and Scrypt). The script supports processing files with millions of rows and maintains the order of the original file.

## Features

- **Supports large datasets**: Processes files line by line to handle large inputs without consuming excessive memory.
- **Address types**:
  - **Legacy** (`1` prefix)
  - **P2SH** (`3` prefix)
  - **SegWit** (`bc1` prefix)
  - **Taproot** (`bc1p` prefix)
  - **Scrypt** (`L` or `M` prefixes, e.g., Litecoin addresses)
- **Input flexibility**:
  - Simple address files.
  - Address files with additional columns (e.g., balance).
- **Maintains input order**: The output files preserve the original order of the addresses.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bitcoin-address-classifier.git
   cd bitcoin-address-classifier
   ```

2. Ensure Python is installed on your system.

## Usage

### Input File

The script can process two types of input files:
1. A simple list of addresses:
   ```
   34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo
   3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
   bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
   ```

2. A file with multiple columns (e.g., `address balance`):
   ```
   address balance
   34xp4vRoCGJym3xR7yCVPFHoCNxR4Twseo 24859753472514
   3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy 1234567890
   bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh 987654321
   ```

### Running the Script

1. Place your input file in the repository folder and update the `input_file` variable in the script with the file name.

2. If your file includes additional columns (e.g., balances), set the `has_balance` flag to `True` in the script:
   ```python
   has_balance = True
   ```

3. Run the script:
   ```bash
   python classify_addresses.py
   ```

4. The script will generate the following output files:
   - `legacy.txt`: Legacy addresses (starting with `1`).
   - `p2sh.txt`: P2SH addresses (starting with `3`).
   - `segwit.txt`: SegWit addresses (starting with `bc1`).
   - `taproot.txt`: Taproot addresses (starting with `bc1p`).
   - `scrypt.txt`: Scrypt-based addresses (e.g., Litecoin, starting with `L` or `M`).

### Example Output

For the following input:
```
address balance
34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo 24859753472514
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy 1234567890
bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh 987654321
```

The script will create:
- `legacy.txt`:
  ```
  34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo
  ```
- `p2sh.txt`:
  ```
  3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
  ```
- `segwit.txt`:
  ```
  bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
  ```

## Customization

You can customize the script to handle additional address types or specific formats by modifying the `classify_address` function.


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.
