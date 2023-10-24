from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from mimesis import Address
from mimesis.builtins import RussiaSpecProvider
import pandas as pd
import random

person = Person(Locale.RU)
person_address = Address(Locale.RU)
person_ru = RussiaSpecProvider()

def get_gen_data(num):
    struct_raw = {
        'first_name': [],
        'last_name': [],
        'patronymic': [],
        'age': [],
        'email': [],
        'first_name': [],
        'phone_number': [],
        'username': [],
        'occupation': [],
        'location': [],
        'language': [],
        'university': [],
        'work_experience': [],
    }

    for i in range(num):
        gender = random.choice([Gender.MALE, Gender.FEMALE])
        struct_raw['first_name'].append(person.first_name(gender))
        struct_raw['last_name'].append(person.last_name(gender))
        struct_raw['patronymic'].append(person_ru.patronymic(gender))
        struct_raw['age'].append(person.age())
        struct_raw['email'].append(person.email())
        struct_raw['phone_number'].append(person.phone_number())
        struct_raw['username'].append(person.username())
        struct_raw['occupation'].append(person.occupation())
        struct_raw['location'].append(person_address.city())
        struct_raw['language'].append(person.language())
        struct_raw['university'].append(person.university())
        struct_raw['work_experience'].append(person.work_experience())
    
    return struct_raw
