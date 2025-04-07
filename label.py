from openai import OpenAI


def get_sentiment(text: list) -> list:

    if not text:
        return "Wrong input. text must be an array of strings."
    if text and not all(isinstance(i,str) for i in text):
        return "Wrong input. text must be an array of strongs."
    
    """
    Utilizing both system prompt and prompt as strings for customer reviews
    """
    system_prompt - """You are a helpful assistant that categorizes text reviews into sentiment categories. The categories are: positive, neutral, negative, and irrelevant."""
    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.
    """
   
    # Use only a one-word response per line. Do not include any numbers.
    #{text}
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages-[
        {"role":"developer", "content": system_prompt},
        {"role":"developer", "content": prompt + "\n".join(text) + "\n"}
    ]
)
   
    return completion.choices[0].message.content.split()
