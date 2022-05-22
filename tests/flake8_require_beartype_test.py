from __future__ import annotations

import ast
import unittest
from pathlib import Path

from flake8_require_beartype import Plugin

SAMPLE_FILE = Path(__file__).parent / 'data' / 'input.txt'


class TestRequireBeartype(unittest.TestCase):

    def setUp(self):
        with SAMPLE_FILE.open('r', encoding='utf-8') as file:
            self.file = file.read()

    def test_one(self):
        errors = {
            '{}:{}: {}'.format(
                *r,
            ) for r in Plugin(ast.parse(self.file)).run()
        }
        valid = {
            '19:4: RBT002 Method missing @beartype',
            '22:4: RBT002 Method missing @beartype',
            '26:4: RBT002 Method missing @beartype',
            '30:4: RBT002 Method missing @beartype',
            '34:4: RBT002 Method missing @beartype',
            '38:4: RBT002 Method missing @beartype',
            '41:4: RBT002 Method missing @beartype',
            '52:0: RBT001 Function missing @beartype',
            '56:0: RBT001 Function missing @beartype',
            '60:0: RBT001 Function missing @beartype',
        }
        self.assertEqual(errors, valid)


if __name__ == '__main__':
    unittest.main()
