import pandas


def get_data(filename):
    xl_file = pandas.ExcelFile(filename)

    dfs = {sheet_name: xl_file.parse(sheet_name)
           for sheet_name in xl_file.sheet_names}

    return dfs
