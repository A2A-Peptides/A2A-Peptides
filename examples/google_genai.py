"""A2A Peptides — google-genai with an MCP ClientSession passed as a tool.
pip install google-genai mcp
Note: some google-genai releases deep-copy the tool list; if the session refuses to copy, neutralise it with
    ClientSession.__deepcopy__ = lambda self, memo: self
before generate_content. The door itself needs no adapter.
"""
import asyncio, os
from google import genai
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://mcp.a2a-peptides.ai/mcp"


async def main():
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            r = await client.aio.models.generate_content(
                model="gemini-2.5-pro",
                contents="Resolve the jurisdiction for a US-CA ship-to, resolve a wholesaler actor, then gate semaglutide on the licensed-medicine pathway. Report the reason code and rule-set version.",
                config=genai.types.GenerateContentConfig(tools=[session], temperature=0),
            )
            print(r.text)


if __name__ == "__main__":
    asyncio.run(main())
