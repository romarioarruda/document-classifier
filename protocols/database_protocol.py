from abc import ABC, abstractmethod
from typing import Dict, Pattern, List
from models.field_pattern import FieldPattern


class DatabaseProtocol(ABC):
    @abstractmethod
    def _load_patterns(self) -> None:
        raise NotImplementedError('Final object not implemented')


    @abstractmethod
    def get_patterns(self) -> Dict[str, Pattern]:
        raise NotImplementedError('Final object not implemented')
    

    @abstractmethod
    def get_list_patterns(self) -> Dict[str, List[FieldPattern]]:
        raise NotImplementedError('Final object not implemented')
    
