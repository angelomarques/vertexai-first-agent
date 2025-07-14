import os
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

from first_agent.agent import Agent as FirstAgent

from vertexai import agent_engines

requirements = "./requirements.txt"

gcloud_project_id = os.getenv("GCLOUD_PROJECT_ID")
gcloud_location = os.getenv("GCLOUD_LOCATION")
gcloud_bucket = os.getenv("GCLOUD_BUCKET")

print(gcloud_project_id, gcloud_location, gcloud_bucket)

env_vars = {
    "GCLOUD_PROJECT_ID": gcloud_project_id,
    "GCLOUD_LOCATION": gcloud_location,
    "GCLOUD_BUCKET": gcloud_bucket,
}

gcs_dir_name = "dev"  # or "staging" or "prod"

display_name = "My First Agent"

description = """
An agent that can answer questions.
"""

extra_packages = ["first_agent/agent.py"]


local_agent = FirstAgent(
    model="gemini-2.0-flash",  # Required.
    tools=[],  # Optional.
    project=gcloud_project_id,
    location=gcloud_location,
    bucket=gcloud_bucket,
)

remote_agent = agent_engines.create(
    local_agent,  # Optional.
    requirements=requirements,  # Optional.
    extra_packages=extra_packages,  # Optional.
    gcs_dir_name=gcs_dir_name,  # Optional.
    display_name=display_name,  # Optional.
    description=description,  # Optional.
    env_vars=env_vars,  # Optional.
    # build_options=build_options,    # Optional.
)

# max_retries = 5
# initial_delay = 5  # seconds
# remote_agent = None

# for i in range(max_retries):
#     try:
#         print(f"Attempt {i+1}/{max_retries} to create remote agent...")
#         remote_agent = agent_engines.create(
#             local_agent,
#             requirements=requirements,
#             gcs_dir_name=gcs_dir_name,
#             display_name=display_name,
#             description=description,
#             env_vars=env_vars,
#         )
#         print("Remote agent created successfully!")
#         break  # Exit loop if successful
#     except Exception as e:
#         if "concurrent policy changes" in str(e):
#             delay = initial_delay * (2 ** i)
#             print(f"Concurrent policy change error. Retrying in {delay} seconds... (Error: {e})")
#             time.sleep(delay)
#         else:
#             print(f"An unexpected error occurred: {e}")
#             raise
# else:
#     print(f"Failed to create remote agent after {max_retries} attempts.")

# # You can now use remote_agent if it was successfully created
# if remote_agent:
#     print("Remote agent object:", remote_agent)
