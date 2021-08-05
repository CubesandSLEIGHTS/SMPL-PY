class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_str(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File: {self.pos_start.fn}, Line: {self.pos_start.ln + 1}'
        return result

class IllCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'IllCharError', details)