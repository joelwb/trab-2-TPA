from datetime import date


class Data(object):
    def __init__(self, email: str, gender: str, uid: str, birthday: date, height: int, weight: int):
        self.email: str = email
        self.gender: str = gender
        self.uid: str = uid
        self.birthday: date = birthday
        self.height: int = height
        self.weight: int = weight

    def __le__(self, other):
        return self != data_inf and (other == data_inf or self.uid <= other.uid)

    def __gt__(self, other):
        return self.uid > other.uid

    def __str__(self):
        return f"{self.email},{self.gender},{self.uid},{self.birthday.strftime('%Y-%m-%d')},{self.height}.{self.weight}"

    def __repr__(self):
        return self.uid


data_inf = Data("", "", "", None, -1, -1)

