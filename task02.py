# Target Interface (System expects XML)
class XMLDataProcessor:
    def process_xml(self):
        pass


# Adaptee (Legacy C-style Data Generator)
class CDataGenerator:
    def get_c_data(self):
        return {
            "id": 101,
            "name": "Ali",
            "marks": 85
        }


# Adapter (Converts C-style data into XML format)
class CtoXMLAdapter(XMLDataProcessor):
    def __init__(self, c_data_generator):   # ✅ FIXED
        self.c_data_generator = c_data_generator

    def process_xml(self):
        c_data = self.c_data_generator.get_c_data()

        xml_data = "<student>\n"
        xml_data += f"  <id>{c_data['id']}</id>\n"
        xml_data += f"  <name>{c_data['name']}</name>\n"
        xml_data += f"  <marks>{c_data['marks']}</marks>\n"
        xml_data += "</student>"

        return xml_data


# Client (System that only accepts XML)
class DataProcessingSystem:
    def __init__(self, xml_processor):   # ✅ FIXED
        self.xml_processor = xml_processor

    def run(self):
        xml_data = self.xml_processor.process_xml()
        print("[System] Processing XML Data:\n")
        print(xml_data)


# Main Execution
if __name__ == "__main__":   # ✅ FIXED
    c_generator = CDataGenerator()
    adapter = CtoXMLAdapter(c_generator)
    system = DataProcessingSystem(adapter)

    system.run()