from utils import qa_chain, search, wiki_scrap

class Controller:
    def __init__(self, title, lang="en"):
        self.title = title
        self.lang = lang
    
    def get_answer(self, question):
        try:
            source = wiki_scrap.get_wiki_content(self.title, lang=self.lang)
            if not source:
                return f"Error: No Wikipedia page found for title '{self.title}' in language '{self.lang}'."
            
            search_index = search.build_search_index(source)
            documents = search_index.similarity_search(question, k=1)
            
            if not documents:
                return "I couldn't find relevant information. SOURCES: None"

            chain = qa_chain.get_qa_chain()
            result = chain(
                {"input_documents": documents, "question": question},
                return_only_outputs=True
            )
            return result
        
        except Exception as e:
            return f"An error occurred: {str(e)}"