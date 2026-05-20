"""
Crysis Remastered Trainer

Usage:
    python main.py

Hotkeys (while game is running):
    F1 - Toggle Infinite Health
    F2 - Toggle Infinite Energy
    F3 - Toggle Infinite Ammo
    F4 - Set Suit Mode: Cloak
    F5 - Set Suit Mode: Strength
"""

import time
import sys
from trainer import MemoryManager, TrainerFeatures, HotkeyListener

def main():
    print("Crysis Remastered Trainer")
    print("Attempting to attach to CrysisRemastered.exe...")

    mem = MemoryManager()
    if not mem.open_process():
        print("Error: Could not find CrysisRemastered.exe process. Make sure the game is running.")
        sys.exit(1)

    print("Process attached successfully.")
    features = TrainerFeatures(mem)
    listener = HotkeyListener(features)
    listener.start()

    print("Trainer active. Use hotkeys (F1-F5) to toggle features.")
    print("Press Ctrl+C in terminal to exit.")

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        listener.stop()
        mem.close_process()

if __name__ == "__main__":
    main()
