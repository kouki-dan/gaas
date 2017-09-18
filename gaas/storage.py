

from abc import ABCMeta, abstractmethod
import hashlib
import os

from git import Repo
from git.exc import GitCommandError

class AbstractGitCredential(metaclass=ABCMeta):
    
    @abstractmethod
    def setup(self):
        pass

class SSHGitCredential(AbstractGitCredential):

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def setup(self, repo_dir, repo):
        with open(repo_dir+"/"+"gaas_ssh_key", "w") as f:
            f.write(self.secret_key)
        os.chmod(repo_dir+"/"+"gaas_ssh_key", 0o600)
        repo.git.update_environment(GIT_SSH_COMMAND='ssh -i ./gaas_ssh_key -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o IdentitiesOnly=yes')

class GitCredential:

    def __init__(self, credential):
        self.credential = credential

    def setup_repo(self, repo_dir, repo):
        self.credential.setup(repo_dir, repo)


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
        git_credential.setup_repo(self.repo_dir, self.repo)
        try:
            self.repo.delete_remote("origin")
        except GitCommandError:
            pass
        self.repo.create_remote("origin", repo_url)
        self.repo.remotes.origin.fetch()
        # TODO: head to remote/origin/master/head and push initial commit if it is initialized.

        if len(self.repo.branches) == 0:
            readme_file = self.repo_dir+"/README.md"
            with open(readme_file, "w") as readme:
                readme.write("# Gaaaas")

            self.repo.index.add(["README.md"])
            self.repo.index.commit("Initialize repo")

    def open(self, filepath, mode="r"):
        return open(self._repo_path(filepath), mode)

    def commit(self, filepath_list, message="no message"):
        self.repo.index.add(filepath_list)
        self.repo.index.commit(message)

    def _repo_path(self, filepath):
        return self.repo_dir+"/"+filepath

