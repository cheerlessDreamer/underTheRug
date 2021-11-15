from setuptools import setup

# To build a new application, run: python3 setup.py py2app

APP = ['underTheRug.py']
DATA_FILES = [('', ['rug.png']),
              ('', ['Hide.sh']),
              ('', ['Show.sh']),
              ]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.png',
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='Under The Rug',
    author='Danny Taylor',
    author_email='danny@dannytaylor.se',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps']
)
