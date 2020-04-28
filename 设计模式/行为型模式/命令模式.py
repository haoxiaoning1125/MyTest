# coding=utf-8

import os

verbose = True


def delete_file(path):
    if verbose:
        print 'delete file {}'.format(path)
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print 'create file {}'.format(self.path)
        with open(self.path, mode='w') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class RenameFile:
    def __init__(self, path_src, path_dst):
        self.src = path_src
        self.dst = path_dst

    def execute(self):
        if verbose:
            print 'renaming {} to {}'.format(self.src, self.dst)
        os.rename(self.src, self.dst)

    def undo(self):
        if verbose:
            print 'renaming {} back to {}'.format(self.dst, self.src)
        os.rename(self.dst, self.src)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print 'reading file {}'.format(self.path)
        with open(self.path, mode='r') as in_file:
            print in_file.read()


if __name__ == '__main__':
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd.execute)
    print commands
