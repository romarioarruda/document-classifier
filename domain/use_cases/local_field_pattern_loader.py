import re
from typing import Dict, List
from domain.dtos.field_pattern import FieldPatternDTO


class LocalFieldsPatternLoader:
    _instance = None

    def __new__(self, patterns_path: str):
        if self._instance is None:
            self.patterns_dictionary: Dict[str, List[FieldPatternDTO]] = {}
            self.patterns_path = patterns_path
            self._load_patterns(self)
            self._instance = super().__new__(self)

        return self._instance


    def _load_patterns(self):
        with open(self.patterns_path, mode='r') as file:
            for line in file:
                line = line.strip()
                if (not line):
                    continue
            
                columns = line.split(';', 3)

                if (len(columns) <=2):
                    continue

                doc_type = columns[0]
                field = columns[1]
                regex = columns[2]

                if self.patterns_dictionary.get(doc_type) is None:
                    self.patterns_dictionary.setdefault(doc_type, [])
                
                self.patterns_dictionary[doc_type].append({ "fieldName": field, "pattern": re.compile(regex) })
                    

    
    def get_list_patterns(self):
        return self.patterns_dictionary

