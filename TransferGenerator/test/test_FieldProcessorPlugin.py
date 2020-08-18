import unittest

from TransferGenerator.TransferProcessorPlugins.FieldProcessorPlugin import FieldProcessorPlugin
from TransferGenerator.Transfers.FieldCollectionTransfer import FieldCollectionTransfer
from TransferGenerator.Transfers.FieldTransfer import FieldTransfer


class TestFieldProcessorPlugin(unittest.TestCase):
    def setUp(self) -> None:
        self.__uut = FieldProcessorPlugin()

    def test_process_happy(self):
        field_transfer_first = self.__build_field_transfer('test_field', 'str')
        field_transfer_second = self.__build_field_transfer('another', 'int')

        field_collection = FieldCollectionTransfer()
        field_collection.add_field(field_transfer_first)
        field_collection.add_field(field_transfer_second)

        expected_result = ('    def __init__(self):\n'
                           '        self.__test_field: str = None\n'
                           '        self.__another: int = None\n'
                           '\n'
                           )
        actual_result = self.__uut.process(field_collection)

        self.assertEqual(expected_result, actual_result)

    def __build_field_transfer(self, field_name: str, field_type: str) -> FieldTransfer:
        field_transfer = FieldTransfer()
        field_transfer.set_field_name(field_name)
        field_transfer.set_field_type(field_type)

        return field_transfer


if __name__ == '__main__':
    unittest.main()
