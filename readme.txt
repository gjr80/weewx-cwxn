cwxn - Cumulus wxnow
Copyright 2014 Matthew Wall

cwxn is a WeeWX extension that emits a wxnow.txt file in the format
specified by Cumulus

  https://cumuluswiki.org/a/Wxnow.txt

Installation instructions:

1.  Download the extension:

    $ wget -P /var/tmp https://github.com/gjr80/weewx-cwxn/releases/download/v0.6/cwxn-0.6.tar.gz

2.  Install the extension:

    -   for setup.py installs:

        $ /home/weewx/bin/wee_extension --install=/var/tmp/cwxn-0.6.tar.gz

    -   for package installs:

        $ wee_extension --install=/var/tmp/cwxn-0.6.tgz

3.  Restart WeeWX:

    $ sudo /etc/init.d/weewx restart

    or

    $ sudo service weewx restart

    or

    $ sudo systemctl restart weewx
