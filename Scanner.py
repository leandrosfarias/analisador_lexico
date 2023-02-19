class Scanner:
    def __init__(self, file_name):
        self.file = open(file_name)
        self.current_char = self.file.read(1)

    def read_char(self):
        prev_char = self.current_char
        self.current_char = self.file.read(1)
        return prev_char

    def has_next(self):
        return bool(self.current_char)

    def close(self):
        self.file.close()
