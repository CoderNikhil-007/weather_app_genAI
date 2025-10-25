from app.agents.base_agent import BaseAgent

class DataFetcher(BaseAgent):

    def fetch_weather_summary(self, raw_data: dict) -> str:
        prompt = f"Here is the raw weather data : {raw_data}\nExtract Key Weather details precisely"
        return self.generate(prompt)