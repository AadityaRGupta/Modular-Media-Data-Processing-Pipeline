import sys
from orchestrator.interface import initiate
import json

def main():
    if len(sys.argv) < 2:
        print("Processing: Python interface.py <file_path>")
        return
    
    input_file_path = sys.argv[1] # takes the first argument
    output_file = initiate(input_file_path) # runs the interface

    output_in_json = "outputs/output.json" # outputs the result
    with open(output_in_json, "w") as process:
        json.dump(output_file, process, indent=4)

        print("Output saved in:", output_in_json)

if __name__ == "__main__":
    main() # runs the main function