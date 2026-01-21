import os
import json
import pandas as pd
from ..utils.copy_file import copy_file_to_dest
from ..utils.compile_code import compile
from ..utils.get_file_extension import get_file_ext
from ..utils.run_code import run
from ..utils.check_answer import check_answer

working_room_path = './cache/workroom'
input_file = f"{working_room_path}/input.inp"
output_file = f"{working_room_path}/output.out"
answer_file = f"{working_room_path}/answer.ans"

def start():
    try:
        data = {}
        result = {}

        print("Reading contest configuration...")
        with open('./cache/config.json', 'r') as config_file:
            data = json.load(config_file)
        print("Successfully read contest infomation")

        contestants = data['contestants']
        testdata = data['testdata']

        for contestant_name, contestant in contestants.items():
            if (not contestant['enabled']):
                continue

            for problem_name, submission_source in contestant['submissions'].items():
                if (not testdata[problem_name]['enabled']):
                    continue

                file_ext = get_file_ext(submission_source)
                dest_file = f"{working_room_path}/{problem_name}{file_ext}"

                copy_file_to_dest(submission_source, dest_file)

                compiled_file = f"{working_room_path}/{problem_name}"
                compile_exit_code = compile(file_ext, dest_file, compiled_file)

                if (compile_exit_code != 0):
                    continue

                problem_data = testdata[problem_name]
                point_count = 0
                total_point = 0
                for test in problem_data['testcase']:
                    copy_file_to_dest(test['input'], input_file)
                    copy_file_to_dest(test['output'], answer_file)

                    run_exit_code = run(file_ext, compiled_file, input_file, output_file)

                    is_correct = check_answer(output_file, answer_file)

                    if (is_correct):
                        if (problem_data['equal_point']):
                            point_count += 1
                        else:
                            point_count += test['point']
                    total_point += 1

                if (not problem_name in  result):
                    result[problem_name] = {}
                if (problem_data['equal_point']):
                    result[problem_name][contestant_name] = f"{(problem_data['point'] * point_count / total_point):.2f}"
                else:
                    result[problem_name][contestant_name] = f"{(point_count):.2f}"

        try:
            result_df = pd.DataFrame(result)
            result_df.to_csv("./result.csv")
        except Exception as e:
            print(e)
            print('Failed while writing result to "./result.csv"')

    except Exception as e:
        print(e)
        print('Error while writing information to "./cache/config.json"')

