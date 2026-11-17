from google import genai

client = genai.Client()

print("Checking available Gemini models...\n")

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)

print("\nModel check completed!")