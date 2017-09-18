
import unittest
from unittest import mock
from gaas.storage import Storage, GitCredential

class TestTest(unittest.TestCase):

    def setUp(self):
        self.credential = GitCredential.ssh_key("private_key")
        pass

    def test_storage_can_initialize(self):
        with mock.patch("gaas.storage.Repo") as patcher:
            storage = Storage("git@example.com/git-repo/url", self.credential)
            self.assertTrue(storage)

