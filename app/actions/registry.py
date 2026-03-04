import os
import importlib
from pathlib import Path
from .base import Action

def get_all_actions():
    actions = {}
    actions_dir = Path(__file__).parent

    for file in os.listdir(actions_dir):
        if file.endswith(".py") and file not in ("__init__.py", "base.py", "registry.py"):
            module_name = f"app.actions.{file[:-3]}"
            module = importlib.import_module(module_name)

            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Action) and obj is not Action:
                    instance = obj()
                    actions[instance.name] = instance
    return actions
