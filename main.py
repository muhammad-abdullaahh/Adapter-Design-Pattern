from xml_service import XmlService
from adapter import XmlToJsonAdapter

# Step 1: create XML service (third-party)
xml_service = XmlService()

# Step 2: wrap it with adapter
adapter = XmlToJsonAdapter(xml_service)

# Step 3: get JSON output
json_data = adapter.get_json_data()

print("JSON Output:", json_data)