# Vacancies stats calculation

Project for calculating stats in excel document

## Getting Started

To download project:
```
git clone https://github.com/Vadbeg/vacancies_stats.git
```

## Installation

To use project you need to install dependencies. You can do it using this command:

```
pip install -r requirements.txt
```

## Project additional information

In folder `help_text` you will find rows separated by `---`. Those are examples of strings for different classes. 
Parsing of such files you can find in `modules/text_parsing.py`

In file `config.py` config is located. Changing this config you can change result of the script. Example:

```
class Config:
    data_path = Path('/home/vadbeg/Data/Milit/table_vno.xlsx')  # row starting file

    result_path = 'result.xlsx'  # where to save resulted file

    exp_by_years_path = Path('help_text/exp.txt')  # help file for experience rows processing
    edu_by_degree_path = Path('help_text/edu.txt')  # help file for education rows processing

    country_type: str = 'ALL'  # can be CIS, EU or ALL
```

## Authors

* **Vadim Titko** aka *Vadbeg* - [LinkedIn](https://www.linkedin.com/in/vadim-titko-89ab16149/) | [GitHub](https://github.com/Vadbeg/)
