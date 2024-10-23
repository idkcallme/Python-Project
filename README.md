# Python-Project

This Python project is a simple command-line tool for generating and comparing file hash values. It was created for educational purposes as a Python project to demonstrate the use of the `hashlib` library, file I/O operations, command-line argument parsing, and error handling. 

**This project is intended for learning and experimentation.** While it functions as a basic file hashing tool, it may not be suitable for production environments or security-critical applications.

## Features

* **Generate Hashes:** Calculate hash values for files using different algorithms.
* **Save Hashes:** Store generated hashes in a JSON file ("hashes.json") for future reference.
* **Compare Hashes:** Compare the hash of a file with a previously stored hash to check for modifications.
* **Command-line Interface:** Easy-to-use command-line interface with clear arguments.
* **Error Handling:** Includes error handling for invalid file paths, unsupported algorithms, and missing hash entries.

## Installation

1.  **Clone or download this repository:**
    ```bash
    git clone <repository_url> 
    ```
    Or download the files directly.

2.  **Make sure you have Python 3.6 or later installed.** You can check your Python version by running:
    ```bash
    python --version
    ```

## Usage

1.  **Open a terminal or command prompt.**
2.  **Navigate to the directory where you saved the script.**
    ```bash
    cd <directory_path>
    ```
3.  **Run the script using the following command:**

    ```bash
    python hashstash.py <file_path> [options]
    ```

    Replace `<file_path>` with the actual path to the file you want to hash.

### Options

*   `-a` or `--algorithm`: Specifies the hashing algorithm to use. Defaults to "sha256". Choose from available algorithms (see below).
*   `-s` or `--save`: Saves the generated hash to "hashes.json".
*   `-c` or `--compare`: Compares the generated hash to a stored hash in "hashes.json".

### Examples

*   **Generate a SHA256 hash for "my_document.txt" and print it to the console:**

    ```bash
    python hashstash.py my_document.txt
    ```

*   **Generate a SHA1 hash for "image.jpg" and save it to "hashes.json":**

    ```bash
    python hashstash.py image.jpg -a sha1 -s 
    ```

*   **Compare the hash of "my_document.txt" to the stored hash:**

    ```bash
    python hashstash.py my_document.txt -c
    ```

## Available Hashing Algorithms

This tool supports various hashing algorithms available in your Python environment. Some common ones include:

*   `sha256` (default)
*   `sha1`
*   `md5`
*   `sha512`
*   `blake2b`
*   `sha3_256`

To see a full list of supported algorithms, run:

```bash
python -c "import hashlib; print(hashlib.algorithms_available)"
