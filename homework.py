from collections import UserDict


class Field:
    pass


class AddressBook(UserDict, Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date = {}

    def add_record(self):
        self.date[Record.name.value] = Record.phone.value

    def iterator(self, n):
        result = []
        for key, value in self.date.items():
            result.append({key: value})
        return result[:n]


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone=None):
        self.value = phone


class Record(Field):
    name = None
    phone = None

    @staticmethod
    def add_contact(new_name, new_phone=None):
        Record.name = Name(new_name)
        Record.phone = Phone(new_phone)

    @staticmethod
    def delete_contact(cls, contact_name):
        for key, value in cls.date.items():
            if key == contact_name:
                Record.name = Name(contact_name)
                Record.phone = Phone()

    @staticmethod
    def edit_contact(cls, contact_name, new_phone):
        for key, value in cls.date.items():
            if key == contact_name:
                Record.name = Name(contact_name)
                Record.phone = Phone(new_phone)


# def main():
#     start = AddressBook()
#     record = Record()
#
#     while True:
#         a = input().lower()
#         if a == '.':
#             break
#         elif a in ("good bye", "close", "exit"):
#             print("Good Bye!")
#             break
#         elif a == 'hello':
#             print('How can I help you?')
#         elif a == 'show all':
#             print(start.date)
#         elif a.split()[0] == 'add':
#             record.add_contact(a.split()[1], a.split()[2:])
#             start.add_record()
#         elif a.split()[0] == 'change':
#             record.edit_contact(start, a.split()[1], a.split()[2:])
#             start.add_record()
#         elif a.split()[0] == 'delete':
#             need_to_delete = ''
#             for key, value in start.date.items():
#                 if key == a.split()[1]:
#                     need_to_delete = a.split()[1]
#             if need_to_delete:
#                 del start.date[need_to_delete]


if __name__ == '__main__':
    # main()
    start = AddressBook()
    record = Record()
    record.add_contact("Artem", '123123')
    start.add_record()
    record.add_contact("Dima", '123123')
    start.add_record()
    record.add_contact("ADasd", '123123')
    start.add_record()
    record.add_contact("dsad", '123123')
    start.add_record()
    print(start.iterator(3))
