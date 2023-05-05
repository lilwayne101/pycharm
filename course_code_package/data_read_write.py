import json

class DataReadWrite:
    def data_write(self, data, path):
        with open(path, 'a+', encoding='utf-8') as data_file:
            data_file.write(json.dumps(data))

    def data_read(self, path):
        with open(path, 'a+', encoding='utf-8') as data_file:
            data_file.seek(0)
            data = json.loads(data_file.read())
        return data
