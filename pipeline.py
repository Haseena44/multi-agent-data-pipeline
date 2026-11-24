# pipeline.py - Connects all 3 Agents
from agents import CleanerAgent, AnalystAgent, ReporterAgent

class MultiAgentPipeline:
    def __init__(self):
        self.cleaner = CleanerAgent()
        self.analyst = AnalystAgent()
        self.reporter = ReporterAgent()

    def run(self, raw_data):
        cleaned = self.cleaner.run(raw_data)
        analysis = self.analyst.run(cleaned)
        final_report = self.reporter.run(analysis)
        return final_report

if __name__ == "__main__":
    data = ["  Apple iPhone Sales 100 ", "  Mac Sales 50", "", "  iPad Sales 75 "]
    pipeline = MultiAgentPipeline()
    print(pipeline.run(data))
