#!C:\Users\jjwri\PycharmProjects\mapping\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ogrtools==0.7.3','console_scripts','ogr'
__requires__ = 'ogrtools==0.7.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ogrtools==0.7.3', 'console_scripts', 'ogr')()
    )
