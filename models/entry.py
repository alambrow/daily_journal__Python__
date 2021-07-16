class Entry():
    """Entry class for return results of SQL query
    """
    def __init__(self, id, title, text, time_stamp):
        self.id = id
        self.title = title
        self.text = text
        self.timestamp = time_stamp
