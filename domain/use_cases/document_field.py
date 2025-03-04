from domain.protocols.database_protocol import DatabaseProtocol

class DocumentField:

    def __init__(self, db: DatabaseProtocol):
        self.patterns_dictionary = db.get_list_patterns()


    def get_fields(self, doc_type: str, text: str):
        dict_output = {}
        regex_fields = self.patterns_dictionary.get(doc_type)

        if regex_fields is None:
            return dict_output

        for item in regex_fields:
            search = item["pattern"].search(text)
            result = search.groups() if not search is None else []

            dict_output[item["fieldName"]] = str(result[0]).replace('\n', '') if len(result) > 0 else None
        
        return dict_output
        
