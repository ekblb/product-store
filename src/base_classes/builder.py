class Builder():
    def __init__(self):
        self.result = {}

    def update_deep_params(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item is not temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result
