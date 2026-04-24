# Target Interface (What smart home system expects)
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Adaptee (Legacy Device with different interface)
class LegacyFan:
    def start(self):
        print("[LegacyFan] Fan started")

    def stop(self):
        print("[LegacyFan] Fan stopped")


# Adapter (Converts start/stop → turn_on/turn_off)
class FanAdapter(SmartDevice):
    def __init__(self, legacy_fan):   # ✅ FIXED
        self.legacy_fan = legacy_fan

    def turn_on(self):
        self.legacy_fan.start()

    def turn_off(self):
        self.legacy_fan.stop()


# Client (Smart Home System)
class SmartHomeSystem:
    def __init__(self, device):   # ✅ FIXED
        self.device = device

    def operate(self):
        print("[SmartHome] Turning device ON...")
        self.device.turn_on()

        print("[SmartHome] Turning device OFF...")
        self.device.turn_off()


# Main Execution
if __name__ == "__main__":   # ✅ FIXED
    old_fan = LegacyFan()
    adapted_fan = FanAdapter(old_fan)
    smart_home = SmartHomeSystem(adapted_fan)

    smart_home.operate()