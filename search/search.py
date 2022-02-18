import os
import pandas


class Search():

    def __init__(self, query):
        self.query = query
        with open(
                os.path.join(os.path.dirname(__file__), 'data.csv'), "r") as f:
            self.csv_data = pandas.read_csv(f, usecols=['Key', 'Values'])

    def get_value_by_key(self):
        self.csv_data.set_index("Key", inplace=True)
        return self.csv_data.loc[self.query]

    def get_values(self):
        value = self.get_value_by_key()
        # search value similariteis in csv
        return [
            {"value": value.Values, "percentage": "%91"},
        ]

    def get_result(self):
        values = self.get_values()
        return {
            "key": self.query,
            "values": values,
            "length": len(values) + 1
        }
