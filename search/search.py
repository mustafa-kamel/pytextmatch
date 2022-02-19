import os
import pandas
from fuzzywuzzy import fuzz, process


class Search():

    def __init__(self, query):
        self.query = query
        with open(
                os.path.join(os.path.dirname(__file__), 'data.csv'), "r") as f:
            self.csv_data = pandas.read_csv(
                f, usecols=['Key', 'Values'], skip_blank_lines=True)

    def get_value_by_key(self):
        self.csv_data.set_index("Key", inplace=True)
        return self.csv_data.loc[self.query]

    def get_values(self):
        value = self.get_value_by_key()
        if value.isnull().Values:
            return []
        values_list = process.extract(
            value.Values, self.csv_data.dropna().Values.to_list(),
            scorer=fuzz.ratio)
        return values_list

    def get_result(self):
        values = []
        for v in self.get_values():
            if 50 < v[1] < 100:
                values.append({'value': v[0], 'percentage': v[1]})
        return {
            "key": self.query,
            "values": values,
            "length": len(values) + 1
        }
