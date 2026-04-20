import xml.etree.ElementTree as ET
import json
from json_interface import JsonData

class XmlToJsonAdapter(JsonData):

    def __init__(self, xml_service):
        self.xml_service = xml_service

    def get_json_data(self):
        xml_data = self.xml_service.get_data()

        # Parse XML
        root = ET.fromstring(xml_data)

        # Convert XML → dict
        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text

        # Convert dict → JSON
        return json.dumps(data_dict)