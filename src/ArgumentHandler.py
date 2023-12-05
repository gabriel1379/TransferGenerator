from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from argparse import ArgumentParser


class ArgumentHandler:
    ARG_SHORT_INPUT_PATH = '-i'
    ARG_LONG_INPUT_PATH = '--input_path'
    ARG_SHORT_OUTPUT_PATH = '-o'
    ARG_LONG_OUTPUT_PATH = '--output_path'

    def __init__(self, arg_parser: 'ArgumentParser'):
        self.__arg_parser: 'ArgumentParser' = arg_parser
        self.__args: dict = None

        self.__boot()

    def __boot(self):
        if self.__args is not None:
            return

        self.__arg_parser.add_argument(
            self.ARG_SHORT_INPUT_PATH,
            self.ARG_LONG_INPUT_PATH,
            type=str,
            help='Provide a custom input path from which to read the source XML files.'
        )
        self.__arg_parser.add_argument(
            self.ARG_SHORT_OUTPUT_PATH,
            self.ARG_LONG_OUTPUT_PATH,
            type=str,
            help='Provide a custom output path where to put the generated transfer class files.'
        )

        self.__args = vars(self.__arg_parser.parse_args())

    def get_input(self) -> str:
        return self.__args.get(self.ARG_LONG_INPUT_PATH.lstrip('--'))

    def get_output(self) -> str:
        return self.__args.get(self.ARG_LONG_OUTPUT_PATH.lstrip('--'))
