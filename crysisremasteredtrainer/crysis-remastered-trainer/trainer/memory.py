import ctypes
import ctypes.wintypes

class MemoryManager:
    """Handles reading/writing process memory for Crysis Remastered."""

    PROCESS_ALL_ACCESS = 0x1F0FFF

    def __init__(self, process_name: str = "CrysisRemastered.exe"):
        self.process_name = process_name
        self.handle = None
        self.pid = None

    def open_process(self) -> bool:
        """Find and open the Crysis process by name."""
        import psutil
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info["name"] == self.process_name:
                self.pid = proc.info["pid"]
                kernel32 = ctypes.windll.kernel32
                self.handle = kernel32.OpenProcess(self.PROCESS_ALL_ACCESS, False, self.pid)
                return self.handle is not None and self.handle > 0
        return False

    def close_process(self):
        """Close the process handle."""
        if self.handle:
            kernel32 = ctypes.windll.kernel32
            kernel32.CloseHandle(self.handle)
            self.handle = None
            self.pid = None

    def read_int(self, address: int) -> int:
        """Read a 4-byte integer from the process memory."""
        buffer = ctypes.c_int()
        bytes_read = ctypes.c_ulong()
        kernel32 = ctypes.windll.kernel32
        success = kernel32.ReadProcessMemory(self.handle, ctypes.c_void_p(address), ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_read))
        if success and bytes_read.value == ctypes.sizeof(buffer):
            return buffer.value
        raise RuntimeError(f"Failed to read memory at 0x{address:X}")

    def write_int(self, address: int, value: int):
        """Write a 4-byte integer to the process memory."""
        buffer = ctypes.c_int(value)
        bytes_written = ctypes.c_ulong()
        kernel32 = ctypes.windll.kernel32
        success = kernel32.WriteProcessMemory(self.handle, ctypes.c_void_p(address), ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_written))
        if not success or bytes_written.value != ctypes.sizeof(buffer):
            raise RuntimeError(f"Failed to write memory at 0x{address:X}")

    def read_float(self, address: int) -> float:
        """Read a 4-byte float from the process memory."""
        buffer = ctypes.c_float()
        bytes_read = ctypes.c_ulong()
        kernel32 = ctypes.windll.kernel32
        success = kernel32.ReadProcessMemory(self.handle, ctypes.c_void_p(address), ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_read))
        if success and bytes_read.value == ctypes.sizeof(buffer):
            return buffer.value
        raise RuntimeError(f"Failed to read memory at 0x{address:X}")

    def write_float(self, address: int, value: float):
        """Write a 4-byte float to the process memory."""
        buffer = ctypes.c_float(value)
        bytes_written = ctypes.c_ulong()
        kernel32 = ctypes.windll.kernel32
        success = kernel32.WriteProcessMemory(self.handle, ctypes.c_void_p(address), ctypes.byref(buffer), ctypes.sizeof(buffer), ctypes.byref(bytes_written))
        if not success or bytes_written.value != ctypes.sizeof(buffer):
            raise RuntimeError(f"Failed to write memory at 0x{address:X}")
