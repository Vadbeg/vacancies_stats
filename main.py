from typing import List, Dict

import pandas as pd


from modules.data.data_loading import load_data
from modules.data.data_loading import get_aggregated_data
from modules.data.name_replacements import (replace_cert, replace_npa, replace_eng,
                                            replace_tech, replace_education,
                                            replace_working, replace_experience)
from modules.data.text_parsing import parse_exp_help_text, parse_edu_help_text
from modules.constants import (eu_countries, cis_countries,
                               certificates, no_info_english,
                               tech_documentation, working_whole_type,
                               npa_lists)
from config import Config


def load_data_on_country_type(data_path: str, country_type: str = 'ALL') -> pd.DataFrame:
    data = load_data(data_path=data_path)

    if country_type == 'EU':
        data = data.loc[data['country'].isin(eu_countries)]
    elif country_type == 'CIS':
        data = data.loc[data['country'].isin(cis_countries)]

    return data


def process_certificates_data(data: pd.DataFrame) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Наличие международных вендорских сертификатов'] = data_copy[
        'Наличие международных вендорских сертификатов'
    ].apply(
        lambda x: replace_cert(cert_name=x, certificates=certificates)
    )

    res_data = get_aggregated_data(data=data_copy,
                                   agg_column='Наличие международных вендорских сертификатов').fillna(value=0)

    return res_data


def process_npa_data(data: pd.DataFrame) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Знание НПА/ТНПА'] = data_copy[
        'Знание НПА/ТНПА'
    ].apply(
        lambda x: replace_npa(npa_name=x, npa_list=npa_lists)
    )

    res_data = get_aggregated_data(data=data_copy,
                                   agg_column='Знание НПА/ТНПА').fillna(value=0)

    return res_data


def process_eng_data(data: pd.DataFrame) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Уровень английского языка'] = data_copy[
        'Уровень английского языка'
    ].apply(
        lambda x: replace_eng(eng_level=x,
                              no_info_english=no_info_english,
                              tech_documentation=tech_documentation)
    )

    res_data = get_aggregated_data(data=data_copy,
                                   agg_column='Уровень английского языка').fillna(value=0)

    return res_data


def process_working_type_data(data: pd.DataFrame) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Режим занятости'] = data_copy[
        'Режим занятости'
    ].apply(
        lambda x: replace_working(working_name=x, working_whole_type=working_whole_type)
    )

    res_data = get_aggregated_data(data=data_copy, agg_column='Режим занятости').fillna(value=0)

    return res_data


def process_soft_knowledge_data(data: pd.DataFrame) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Знание ПО'] = data_copy[
        'Знание ПО'
    ].apply(
        lambda x: replace_tech(npa_name=x, npa_lists=npa_lists)
    )

    res_data = get_aggregated_data(data=data_copy, agg_column='Знание ПО').fillna(value=0)

    return res_data


def process_exp_data(data: pd.DataFrame, exp_dict: Dict[str, List[str]]) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Опыт работы (лет)'] = data_copy[
        'Опыт работы (лет)'
    ].apply(
        lambda x: replace_experience(exp_name=x, exp_dict=exp_dict)
    )

    res_data = get_aggregated_data(data=data_copy, agg_column='Опыт работы (лет)').fillna(value=0)

    return res_data


def process_edu_data(data: pd.DataFrame, edu_dict: Dict[str, List[str]]) -> pd.DataFrame:
    data_copy = data.copy()
    data_copy['Образование'] = data_copy[
        'Образование'
    ].apply(
        lambda x: replace_education(edu_name=x, edu_dict=edu_dict)
    )

    res_data = get_aggregated_data(data=data_copy, agg_column='Образование').fillna(value=0)

    return res_data


if __name__ == '__main__':
    vac_config = Config()

    data = load_data_on_country_type(data_path=vac_config.data_path, country_type=vac_config.country_type)

    exp_dict = parse_exp_help_text(filepath=vac_config.exp_by_years_path)
    edu_dict = parse_edu_help_text(filepath=vac_config.edu_by_degree_path)

    certificates_data = process_certificates_data(data=data)
    npa_data = process_npa_data(data=data)
    eng_data = process_eng_data(data=data)
    working_type_data = process_working_type_data(data=data)
    soft_knowledge_data = process_soft_knowledge_data(data=data)
    exp_data = process_exp_data(data=data, exp_dict=exp_dict)
    edu_data = process_edu_data(data=data, edu_dict=edu_dict)

    res_data_list = [
        certificates_data,
        npa_data,
        eng_data,
        working_type_data,
        soft_knowledge_data,
        exp_data,
        edu_data
    ]

    keys = [curr_dataframe.columns.name for curr_dataframe in res_data_list]

    res_dataframe = pd.concat(res_data_list, axis=1, keys=keys)
    res_dataframe.to_excel(f'{vac_config.country_type}_countries_stats.xlsx')
