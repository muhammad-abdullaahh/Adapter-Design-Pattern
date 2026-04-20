# 🔌 Adapter Pattern Demo (XML → JSON Converter)

This project demonstrates the **Adapter Design Pattern** in Python by converting XML data from a third-party service into JSON format without modifying the original service.

---

## 📌 Problem Statement

We are working with a third-party API that returns data in **XML format**, but our application (charts system) requires **JSON format**.

Since we cannot modify the third-party service, we use an **Adapter Pattern** to bridge the gap.

---

## 💡 Solution

We created an **Adapter (XmlToJsonAdapter)** that:
- Takes XML data from the service
- Converts it into a Python dictionary
- Then converts it into JSON format

---

## 🧱 Project Structure

LAB08/
│
├── main.py              # Client code (entry point)
├── xml_service.py       # Third-party XML service (Adaptee)
├── json_interface.py    # Interface (Abstract Base Class)
└── adapter.py           # Adapter (XML → JSON converter)

---

## ⚙️ How It Works

1. XmlService returns XML data  
2. XmlToJsonAdapter converts XML → JSON  
3. main.py uses only JSON output (doesn’t care about XML)

---

## 🚀 How to Run

1. Open project in VS Code  
2. Run:

python main.py

---

## 📤 Example Output

JSON Output: {"name": "Abdullah", "age": "21"}

---

## 🧠 Design Pattern Used

Adapter Pattern

Intent:
Convert the interface of a class into another interface clients expect.

Why used:
- Cannot modify third-party API
- Need JSON format for system
- Adapter acts as translator

---

## 🎯 Key Benefits

- No modification to third-party code  
- Loose coupling  
- Easy integration  
- Open/Closed principle  

---

## 👨‍💻 Tech Used

- Python
- XML parsing
- JSON handling
- OOP Design Patterns

---

## 🔥 Author

Software Design & Architecture Lab Project
