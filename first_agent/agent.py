"""
This is a simple agent that can answer questions.
"""

from typing import Callable, Sequence
import os

gcloud_project_id = os.getenv("GCLOUD_PROJECT_ID")
gcloud_location = os.getenv("GCLOUD_LOCATION")
gcloud_bucket = os.getenv("GCLOUD_BUCKET")


class Agent:
    """A simple agent that can answer questions using Vertex AI and LangGraph."""

    def __init__(
        self,
        model: str,
        tools: Sequence[Callable],
        project: str,
        location: str,
        bucket: str,
    ):
        self.model_name = model
        self.tools = tools
        self.project = project
        self.location = location
        self.bucket = bucket

    def set_up(self):
        import vertexai
        from langchain_google_vertexai import ChatVertexAI
        from langgraph.prebuilt import create_react_agent

        vertexai.init(
            project=self.project, location=self.location, staging_bucket=self.bucket
        )

        model = ChatVertexAI(model_name=self.model_name)
        self.graph = create_react_agent(model, tools=self.tools)

    def query(self, **kwargs):
        return self.graph.invoke(**kwargs)


agent = Agent(
    model="gemini-2.0-flash",  # Required.
    tools=[],  # Optional.
    project=gcloud_project_id,
    location=gcloud_location,
    bucket=gcloud_bucket,
)
agent.set_up()

# response = agent.query(
#     input={
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "What is the exchange rate from US dollars to Swedish currency?",
#             }
#         ]
#     }
# )

# print(response)
