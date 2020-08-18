import unittest

from TransferGenerator.TransferProcessorPlugins.ClassDeclarationProcessorPlugin import ClassDeclarationProcessorPlugin
from TransferGenerator.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class TestClassDeclarationProcessorPlugin(unittest.TestCase):
    def setUp(self) -> None:
        self.__uut = ClassDeclarationProcessorPlugin()

    def test_process_happy(self):
        transfer = FieldCollectionTransfer()
        transfer.set_name('test')

        expected_result = 'class test:\n'
        actual_result = self.__uut.process(transfer)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
