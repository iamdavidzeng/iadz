# -*- coding: utf-8 -*-


phonebook = {
    'Beth': '9102',
    'Alice': '2341',
    'Cecil': '3258',
}

demo = "Cecil's phone number is {Cecil}"

if __name__ == '__main__':
    print(demo.format_map(phonebook))
