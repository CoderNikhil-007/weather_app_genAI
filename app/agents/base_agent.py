from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

load_dotenv()

# Azure OpenAI Configuration
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


class BaseAgent:

    user_agent = UserProxyAgent(name = "User", human_input_mode="NEVER", code_execution_config={"use_docker": False})

    def __init__(self, name):
        
        self.name = name
        
        # Check if Azure OpenAI is configured
        if azure_api_key and azure_endpoint and azure_deployment:
            # Use Azure OpenAI
            self.llm_model = azure_deployment
            llm_config = {
                "model": self.llm_model,
                "api_key": azure_api_key,
                "base_url": azure_endpoint,
                "api_type": "azure",
                "api_version": azure_api_version,
                "max_tokens":6553,
                "temperature":0.7,
                "top_p":0.95,
            }
            print(f"Azure OpenAI Config: {azure_endpoint}, Deployment: {azure_deployment}")
        else:
            raise ValueError("Azure OpenAI configuration is incomplete. Please check your environment variables.")

        
        self.agent = AssistantAgent(name=self.name, llm_config=llm_config)

    def generate(self, prompt : str) ->str:
        #Common function to generate output
        return self.user_agent.initiate_chat(self.agent, message=prompt)