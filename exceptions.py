class InvalidPath(Exception):
    def __init__(self, full_path):
        """
        :type full_path: str
        """
        self.full_path = full_path