class Student:
    def __init__(self, name, slack_handle=None):
        self.name = name
        self.slack_handle = slack_handle
    
    def __repr__(self) -> str:
        return f"<Student {self.name}, {self.slack_handle}>"


students = [
    Student('Leif Enoksen', '@Leif Enoksen'),
    Student('Chris Hontos', '@Chris Hontos'),
    # Student('Michael Ibragimchayev', '@Michael Ibragimchayev'),
    Student('Samuel Peck', '@Sam Peck'),
    Student('Jamal Portericker', '@Jamal Portericker'),
    Student('Michoel Rivkin', '@Michoel'),
    Student('Anglea S', '@Angela Shen'),
    Student('Ryan Sinnott', '@Ryan Sinnott'),
    Student('James Sullivan', '@James'),
    Student('David Yarmush', '@David Yarmush'),
]