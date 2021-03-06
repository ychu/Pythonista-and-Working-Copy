#!/usr/bin/env python3
# coding: utf-8

# Appex script to copy a git file, folder, or repo from the Working Copy app

import appex, os, shutil

TARGET_DIR = ''

wc_dir = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/{}'.format(TARGET_DIR)
from_wc = os.path.abspath(os.path.expanduser(wc_dir))


def main():
    if appex.is_running_extension():
        file_paths = appex.get_file_paths()
        assert len(file_paths) == 1, 'Invalid file paths: {}'.format(file_paths)
        srce_path = file_paths[0]
        if '/tmp/' in srce_path:
            dest_base = srce_path.split('/tmp/')[-1]
        else:
            dest_base = srce_path.split('/Repositories/')[-1]
        dest_path = os.path.join(from_wc, dest_base)
        file_path, file_name = os.path.split(dest_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        if os.path.isdir(srce_path):
            shutil.rmtree(dest_path, ignore_errors=True)
            shutil.copytree(srce_path, dest_path)
        else:
            shutil.copy2(srce_path, dest_path)
        print('{} was copied to {}/{}'.format(file_name, TARGET_DIR, dest_base))
    else:
        print('''* In Working Copy app select a repo, file, or directory to be
copied into Pythonista.  Click the Share icon at the upperight.  Click Run
Pythonista Script.  Pick this script and click the run button.  When you return
to Pythonista the files should be in the 'from Working Copy'
directory.'''.replace('\n', ' ').replace('.  ', '.\n* '))

if __name__ == '__main__':
    main()
