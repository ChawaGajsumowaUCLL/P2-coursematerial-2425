class Duration:
    def __init__(self, seconds):
        self.from_seconds = seconds

    @property
    def hours(self):
        return self.from_seconds //3600
    
    @property
    def minutes(self):
        return self.from_seconds // 60
    
    @property
    def seconds(self):
        return self.from_seconds
    
    @staticmethod    
    def from_seconds(amount):
        return Duration(seconds = amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(seconds = amount*60)

    @staticmethod
    def from_hours(amount):
        return Duration(seconds = amount*3600)
