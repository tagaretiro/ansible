import requests
import subprocess as sub
import shutil
import os

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def extract_7z_job():
    process_7z = sub.Popen(['7za.exe', 'e', 'ansible.zip', '-oTEMP', '-y'])
    process_7z.communicate()

def run_install():
    os.chdir('TEMP')
    process_7z = sub.Popen(['python.exe', 'setup.py', 'install'])
    process_7z.communicate()

download_url('https://github.com/ansible/ansible/archive/v2.9.2.zip', 'ansible.zip')
extract_7z_job()
shutil.copy2('template\\setup.py', 'TEMP')
run_install()