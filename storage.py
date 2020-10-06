class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            value = self.data.pop(key)
        else:
            raise Exception(f"Key {key} don't exist")

    def set(self):
        pass


    def add(self, key, value):
        if key not in self.data:
            self.data[key] = value
        else:
            raise Exception(f"Key {key} already exists")

