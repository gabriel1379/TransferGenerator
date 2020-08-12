from Processors.ClassDeclarationProcessor import ClassDeclarationProcessor
from Processors.FieldProcessor import FieldProcessor
from Processors.GetterProcessor import GetterProcessor
from Processors.SetterProcessor import SetterProcessor


class Processors:
    def get_processors(self):
        return [
            ClassDeclarationProcessor(),
            FieldProcessor(),
            SetterProcessor(),
            GetterProcessor(),
        ]
