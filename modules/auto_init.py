import os
import importlib

class AtlasBrainRegistry:
    def __init__(self):
        self.brains = {}

    def load_modules(self, base_path="modules"):
        for filename in os.listdir(base_path):
            if filename.endswith(".py") and filename not in ["__init__.py", "auto_init.py"]:
                module_name = filename.replace(".py", "")
                module_path = f"{base_path}.{module_name}"

                try:
                    module = importlib.import_module(module_path)

                    class_name = "".join([part.capitalize() for part in module_name.split("_")])
                    if hasattr(module, class_name):
                        cls = getattr(module, class_name)
                        instance = cls()
                        self.brains[module_name] = instance
                        print(f"[AUTO-INIT] Registered: {module_name}")
                except Exception as e:
                    print(f"[AUTO-INIT] Error loading {module_name}: {e}")

    def get(self, name):
        return self.brains.get(name, None)


brain_registry = AtlasBrainRegistry()
brain_registry.load_modules()
