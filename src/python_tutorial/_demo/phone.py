import re
import phonenumbers

def get_international_phone(phone):
        try:
            phone = re.sub(r"[)( ]", "", phone)
            phone_obj = phonenumbers.parse(phone, None)

            international_phone = phonenumbers.format_number(
                phone_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            return phone, international_phone
        except phonenumbers.NumberParseException:
            return None, None


def get_wallet(balance):
    result = None
    if balance > 0:
        balance -= 1
        print("1")
        result = balance
    return result

if __name__ == "__main__":
    phone = "+86 15779712170"
    # print(get_international_phone(phone))

    print(get_wallet(3))
