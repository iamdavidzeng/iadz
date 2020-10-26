# -*- coding: utf-8 -*-


def get_changed_fields(new: dict, old: dict):
    """
    Find out changed fields between new and old.
    """
    return {
        key: value
        for key, value in new.items()
        if key not in old or new[key] != old[key]
    }


if __name__ == "__main__":
    old_person = {
        "name": "david",
        "gender": "male",
        "phone": "123456",
        "country": "China",
        "city": "Pingxiang",
    }
    new_person = old_person.copy()
    new_person.update(
        {"name": "iamdavidzeng", "city": "Shanghai", "phone": "123333",}
    )
    print(get_changed_fields(new_person, old_person))
