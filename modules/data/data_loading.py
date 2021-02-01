"""Module with functions for data loading"""

import pandas as pd


def read_sheet(reader, sheet_name):
    data = pd.read_excel(reader, skiprows=1, sheet_name=sheet_name, usecols='A:I')
    data = data.dropna(axis=0, how='all').dropna(axis=1, how='all')

    return data


def get_aggregated_data(data, agg_column):
    res_data = data.groupby(by=['Должность/отрасль', agg_column])['country'].count()
    res_data = res_data.reset_index(level=1)

    res_data = pd.pivot_table(res_data, values='country',
                              columns=[agg_column],
                              index='Должность/отрасль')

    return res_data


def load_data(data_path: str) -> pd.DataFrame:
    with pd.ExcelFile(data_path) as reader:
        all_sheets = list()

        for curr_sheet_name in reader.sheet_names:

            try:
                data = read_sheet(reader=reader, sheet_name=curr_sheet_name)

                data['country'] = len(data) * [curr_sheet_name]

                if len(data) > 0:
                    data['Должность/отрасль'] = data['Должность/отрасль'].str.strip()
                    data['Должность/отрасль'] = data['Должность/отрасль'].str.replace(
                        'Cпециалист по информационной безопасности',
                        'Специалист по информационной безопасности'
                    )

                all_sheets.append(data)
            except Exception:
                raise

    all_data = pd.concat(all_sheets)

    return all_data
