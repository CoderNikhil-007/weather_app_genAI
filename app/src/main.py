from fastapi import FastAPI

from app.models.user_input import UserInput
from app.agents.data_fetcher import DataFetcher
from app.agents.analyzer import Analyzer
from app.agents.advisor import Advisor
from app.models.utils import fetch_weather

app = FastAPI(title="Weather App", version="1.0")

#Initialize Agents
data_fetcher = DataFetcher("DataFetcher")
analyzer = Analyzer("Analyzer")
advisor = Advisor("Advisor")

@app.get('/')
def root():
    return {"message" : "Welcome to weather API Agent"}

@app.post('/weather_api')
def weather(text : UserInput):

    city = text.city

    raw_data = fetch_weather(city)

    summary = data_fetcher.fetch_weather_summary(raw_data=raw_data)

    analysis = analyzer.analyze_weather(summary=summary)

    advise = advisor.provide_advise(analysis=analysis)

    return {
        "city" : city,
        "raw_data" : raw_data,
        "summary" : summary,
        "analysis" : analysis,
        "advise" : advise
    }