from app.agents.base_agent import BaseAgent

class Analyzer(BaseAgent):

    def analyze_weather(self, summary : str) -> str:

        prompt = f"Analyze the following weather summary and provide insights (temperature extremes, rain, wind, etc):\n {summary}"
        return self.generate(prompt)