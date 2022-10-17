import logging

from pathlib import Path
from typing import List
from argparse import ArgumentParser

from oak_build.app_logging import DEFAULT_LEVEL, LEVELS, init_logging
from oak_build.oak_file import DEFAULT_OAK_FILE, OakFileLoader


class App:
    def __init__(self, args: List[str]):
        parser = App._init_arg_parser()
        parsed_args = parser.parse_args(args)

        init_logging(parsed_args.log_level)

        self.oak_file: Path = parsed_args.file

    def run(self) -> int:
        self._load_oak_file()
        return 0

    def _load_oak_file(self) -> int:
        file_description = OakFileLoader.load_file(self.oak_file)
        if file_description.is_ok:
            return 0
        else:
            errors = file_description.unwrap_err()
            logging.error(f"Found {len(errors)} errors:")
            for error in errors:
                logging.error(error)
            return 1

    @staticmethod
    def _init_arg_parser() -> ArgumentParser:
        parser = ArgumentParser(prog="oak")
        parser.add_argument("-l", "--log-level", default=DEFAULT_LEVEL, choices=LEVELS)
        parser.add_argument("-f", "--file", default=DEFAULT_OAK_FILE, type=Path)
        return parser



