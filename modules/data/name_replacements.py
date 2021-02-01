"""Module with name replacements for pandas dataframe columns"""


import math
from typing import List, Dict


def replace_cert(cert_name: str, certificates: List[str]) -> str:
    for curr_no_cert in certificates:
        if curr_no_cert in cert_name:
            return 'no'

    return 'yes'


def replace_npa(npa_name: str, npa_list: List[str]) -> str:
    for curr_no_npa in npa_list:
        if curr_no_npa in npa_name:
            return 'no'

    return 'yes'


def replace_eng(eng_level, no_info_english: List[str], tech_documentation: List[str]) -> str:
    if isinstance(eng_level, float):
        if math.isnan(eng_level):
            return 'no info'

    eng_level = eng_level.strip()

    for curr_no_info in no_info_english:
        if curr_no_info in eng_level:
            return 'no info'

    for curr_tech_doc in tech_documentation:
        if curr_tech_doc in eng_level:
            return 'for technical documentation'

    if eng_level == 'C1':
        return 'С1'

    if eng_level == 'C2':
        return 'С2'

    if eng_level == 'B2':
        return 'В2'

    if eng_level == 'B1':
        return 'В1'

    return eng_level


def replace_working(working_name: str, working_whole_type: List[str]) -> str:
    for curr_whole in working_whole_type:
        if curr_whole in working_name:
            return 'Полная ставка'

    return working_name


def replace_tech(npa_name: str, npa_lists: List[str]) -> str:
    for curr_no_npa in npa_lists:
        if curr_no_npa in npa_name:
            return 'no'

    return 'yes'


def replace_experience(exp_name: str, exp_dict: Dict[str, List[str]]) -> str:
    for new_name, curr_experience_names_list in exp_dict.items():
        for curr_name in curr_experience_names_list:
            if curr_name in exp_name:
                return new_name

    return 'no info'


def replace_education(edu_name: str, edu_dict: Dict[str, List[str]]) -> str:
    for new_name, curr_edu_names_list in edu_dict.items():
        for curr_name in curr_edu_names_list:
            if curr_name in edu_name:
                return new_name

    return 'no info'
