"""Unit tests for TrainerFeatures (no actual memory access)."""

import unittest
from unittest.mock import MagicMock, patch
from trainer.features import TrainerFeatures
from trainer.memory import MemoryManager

class TestTrainerFeatures(unittest.TestCase):
    """Test suite for TrainerFeatures."""

    def setUp(self):
        """Create a mock MemoryManager for testing."""
        self.mock_mem = MagicMock(spec=MemoryManager)
        self.features = TrainerFeatures(self.mock_mem)

    def test_set_infinite_health_enable(self):
        """Enable infinite health should write 9999.0 to health address."""
        self.features.set_infinite_health(True)
        self.mock_mem.write_float.assert_called_once_with(self.features.health_addr, 9999.0)

    def test_set_infinite_health_disable(self):
        """Disable infinite health should write 100.0 to health address."""
        self.features.set_infinite_health(False)
        self.mock_mem.write_float.assert_called_once_with(self.features.health_addr, 100.0)

    def test_set_infinite_energy_enable(self):
        """Enable infinite energy should write 9999.0 to energy address."""
        self.features.set_infinite_energy(True)
        self.mock_mem.write_float.assert_called_once_with(self.features.energy_addr, 9999.0)

    def test_set_infinite_ammo_enable(self):
        """Enable infinite ammo should write 999 to ammo address."""
        self.features.set_infinite_ammo(True)
        self.mock_mem.write_int.assert_called_once_with(self.features.ammo_addr, 999)

    def test_set_suit_mode_strength(self):
        """Setting suit mode to strength should write 1."""
        self.features.set_suit_mode("strength")
        self.mock_mem.write_int.assert_called_once_with(self.features.suit_mode_addr, 1)

    def test_set_suit_mode_cloak(self):
        """Setting suit mode to cloak should write 3."""
        self.features.set_suit_mode("cloak")
        self.mock_mem.write_int.assert_called_once_with(self.features.suit_mode_addr, 3)

    def test_set_suit_mode_invalid(self):
        """Invalid suit mode should raise ValueError."""
        with self.assertRaises(ValueError):
            self.features.set_suit_mode("invisible")

if __name__ == "__main__":
    unittest.main()
