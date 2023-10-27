"""
    - a structural design pattern that allows objects with incompatible interfaces to collaborate.
"""

import xmltodict


class Application:
    def send_request(self):
        return 'adapter_data.xml'


class Analytic:
    def rececive_reqeust(self, json):
        return json


class Adapter:  # convertor
    def convert_xml_json(self, file):
        with open(file, 'r') as my_file:
            obj = xmltodict.parse(my_file.read())
            return obj


def client():
    sender = Application().send_request()
    converted_data = Adapter().convert_xml_json(sender)
    receiver = Analytic().rececive_reqeust(converted_data)

    return receiver


print(client())
