"""Module with helping text parsing"""

from typing import List, Dict


def parse_exp_help_text(filepath: str) -> Dict[str, List[str]]:
    with open(filepath, mode='r') as file:
        exp_names_list = file.readlines()

        exp_names_list = [curr_exp.strip() for curr_exp in exp_names_list]

    exp_lengths_list = iter(['no exp', '1+', '2+',
                             '3+', '4+', '5+',
                             '6+', '8+', '10+'])

    exp_dict = dict()
    idx_prev = 0
    for idx, curr_exp in enumerate(exp_names_list):
        if curr_exp == '---' or idx == len(exp_names_list) - 1:

            try:
                curr_edu_name = next(exp_lengths_list)
            except StopIteration:
                break

            if idx == len(exp_names_list) - 1:
                exp_dict[curr_edu_name] = exp_names_list[idx_prev:]
            else:
                exp_dict[curr_edu_name] = exp_names_list[idx_prev:idx]

            idx_prev = idx + 1

    return exp_dict


def parse_edu_help_text(filepath: str) -> Dict[str, List[str]]:
    with open(filepath, mode='r') as file:
        edu_names_list = file.readlines()

        edu_names_list = [curr_edu.strip() for curr_edu in edu_names_list]

    edu_types_list = iter(['bachelor+',
                           'magister+'])

    edu_dict = dict()
    idx_prev = 0
    for idx, curr_exp in enumerate(edu_names_list):
        if curr_exp == '---' or idx == len(edu_names_list) - 1:

            try:
                curr_edu_name = next(edu_types_list)
            except StopIteration:
                break

            if idx == len(edu_names_list) - 1:
                edu_dict[curr_edu_name] = edu_names_list[idx_prev:]
            else:
                edu_dict[curr_edu_name] = edu_names_list[idx_prev:idx]

            idx_prev = idx + 1

    return edu_dict


