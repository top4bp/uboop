from .base import Action
import re

class RgbToHexColorAction(Action):
    name = "RGB to Hex Color"
    def run(self, text: str) -> str:
        nums = [int(n) for n in re.findall(r"\d+", text)]
        if len(nums) < 3:
            raise ValueError("Need three numeric RGB components")
        r, g, b = nums[0], nums[1], nums[2]
        return "#{:02x}{:02x}{:02x}".format(r & 0xFF, g & 0xFF, b & 0xFF)

