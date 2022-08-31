from collections import UserDict


class Field:
    pass


class AddressBook(UserDict, Field):
    def is_data(self, name):
        if name in self.data:
            return True
        return False

    def add_record(self, record):
        self.data[record.name.value] = record


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record(Field):
    def __init__(self, new_name):
        self.name = Name(new_name)
        self.phones = []

    def add_contact(self, new_phone):
        self.phones.append(Phone(new_phone))

    def change_phone(self, old_phone, new_phone):
        if self.get_phone(old_phone):
            self.phones.append(Phone(new_phone))
            self.phones.remove(self.get_phone(old_phone))
        else:
            print('The phone number not exist')

    def delete_phone(self, phone):
        if self.get_phone(phone):
            self.phones.remove(self.get_phone(phone))
        else:
            print('The phone number not exist')

    def get_phone(self, new_phone):
        for phone in self.phones:
            if phone.value == new_phone:
                return phone
        return False


def get_name_and_phone():
    """
    To avoid duplication
    """
    name = input('Enter name:\n')
    phone = input('Enter phone number: \n')
    return name, phone


def main():
    adressbook = AddressBook()

    while True:
        a = input('Enter command:\n').lower()
        if a == '.':
            break
        elif a in ("good bye", "close", "exit"):
            print("Good Bye!")
            break
        elif a == 'hello':
            print('How can I help you?')
        elif a == 'show all':  # Show all contacts
            print(adressbook.data)
        elif a == 'show':  # Show one contact
            name = input('Enter name:\n')
            if adressbook.is_data(name):
                print('name:', adressbook.data[name].name.value, 'phone:',
                      list(map(lambda x: x.value, adressbook.data[name].phones)))
            else:
                print('Enter correct name')

        elif a.split()[0] == 'add':  # Add contact
            name, phone = get_name_and_phone()
            if len(phone.split()) > 1:
                print('Enter ONE phone number')
            else:
                if name and phone:
                    record_add = Record(name.lower())
                    record_add.add_contact(phone)
                    adressbook.add_record(record_add)
                else:
                    print('Enter correct name and phone')

        elif a.split()[0] == 'change_phone':  # Change contact number
            name, phone = get_name_and_phone()
            new_phone = input('Enter new phone\n')
            if adressbook.is_data(name):
                record_change = adressbook.data[name]
                record_change.change_phone(old_phone=phone, new_phone=new_phone)
            else:
                print('Enter correct name')

        elif a.split()[0] == 'add_phone':  # Add contact number
            name, phone = get_name_and_phone()
            if adressbook.is_data(name):
                record_add_phone = adressbook.data[name]
                record_add_phone.add_contact(phone)
            else:
                print('Enter correct name')

        elif a.split()[0] == 'delete':  # Delete contact number
            name, phone = get_name_and_phone()
            if adressbook.is_data(name):
                record_delete = adressbook.data[name]
                record_delete.delete_phone(phone)
            else:
                print('Enter correct name')


if __name__ == '__main__':
    main()
