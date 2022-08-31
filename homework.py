from collections import UserDict
from datetime import datetime, timedelta


class Field:
    pass


class AddressBook(UserDict, Field):
    def is_data(self, name):
        if name in self.data:
            return True
        return False

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n):
        result = []
        for key, value in self.data.items():
            result.append({key: value})
        return result[:n]


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self):
        self._value = ''

    @property
    def value(self):
        """
        getter for phone
        :return: self._value
        """
        return self._value

    @value.setter
    def value(self, x):
        """
        setter for phone
        :param x:
        """
        if x.isdigit():
            self._value = x
        else:
            print('Number is not digit')


class Birthday(Field):
    def __init__(self):
        self._value = ''

    @property
    def value(self):
        """
        getter for birthday
        :return: self._value
        """
        return self._value

    @value.setter
    def value(self, x):
        """
        setter for birthday
        :param x:
        :return:
        """
        if isinstance(x, datetime):
            self._value = x
        elif len(x.split('-')) == 3 and int(x.split('-')[0]) <= 2022 and int(x.split('-')[1]) <= 12 and int(
                x.split('-')[2]) <= 31:
            self._value = datetime(year=datetime.now().year, month=int(x.split('-')[1]), day=int(x.split('-')[2]))
        else:
            print('Birthday entered incorrectly')


class Record(Field):
    def __init__(self, new_name, birthday=None):
        self.name = Name(new_name)
        self.phones = []
        if birthday:
            self.birthday = Birthday()
            self.birthday.value = birthday
        else:
            self.birthday = birthday

    def days_to_birthday(self):
        """
        Returns the number of days until the contact's birthday
        :return:
        """
        if self.birthday.value:
            now = datetime.now()
            if int(self.birthday.value.month) <= int(now.month) and int(self.birthday.value.day) != int(now.day):
                self.birthday.value = self.birthday.value.replace(year=2023)
            days_to_birthday = self.birthday.value - now + timedelta(days=1)
            return days_to_birthday.days
        else:
            return 'You did not enter a birthday'

    def add_contact(self, new_phone):
        """
        Adds contact in adressbook
        :param new_phone:
        """
        phone = Phone()
        phone.value = new_phone
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        """
        Changes an existing number
        :param old_phone:
        :param new_phone:
        """
        if self.get_phone(old_phone):
            phone = Phone()
            phone.value = new_phone
            self.phones.append(phone)
            self.phones.remove(self.get_phone(old_phone))
        else:
            print('The phone number not exist')

    def delete_phone(self, phone):
        """
        Deletes a number
        :param phone:
        """
        if self.get_phone(phone):
            self.phones.remove(self.get_phone(phone))
        else:
            print('The phone number not exist')

    def get_phone(self, new_phone):
        """
        Checks if a number exists,
        :param new_phone:
        :return: phone or False
        """
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
        elif a == 'show_iter':
            count = int(input('Enter the number of entries:\n'))
            print(adressbook.iterator(count))
        elif a == 'birthday':
            name = input('Enter name:\n')
            if adressbook.is_data(name):
                record_change = adressbook.data[name]
                print('Days to birthday:', record_change.days_to_birthday())

        elif a.split()[0] == 'add':  # Add contact
            name, phone = get_name_and_phone()
            birthday = input('Enter birthday(Y-M-D) or skip(enter):\n')
            if len(phone.split()) > 1:
                print('Enter ONE phone number')
            else:
                if name and phone:
                    record_add = Record(name.lower(), birthday if birthday != '' else None)
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
