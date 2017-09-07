
import unittest
from gaas.storage import Storage, GitCredential

class TestTest(unittest.TestCase):

    def setUp(self):
        self.credential = GitCredential.ssh_key("public_key")
        pass

    def test_storage_can_initialize(self):
        storage = Storage("git@example.com/git-repo/url", self.credential)
        self.assertTrue(storage)

