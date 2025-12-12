# memory_core/style_memory.py

class StyleMemory:
    """
    記錄使用者的偏好與風格。
    """

    def __init__(self):
        self.preferences = {}

    def update(self, key: str, value: str):
        self.preferences[key] = value

    def get(self, key: str):
        return self.preferences.get(key, None)
