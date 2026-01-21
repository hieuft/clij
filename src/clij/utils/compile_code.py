import os 

def compile(file_type: str, source: str, dest: str):
    if (file_type == '.cpp'):
        exit_code = os.system(f"g++ {source} -o {dest}")
        return exit_code
    elif (file_type == 'py'):
        return 0
