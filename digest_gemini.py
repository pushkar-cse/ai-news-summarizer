import feedparser
from google import genai

FEED_URL = "https://feeds.bbci.co.uk/news/rss.xml"  # swap in any RSS feed
MAX_ITEMS = 15
MODEL = "gemini-3.5-flash"

# Reads your key from the GEMINI_API_KEY environment variable
client = genai.Client()


def get_headlines():
    feed = feedparser.parse(FEED_URL)
    items = []
    for entry in feed.entries[:MAX_ITEMS]:
        items.append(f"- {entry.title}: {entry.get('summary', '')}")
    return "\n".join(items)


def summarize(text):
    response = client.models.generate_content(
        model=MODEL,
        contents="Summarize these news items in 5 short bullet points:\n\n" + text,
    )
    return response.text


if __name__ == "__main__":
    headlines = get_headlines()
    print("Today's digest:\n")
    print(summarize(headlines))
