import unittest

from . import test_app


class TestHello(unittest.TestCase):
    def test_default(self):
        runner = test_app.test_cli_runner()
        result = runner.invoke(args=['hello'])
        self.assertEqual('Hello, World!\n', result.output)

    def test_set_name(self):
        runner = test_app.test_cli_runner()
        result = runner.invoke(args=['hello', '--name', 'foo'])
        self.assertEqual('Hello, foo!\n', result.output)
