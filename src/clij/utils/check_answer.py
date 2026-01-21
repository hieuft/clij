import os 

def check_answer(output: str, answer: str) -> boolean:
    exit_code = os.system(f"diff -q -w -B {output} {answer} &>/dev/null")
    if (exit_code):
        return False
    return True
