import requests
from langchain_core.documents import Document

class Wikipedia:
    def __init__(self, lang="en"):
        self.lang = lang

    def search(self, title, first_paragraph_only=False):
        url = f"https://{self.lang}.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
            "exintro": first_paragraph_only,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            if not pages:
                return None
            page = list(pages.values())[0]
            return Document(
                page_content=page.get("extract", ""),
                metadata={"source": f"https://{self.lang}.wikipedia.org/wiki/{title}"}
            )
        except requests.RequestException as e:
            print(f"Error fetching Wikipedia content: {e}")
            return None
    
def get_wiki_content(title, lang="en"):
    wiki = Wikipedia(lang=lang)
    return wiki.search(title, first_paragraph_only=False)