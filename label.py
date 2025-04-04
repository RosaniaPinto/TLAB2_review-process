from openai import OpenAI


def get_sentiment(text: list) -> list:
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"developer", "content": "You are a children's short-story writer"},
        {"role":"developer", "content": "Write a one-sentence bedtime story about a unicorn"}
    ]
    )

    """
    INSERT DOCSTRING HERE
    """
    system_prompt = """
    As a artist manager, if I wanted to be a musician but I have zeo fans, what are steps to get to stardom?
    ...
    """  

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    print(completions,choices[0].message.content)
