import json


class ProcessJson:
    json_file = None

    def read_file(self):
        # print(type(self.json_file))
        try:
            with open(self.json_file, "r") as f:
                data_file = f.read()
        except FileNotFoundError as err:
            return None
        return data_file

    def sniff_schema(self):

        try:
            data = json.loads(self.read_file())
        except ValueError as err:
            return None
        return data

    def check_type(self, val):

        data_type = None
        if type(val) == dict:
            data_type = "dict"
        elif type(val) == str:
            data_type = "string"
        elif type(val) == int:
            data_type = "integer"
        elif type(val) == list:
            data_type = "array"

        return data_type

    def capture_attributes(self):

        output_data = {}

        json_data = self.sniff_schema()

        for key, value in json_data['message'].items():
            output_data[key] = {"type": self.check_type(value),
                                "tag": "",
                                "description": "",
                                "required": False
                                }

        return output_data

    def dump_output(self):
        output_json = self.capture_attributes()

        with open("schema/schema_1.json", "w") as f:
            json.dump(output_json, f)
        return
