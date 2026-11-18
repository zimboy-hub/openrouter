import os
from openai import OpenAI

# Initialize the OpenAI client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", "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"),
)

def ask_openrouter():
    try:
        # You can specify any model available on OpenRouter 
        # (e.g., 'anthropic/claude-3.5-sonnet', 'openai/gpt-4o', or free models like 'deepseek/deepseek-chat')
        response = client.chat.completions.create(
            model="dots-studio/dots-3-note-preview:free",  # or another model of your choice
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": "What is the integral of x^2?"}
            ],
            # Optional headers recommended by OpenRouter for ranking/site attribution
            extra_headers={
                "HTTP-Referer": "https://github.com/zimboy-hub", # Optional: Your site URL
                "X-Title": "openrouter",     # Optional: Your app name
            }
        )
        
        # Print the response content
        print("AI Response:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ask_openrouter()