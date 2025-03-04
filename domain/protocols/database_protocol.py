from abc import ABC, abstractmethod
from typing import Dict, Pattern, List
from domain.dtos.field_pattern import FieldPatternDTO


class DatabaseProtocol(ABC):
    @abstractmethod
    def _load_patterns(self) -> None:
        raise NotImplementedError('Final object not implemented')


    @abstractmethod
    def get_patterns(self) -> Dict[str, Pattern]:
        raise NotImplementedError('Final object not implemented')
    

    @abstractmethod
    def get_list_patterns(self) -> Dict[str, List[FieldPatternDTO]]:
        raise NotImplementedError('Final object not implemented')
    
