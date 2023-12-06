from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class ProcessorPluginInterface(ABC):
    @abstractmethod
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        pass
