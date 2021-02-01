"""Module with config"""

from pathlib import Path


class Config:
    data_path = Path('/home/vadbeg/Data/Milit/table_vno.xlsx')

    result_path = 'result.xlsx'

    exp_by_years_path = Path('help_text/exp.txt')
    edu_by_degree_path = Path('help_text/edu.txt')

    country_type: str = 'ALL'

