import asyncio
import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import InMemoryRunner
from google.genai import types as genai_types

# Defining a very simple chat agent
root_agent = chat_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="chat_agent",
    description="A friendly assistant for conversations.",
    instruction=(
        "You are a helpful chat assistant."
        "Answer the user's questions clearly without any ambiguity."
    )
)

async def main() -> None:
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError("Please set the GOOGLE_API_KEY environment variable.")

    # create an in-memory runner for this agent
    runner = InMemoryRunner(
        agent=chat_agent,
        app_name="chat_app",
    )

    # create a session (kept in memory only for this run)
    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="local-user"
    )

    print("ADK Chat Agent is ready.")
    print("Type your message, or 'exit' / 'quit' to stop. \n")

    # simple chat loop
    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break

        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_text:
            continue

    # build the user message as a content object
    new_message = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text=user_text)]
    )

    # collect the model's textual reply
    reply_chunks: list[str] = []

    # run the agent through the runner for this turn
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=new_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                text = getattr(part, "text", None)
                if text:
                    reply_chunks.append(text)

    # print the last assembled reply (if any)
    if reply_chunks:
        # join all text parts for this turn
        reply_text = "".join(reply_chunks)
        print(f"Agent: {reply_text} \n")
    else:
        print("Agent: (no response content received) \n")


if __name__ == "__main__":
    asyncio.run(main())