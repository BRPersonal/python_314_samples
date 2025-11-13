from openai import OpenAI
from instructor import from_openai
from pydantic import BaseModel
from utils.config import settings

class Summary(BaseModel):
    title: str
    keywords: list[str]

# Instantiate OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Pass the actual client, not just a string/model name
instructor_client = from_openai(client)

data = instructor_client.chat.completions.create(
    model=settings.OPENAI_DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Summarize Python automation"}],
    response_model=Summary
)

#using instructor library, We get exact pydantic object as output from open ai
print(f"title={data.title}, keywords={data.keywords}")
