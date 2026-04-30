import random, math, datetime as dt, json
from agents import DataAgent, ForecastAgent, StrategyAgent, ReportAgent

def main():
    data = DataAgent().collect()
    forecast = ForecastAgent().predict(data)
    plan = StrategyAgent().optimize(data, forecast)
    report = ReportAgent().render(data, forecast, plan)
    print(report)

if __name__ == '__main__':
    main()
