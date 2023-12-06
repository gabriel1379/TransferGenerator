import unittest

from TransferGenerator.TransferProcessorPlugins.SetterProcessorPlugin import SetterProcessorPlugin
from TransferGenerator.Transfers.FieldCollectionTransfer import FieldCollectionTransfer
from TransferGenerator.Transfers.FieldTransfer import FieldTransfer


class TestSetterProcessorPlugin(unittest.TestCase):
    def setUp(self) -> None:
        self.__uut = SetterProcessorPlugin()

    def test_process_happy(self):
        field_transfer_first = self.__build_field_transfer('test_field', 'str')
        field_transfer_second = self.__build_field_transfer('another', 'int')

        field_collection = FieldCollectionTransfer()
        field_collection.set_name('TestTransfer')
        field_collection.add_field(field_transfer_first)
        field_collection.add_field(field_transfer_second)

        expected_result = ('    def set_test_field(self, test_field: str) -> \'TestTransfer\':\n'
                           '        self.__test_field = test_field\n'
                           '        return self\n'
                           '\n'
                           '    def set_another(self, another: int) -> \'TestTransfer\':\n'
                           '        self.__another = another\n'
                           '        return self\n'
                           '\n')
        actual_result = self.__uut.process(field_collection)

        self.assertEqual(expected_result, actual_result)

    def __build_field_transfer(self, field_name: str, field_type: str) -> FieldTransfer:
        field_transfer = FieldTransfer()
        field_transfer.set_field_name(field_name)
        field_transfer.set_field_type(field_type)

        return field_transfer


if __name__ == '__main__':
    unittest.main()
