from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = value
        try:
            if len(self.value) == 10:
                s = int(self.value)
            else:
                raise ValueError('phone number is not 10 digits ')
        except ValueError:
            raise ValueError('phone is not numbers')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone):
        self.phones.append(Phone(new_phone))
        return {self.name: self.phones}

    def remove_phone(self, del_phone):
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)
        return {self.name: self.phones}

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                self.phones[i] = Phone(new_phone)
                return {self.name: self.phones}
        raise ValueError('No such number')

    def find_phone(self, phone):
        for i in range(len(self.phones)):
            if phone == self.phones[i].value:
                return self.phones[i]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, new):
        self.data.update({new.name.value: new})

    def find(self, find_name):
        if find_name in self.data:
            return self.data[find_name]

    def delete(self, del_name):
        if del_name in self.data:
            self.data.pop(del_name)
