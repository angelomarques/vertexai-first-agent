from vertexai import agent_engines

resource_name = "test/resource/name"

agent_engine = agent_engines.get(resource_name=resource_name)

print(agent_engine.execution_api_client)
