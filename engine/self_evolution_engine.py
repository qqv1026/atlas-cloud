class SelfEvolutionEngine:
    """
    自我進化引擎：根據學習紀錄檢測弱點並給出成長建議。
    """

    def analyze_weakness(self, learning_record: dict):
        keywords = learning_record.get("keywords", [])
        if not keywords:
            return "弱點：關鍵概念不足；建議擴充關鍵詞庫。"
        if "重力" in keywords and "加速度" not in keywords:
            return "弱點：對加速度理解不足；建議學習 v-t 與 a。"
        return "狀態良好：持續練習並連結概念網。"
