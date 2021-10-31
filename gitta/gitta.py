# -*- coding: utf-8 -*-
"""bootstrap.bootstrap: provides entry point main()."""

import os, sys
from getpass import getpass

__version__ = "0.3.0"

import sys, subprocess


# from .stuff import Stuff
class Gitta():
    def __init__(self,
                 components='',
                 user='suredream',
                 repo='mlops',
                 verbose=False):
        self.user = user
        self.repo = f'https://github.com/{user}/{repo}'
        self.token = self.get_token()
        self.verbose = verbose

    def __call__(self, src, print_stdout=False, pip=''):
        dest = os.path.expanduser(src.replace('~', '~/.'))
        if not src or os.path.isfile(dest):
            return  # skip if already done or src is None
        conn_str = self.repo.replace(
            'https://github',
            f'https://{self.token}@raw.githubusercontent') + f'/main/{src}'
        if self.verbose:
            print(conn_str)
        content = os.popen(f'curl -s {conn_str}').read()
        assert content != '404: Not Found', f'{src} not found in gitta!'
        if print_stdout:
            print(content)
        else:  # export to same filename
            if src.startswith('~'):
                folders = dest.split('/')
                if len(folders) > 1:
                    for i, dname in enumerate(folders):
                        dirname = '/'.join(folders[:i]) if i else dname
                        if dirname and not os.path.exists(dirname):
                            os.mkdir(dirname)
            with open(dest, 'w') as f:
                f.write(content)
        if pip:
            install_cmd = [sys.executable, "-m", "pip", "-q", "install"
                           ] + pip.split()
            subprocess.check_call(install_cmd)

    def read(self, src):
        dest = os.path.expanduser(src.replace('~', '~/.'))
        if os.path.isfile(dest):
            return open(dest).read().rstrip()

    def get_token(self, cred='~/.git_cred'):
        cred = os.path.expanduser(cred)
        if os.path.isfile(cred):  # need auth
            token = open(cred).read().rstrip()
        else:
            token = getpass('token: ')
            with open(cred, 'w') as fout:
                fout.write(token)
        return token

    def get(self, repo, keep_dir_level=False):
        repo_name = f"https://{self.token}@github.com/suredream/{repo}"
        os.system(
            'git config --global user.email "junxiong360@gmail.com" && git config --global user.name "Jun Xiong"'
        )
        os.system(f"git clone {repo_name}")
        if not keep_dir_level:
            os.system(
                f"mv {repo}/.git . && rm -rf {repo} && git reset --hard"
            )

    def push(self, repo, amend_commit=False):
        os.system('git add -u')
        if amend_commit:
            os.system("git commit --amend --reuse-message HEAD")
        os.system(
            f'git pull && git push "https://{self.token}@github.com/suredream/{repo}.git"'
        )


help_text = """
Usage: 

$ pip install -q git+https://git@github.com/suredream/guitar.git@master
"""

def main():
    print('gitta is comming')
    run = Gitta(verbose=True)
    dict_dep = {'aws': ('~aws/credentials', 'awscli')}
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd in ['clone', 'get']:
            # clone --> keep_dir_level
            # get --> remove level-1-dir
            run.get(sys.argv[2], keep_dir_level=cmd == 'clone')
        elif cmd in ['push', 'update']:
            # push: new commit
            # update: amend
            run.push(amend_commit=cmd == 'update')
        else:  # fetch cred & snippets
            for cmd in sys.argv[1:]:
                if cmd.startswith('-'): # options
                    continue
                elif cmd in dict_dep:
                    cred, packages = dict_dep[cmd]
                    run(cred, pip=packages)
                else:  # snippets in mlops
                    if '-o' in sys.argv[1:]:
                        run(cmd)
                    else:
                        run(cmd, print_stdout=True)
    else:
        print(help_text)