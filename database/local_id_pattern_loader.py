import re
from typing import Dict, Pattern

class LocalIdPatternLoader:
    _instance = None

    def __new__(self, patterns_path: str):
        if self._instance is None:
            self.patterns_dictionary: Dict[str, Pattern] = {}
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
            
                columns = line.split(';', 1)

                if (len(columns) <=1):
                    continue

                doc_id = columns[0]
                pattern = columns[1]

                self.patterns_dictionary[doc_id] = re.compile(pattern)

    
    def get_patterns(self):
        return self.patterns_dictionary

