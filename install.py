"""
Installer for cwxn extension

Forked from weewx-cwxn v0.4 Copyright 2014 Matthew Wall
"""

from setup import ExtensionInstaller


def loader():
    return CWXNInstaller()


class CWXNInstaller(ExtensionInstaller):
    def __init__(self):
        super(CWXNInstaller, self).__init__(
            version="0.6",
            name='cwxn',
            description='Emit a Cumulus wxnow.txt file.',
            author="Matthew Wall",
            author_email="mwall.weewx@gmail.com",
            process_services='user.cwxn.CumulusWXNow',
            config={
                'CumulusWXNow' : {
                    'filename': '/var/tmp/wxnow.txt'}},
            files=[('bin/user', ['bin/user/cwxn.py'])]
            )
