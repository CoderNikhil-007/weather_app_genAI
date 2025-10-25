from app.agents.base_agent import BaseAgent

class Advisor(BaseAgent):
    
    def provide_advise(self, analysis: str) -> str:

        prompt = f"Based on this weather analysis: \n{analysis}\nGive Practical advise for residents and travelers."