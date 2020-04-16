# coding=utf-8

import json
import xml.etree.ElementTree as etree


class JsonConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XmlConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def pardsd_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JsonConnector
    elif filepath.endswith('xml'):
        connector = XmlConnector
    else:
        raise ValueError('Can not connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve
    return factory


if __name__ == '__main__':
    f = 'datas/factory_data.json'
    json_factory = connect_to(f)
    print json_factory.data

    f = 'datas/factory_data.xml'
    xml_factory = connect_to(f)
    xml_data = xml_factory.pardsd_data
    liars = xml_data.findall('.*type')
    print liars
