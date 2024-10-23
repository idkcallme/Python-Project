import argparse
import hashlib
import json
import os

def generate_hash(file_path, algorithm="sha256"):
    """Generates the hash of a file."""
    hasher = hashlib.new(algorithm)
    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)  # Read in chunks
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except IOError:
        print(f"Error: Could not read file - {file_path}")
        return None

def save_hash(file_path, hash_value, algorithm, hashes_file="hashes.json"):
    """Saves the hash to a JSON file."""
    try:
        with open(hashes_file, "r+") as file:
            data = json.load(file)
            data[file_path] = {"algorithm": algorithm, "hash": hash_value}
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(hashes_file, "w") as file:
            data = {file_path: {"algorithm": algorithm, "hash": hash_value}}
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {hashes_file}")

def compare_hash(file_path, algorithm="sha256", hashes_file="hashes.json"):
    """Compares the hash of a file to a stored hash."""
    try:
        with open(hashes_file, "r") as file:
            data = json.load(file)
            if file_path in data:
                stored_hash = data[file_path]["hash"]
                stored_algorithm = data[file_path]["algorithm"]
                if algorithm == stored_algorithm:
                    generated_hash = generate_hash(file_path, algorithm)
                    if generated_hash == stored_hash:
                        print("Match")
                    else:
                        print("Mismatch")
                else:
                    print(f"Error: Different algorithm used for stored hash. "
                          f"Stored: {stored_algorithm}, Provided: {algorithm}")
            else:
                print(f"Error: No stored hash found for {file_path}")
    except FileNotFoundError:
        print(f"Error: Hashes file not found - {hashes_file}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {hashes_file}")

def main():
    parser = argparse.ArgumentParser(description="File Hashing Tool")
    parser.add_argument("file_path", help="Path to the file")
    parser.add_argument("-a", "--algorithm", default="sha256", 
                        choices=hashlib.algorithms_available,
                        help="Hashing algorithm to use")
    parser.add_argument("-s", "--save", action="store_true", 
                        help="Save hash to hashes.json")
    parser.add_argument("-c", "--compare", action="store_true", 
                        help="Compare generated hash to stored hash")
    args = parser.parse_args()

    if args.compare:
        compare_hash(args.file_path, args.algorithm)
    else:
        hash_value = generate_hash(args.file_path, args.algorithm)
        if hash_value:
            print(f"Hash ({args.algorithm}): {hash_value}")
            if args.save:
                save_hash(args.file_path, hash_value, args.algorithm)

if __name__ == "__main__":
    main()
