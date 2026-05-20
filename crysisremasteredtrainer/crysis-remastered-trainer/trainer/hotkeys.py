from pynput import keyboard
from .features import TrainerFeatures

class HotkeyListener:
    """Listens for global hotkeys to toggle trainer features."""

    def __init__(self, features: TrainerFeatures):
        self.features = features
        self.listener = None
        self.infinite_health_active = False
        self.infinite_energy_active = False
        self.infinite_ammo_active = False

    def _on_press(self, key):
        """Handle key press events."""
        try:
            if key == keyboard.Key.f1:
                self.infinite_health_active = not self.infinite_health_active
                self.features.set_infinite_health(self.infinite_health_active)
                print(f"Infinite Health: {'ON' if self.infinite_health_active else 'OFF'}")
            elif key == keyboard.Key.f2:
                self.infinite_energy_active = not self.infinite_energy_active
                self.features.set_infinite_energy(self.infinite_energy_active)
                print(f"Infinite Energy: {'ON' if self.infinite_energy_active else 'OFF'}")
            elif key == keyboard.Key.f3:
                self.infinite_ammo_active = not self.infinite_ammo_active
                self.features.set_infinite_ammo(self.infinite_ammo_active)
                print(f"Infinite Ammo: {'ON' if self.infinite_ammo_active else 'OFF'}")
            elif key == keyboard.Key.f4:
                self.features.set_suit_mode("cloak")
                print("Suit Mode: Cloak")
            elif key == keyboard.Key.f5:
                self.features.set_suit_mode("strength")
                print("Suit Mode: Strength")
        except AttributeError:
            pass

    def start(self):
        """Start listening for hotkeys in a background thread."""
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()

    def stop(self):
        """Stop the hotkey listener."""
        if self.listener:
            self.listener.stop()
