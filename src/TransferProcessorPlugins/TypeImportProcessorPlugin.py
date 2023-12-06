from typing import TYPE_CHECKING, Dict, List

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class TypeImportProcessorPlugin(ProcessorPluginInterface):
    TYPE_SOURCE_OTHER = 'other'
    TYPE_SOURCE_TYPING = 'typing'
    TYPES_BUILTIN = ['int', 'float', 'complex', 'list', 'tuple', 'range', 'str', 'bytes', 'bytearray', 'memoryview', 'set', 'frozenset', 'dict', 'bool']
    TYPES_TYPING = ['List', 'Dict']

    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        if not self.__is_import_needed(field_collection):
            return ''

        field_code = 'from typing import TYPE_CHECKING'

        types_to_import = self.__extract_types_to_import(field_collection)
        if len(types_to_import.get(self.TYPE_SOURCE_TYPING)) > 0:
            for field_type in types_to_import.get(self.TYPE_SOURCE_TYPING):
                field_code += f", {field_type}"

        field_code += '\n\n'

        # TODO: Find out the source of the other imports, so the proper 'from ... import ...' can be generated for them.
        if len(types_to_import.get(self.TYPE_SOURCE_OTHER)) > 0:
            field_code += 'if TYPE_CHECKING:\n'

            for field_type in types_to_import.get(self.TYPE_SOURCE_OTHER):
                field_code += f"    from ... import {field_type}\n"  # Placeholder code, needs development, see TODO above

            field_code += '\n\n'

        return field_code

    def __is_import_needed(self, field_collection: 'FieldCollectionTransfer') -> bool:
        for field in field_collection.get_fields():
            if field.get_field_type() not in self.TYPES_BUILTIN:
                return True

        return False

    def __extract_types_to_import(self, field_collection: 'FieldCollectionTransfer') -> Dict[str, str]:
        field_types_found = {
            self.TYPE_SOURCE_TYPING: [],
            self.TYPE_SOURCE_OTHER: [],
        }

        for field in field_collection.get_fields():
            field_types_to_analyze = self.__split_generics(field.get_field_type())
            for field_type in field_types_to_analyze:
                if field_type in self.TYPES_BUILTIN:
                    continue

                if field_type in self.TYPES_TYPING:
                    field_types_found[self.TYPE_SOURCE_TYPING].append(field_type)
                    continue

                field_types_found[self.TYPE_SOURCE_OTHER].append(field_type)

        return field_types_found

    def __split_generics(self, field_type: str) -> List[str]:
        field_type = field_type.replace('[', ',')
        field_type = field_type.replace(']', '')
        field_type = field_type.replace('\'', '')
        field_type = field_type.replace(' ', '')

        return field_type.split(',')

    def __is_builtin_type(self, field_type: str) -> bool:
        return field_type in self.TYPES_BUILTIN

    def __is_typing_type(self, field_type: str) -> bool:
        return field_type in self.TYPES_TYPING
