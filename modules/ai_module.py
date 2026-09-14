from google import genai

# Your Gemini API key
API_KEY = "API_KEY"  # Replace with your actual Gemini API key

# Gemini client
client = genai.Client(api_key=API_KEY)


def process_ai_command(command, speak_func):
    """
    Sends unknown commands/questions to Gemini AI.
    """

    try:

        prompt = f"""
You are KAI, a helpful voice assistant.

Answer the user's question clearly and naturally.

User said:
{command}

Rules:
- Keep the answer concise because it will be spoken aloud.
- Do not use unnecessary formatting.
- Give a direct answer.
"""

        response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)

        answer = response.text

        if answer:
            speak_func(answer)
        else:
            speak_func("Sorry, I couldn't generate an answer.")

    except Exception as e:

        print("Gemini Error:", e)
        
        speak_func("Sorry, I couldn't connect to Gemini right now.")