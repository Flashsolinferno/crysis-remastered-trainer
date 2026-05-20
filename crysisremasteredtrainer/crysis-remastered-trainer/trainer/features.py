from .memory import MemoryManager

class TrainerFeatures:
    """Provides cheat features for Crysis Remastered.

    Memory addresses are placeholders — replace with real offsets from tools like Cheat Engine.
    """

    def __init__(self, mem: MemoryManager):
        self.mem = mem
        # Placeholder addresses (example offsets, not guaranteed to be correct)
        self.health_addr = 0x00A1B2C0
        self.energy_addr = 0x00A1B2C4
        self.ammo_addr = 0x00A1B2C8
        self.suit_mode_addr = 0x00A1B2D0

    def set_infinite_health(self, enable: bool):
        """Set health to max or freeze at a high value."""
        if enable:
            self.mem.write_float(self.health_addr, 9999.0)
        else:
            # Restore default (example)
            self.mem.write_float(self.health_addr, 100.0)

    def set_infinite_energy(self, enable: bool):
        """Set energy to max or freeze."""
        if enable:
            self.mem.write_float(self.energy_addr, 9999.0)
        else:
            self.mem.write_float(self.energy_addr, 100.0)

    def set_infinite_ammo(self, enable: bool):
        """Set ammo to a large value."""
        if enable:
            self.mem.write_int(self.ammo_addr, 999)
        else:
            self.mem.write_int(self.ammo_addr, 30)

    def set_suit_mode(self, mode: str):
        """Set nanosuit mode: 'strength', 'speed', 'cloak', 'armor'."""
        modes = {
            "strength": 1,
            "speed": 2,
            "cloak": 3,
            "armor": 4
        }
        value = modes.get(mode.lower())
        if value is not None:
            self.mem.write_int(self.suit_mode_addr, value)
        else:
            raise ValueError(f"Unknown suit mode: {mode}")
