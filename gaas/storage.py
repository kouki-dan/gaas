

from abc import ABCMeta

class AbstractGitCredential:
    __metaclass__ = ABCMeta
    pass

class SSHGitCredential(AbstractGitCredential):

    def __init__(self, public_key):
        self.public_key = public_key

class GitCredential:

    def __init__(self, credential):
        self.credential = credential

    @staticmethod
    def ssh_key(key):
        return GitCredential(SSHGitCredential(key))

class Storage:
    def __init__(self, repo_url, git_credential=None):
        pass

    def add_file(self, filepath):
        pass

    def commit(self):
        pass

