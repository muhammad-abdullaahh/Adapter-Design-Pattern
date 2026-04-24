# 🔌 Adapter Design Pattern — Python Practice

A focused collection of Python implementations demonstrating the **Adapter Design Pattern** across real-world scenarios. Each file is a standalone, runnable example built as part of design pattern practice.

---

## 📌 What is the Adapter Pattern?

The **Adapter Pattern** is a structural design pattern that allows two incompatible interfaces to work together. It acts as a bridge between a client that expects one interface and a legacy or third-party class that provides a different one.

```
Client → Target Interface → Adapter → Adaptee (Legacy/Incompatible System)
```

---

## 📂 Files Overview

| File | Scenario | Adaptee → Target |
|------|----------|-----------------|
| `main.py` | Media Player | `LegacyMediaPlayer`, `MP4Player`, `VLCPlayer` → `MediaPlayer` |
| `task01.py` | Smart Home System | `LegacyFan` (`start/stop`) → `SmartDevice` (`turn_on/turn_off`) |
| `task02.py` | Data Processing | `CDataGenerator` (dict) → `XMLDataProcessor` (XML string) |
| `task03.py` | University Library | `LegacyArchive` (`fetch/display`) → `LibrarySystem` (`load/use`) |
| `task04.py` | College Performance | `GradingSystem` + `EvaluationSystem` → `StudentPerformance` (ABC) |

---

## 🚀 How to Run

Make sure you have **Python 3.x** installed.

```bash
# Clone the repo
git clone https://github.com/muhammad-abdullaahh/adapter-pattern-python.git
cd adapter-pattern-python

# Run any file
python main.py
python task01.py
python task02.py
python task03.py
python task04.py
```

---

## 🧠 Key Concepts Demonstrated

- **Target Interface** — the interface the client expects (`SmartDevice`, `MediaPlayer`, etc.)
- **Adaptee** — the existing class with an incompatible interface (`LegacyFan`, `LegacyMediaPlayer`, etc.)
- **Adapter** — wraps the adaptee and translates calls to match the target interface
- **Client** — interacts only with the target interface, unaware of the adaptee
- **Abstract Base Class (ABC)** — used in `task04.py` to enforce the interface contract

---

## 📋 Example Output

**`task01.py` — Smart Home Fan Adapter**
```
[SmartHome] Turning device ON...
[LegacyFan] Fan started
[SmartHome] Turning device OFF...
[LegacyFan] Fan stopped
```

**`task02.py` — C Data to XML Adapter**
```
[System] Processing XML Data:

<student>
  <id>101</id>
  <name>Ali</name>
  <marks>85</marks>
</student>
```

---

## 🏗️ Pattern Structure (UML-style)

```
┌─────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│   <<Interface>> │       │    <<Adapter>>   │       │   <<Adaptee>>    │
│  Target         │◄──────│  XxxAdapter      │──────►│  LegacySystem    │
│  + method()     │       │  + method()      │       │  + old_method()  │
└─────────────────┘       └──────────────────┘       └──────────────────┘
        ▲
        │
┌───────┴─────────┐
│    Client       │
│  Uses target    │
│  interface only │
└─────────────────┘
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts:** OOP, Structural Design Patterns, Abstract Base Classes (`abc` module)

---

## 👤 Author

**Muhammad Abdullah**
GitHub: [@muhammad-abdullaahh](https://github.com/muhammad-abdullaahh)

---

> Part of an ongoing series of design pattern implementations for academic and portfolio purposes.
