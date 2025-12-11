# world_model/commonsense.py

class CommonSenseModel:
    """
    基礎常識模型。
    """

    def check(self, statement: str):
        if "太陽掉下來" in statement:
            return "常識錯誤：太陽不可能掉下來。"
        if "水往上流" in statement:
            return "常識錯誤：水通常往下流。"
        return "常識合理。"
