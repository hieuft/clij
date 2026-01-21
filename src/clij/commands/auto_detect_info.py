import json
from pathlib import Path

def get_number(s: str) -> int:
    ret = 0
    for x in s:
        if (x.isdigit()):
            ret = ret * 10 + int(x)
    return ret

def get_file_name_without_extension(file_name: str) -> str:
    return file_name.split('.')[0]

def get_valid_submission_name(file_name_without_ext: str, problem_name_list: list) -> str:
    for name in problem_name_list:
        if (name.lower() == file_name_without_ext.lower()):
            return name
    return ""

def get_contestant_submissions_data(path: str, problem_name_list: list) -> object:
    contestant_path = Path(path)

    contestant_data = {
        'enabled': True
    }
    
    submissions = {}
    for sub in contestant_path.iterdir():
        if (sub.is_file()):
            valid_submission_name = get_valid_submission_name(get_file_name_without_extension(sub.name), problem_name_list)
            if (len(valid_submission_name)):
                submissions[valid_submission_name] = './' + str(sub)

    contestant_data['submissions'] = submissions

    return contestant_data

def get_problem_tests_data(path: str) -> list:
    problem_path = Path(path)

    problem_data = {
        'enabled': True,
        'point': 10,
        'equal_point': True,
    }

    test_list = []
    for test in problem_path.iterdir():
        if (test.is_dir()):
            # print(test)
            input_file = ""
            output_file = ""
            for file in test.iterdir():
                if (".i" in file.suffix):
                    input_file = file 
                elif (".o" in file.suffix):
                    output_file = file 
            # print(input_file, output_file)

            test_list.append({
                'name': test.name,
                'point': 1,
                'input': './' + str(input_file),
                'output': './' + str(output_file)
            })

    test_list = sorted(test_list, key = lambda x: get_number(x['name']))

    problem_data['testcase'] = test_list

    return problem_data

def get_contestants_info(problem_name_list: list) -> object:
    contestants_path = Path("./contest/contestants")

    contestant_name_list = []
    contestant_data = {}

    for folder in contestants_path.iterdir():
        if (folder.is_dir()):
            contestant_name_list.append(folder.name)
            contestant_data[folder.name] = get_contestant_submissions_data(folder, problem_name_list)

    return contestant_data, contestant_name_list


def get_testdata_info() -> object:
    testcases_path = Path("./contest/testcases")

    problem_name_list = []
    test_data = {}

    for folder in testcases_path.iterdir():
        if (folder.is_dir()):
            problem_name_list.append(folder.name)
            test_data[folder.name] = get_problem_tests_data(folder)

    return test_data, problem_name_list

def auto_detect_info():
    """
    Auto detect contest infomation.
    Check "./cache/config.json" for contest configuration.
    """

    try:
        print("Detecting contest infomation...")

        test_data, problem_name_list = get_testdata_info()
        contestant_data, contestant_name_list = get_contestants_info(problem_name_list)

        configuration = {
            'contestants': contestant_data,
            'testdata': test_data
        }

        try:
            with open('./cache/config.json', 'w') as config_file:
                json.dump(configuration, config_file, indent = 2)

            print("Successfully detected contest infomation")
            print('Please visit "./cache/config.json" to config the contest and make sure all file paths are correct.')
        except:
            print('Error while writing information to "./cache/config.json"')

    except:
        print("Error while detecting contest information!")


