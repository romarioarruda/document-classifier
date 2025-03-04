from domain.protocols.database_protocol import DatabaseProtocol

class DocumentIdentify:

    def __init__(self, db: DatabaseProtocol):
        self.patterns_dictionary = db.get_patterns()


    def get_classification(self, text: str) -> str:
        """
        Returns the document classification or 'unknown' if not recognized.
        """
        for doc_type, pattern in self.patterns_dictionary.items():
            if pattern.search(text):
                return doc_type
        
        return "unknown"

