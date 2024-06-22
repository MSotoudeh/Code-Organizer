import os

def parse_input_file(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    file_structure = {}
    current_file = None
    for line in lines:
        line = line.strip()
        if line.startswith('/'):
            current_file = line[1:]
            file_structure[current_file] = []
        else:
            if current_file:
                file_structure[current_file].append(line)

    return file_structure

def create_files_and_directories(file_structure, base_path):
    for file_path, code_lines in file_structure.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write('\n'.join(code_lines))

def main():
    input_file_path = 'data/input_code.txt'
    base_path = 'output_repo'
    
    file_structure = parse_input_file(input_file_path)
    create_files_and_directories(file_structure, base_path)

if __name__ == "__main__":
    main()
