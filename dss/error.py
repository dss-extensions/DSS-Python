class DSSException(Exception):
    def __str__(self):
        return f'(#{self.args[0]}) {self.args[1]}'
