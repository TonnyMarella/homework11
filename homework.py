from collections import UserDict
from datetime import datetime, timedelta
import re

from simple_commands import simple
from show_commands import show
from phone_commands import phone_command


class Field:
    def __init__(self):
        self._value = ''

    @property
    def value(self):
        """
        getter for phone and birthday
        :return: self._value
        """
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class AddressBook(UserDict, Field):
    def is_data(self, name) -> bool:
        return name in self.data

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self):
        for key, record in self.data.items():
            yield key, record


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, phone):
        """
        setter for phone
        :param phone:
        """
        if re.match(r'^\+1?\d{9,20}$', phone):
            self._value = phone
        else:
            print('Number must be minimum 9 digits maximum 20 and start with \'+\'')


class Birthday(Field):
    @Field.value.setter
    def value(self, birthday):
        """
        setter for birthday
        :param birthday:
        :return:
        """
        if int(birthday.year) <= 2022 and int(birthday.month) <= 12 and int(birthday.day) <= 31:
            self._value = datetime(year=datetime.now().year, month=int(birthday.month),
                                   day=int(birthday.day))
        else:
            print('Birthday entered incorrectly')


class Record():
    def __init__(self, new_name, birthday=None):
        self.name = Name()
        self.name.value = new_name
        self.phones = []
        self.birthday = Birthday()
        if birthday:
            self.birthday.value = birthday

    def days_to_birthday(self):
        """
        Returns the number of days until the contact's birthday
        :return:
        """
        if not self.birthday:
            return 'You did not enter a birthday'
        now = datetime.now()
        if int(self.birthday.value.month) <= int(now.month) and int(self.birthday.value.day) != int(now.day):
            days_to_birthday = self.birthday.value - now.replace(year=(int(now.year) - 1)) + timedelta(days=1)
            return days_to_birthday.days
        days_to_birthday = self.birthday.value - now + timedelta(days=1)
        return days_to_birthday.days

    def add_contact(self, new_phone):
        """
        Adds contact to adressbook
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
        current_phone = self.get_phone(old_phone)
        if current_phone:
            phone = Phone()
            phone.value = new_phone
            phone_examination = self.phones.append(phone)
            if phone_examination == phone:
                self.phones.remove(current_phone)
        else:
            print('The phone number not exist')

    def delete_phone(self, phone):
        """
        Deletes a number
        :param phone:
        """
        current_phone = self.get_phone(phone)
        if current_phone:
            self.phones.remove(current_phone)
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
        command = input('Enter command:\n').lower()
        if command == '.':
            break
        simple(command)
        show(command, adressbook)
        phone_command(command, adressbook, get_name_and_phone, Record)

        if command == 'birthday':
            name = input('Enter name:\n')
            if adressbook.is_data(name):
                record_change = adressbook.data[name]
                print('Days to birthday:', record_change.days_to_birthday())


if __name__ == '__main__':
    main()
