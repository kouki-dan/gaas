

from abc import ABCMeta
import hashlib
import os

from git import Repo

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
        self.repo_dir = "repo/" + hashlib.sha224(repo_url.encode("utf-8")).hexdigest()[:10]
        try:
            os.mkdir(self.repo_dir)
        except FileExistsError:
            pass
        self.repo = Repo.init(self.repo_dir)
        if len(self.repo.branches) == 0:
            readme_file = self.repo_dir+"/README.md"
            with open(readme_file, "w") as readme:
                readme.write("# Gaaaas")

            self.repo.index.add(["README.md"])
            self.repo.index.commit("Initialize repo")

    def add_file(self, filepath):
        pass

    def commit(self):
        pass

