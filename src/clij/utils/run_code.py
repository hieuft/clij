import os 

def run(file_type: str, source: str, input: str, output: str) -> int:
    if (file_type == '.cpp'):
        exit_code = os.system(f"timeout 1s {source} < {input} > {output}")

        return exit_code
    else:
        exit_code = os.system(f"timeout 1s python {source} < {input} > {output}")

        return exit_code
