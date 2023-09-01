===============================
Merge proposal Review Inspector
===============================


.. image:: https://img.shields.io/pypi/v/launchpad_mp_review_inspector.svg
        :target: https://pypi.python.org/pypi/launchpad_mp_review_inspector

.. image:: https://img.shields.io/travis/philroche/launchpad_mp_review_inspector.svg
        :target: https://travis-ci.com/philroche/launchpad_mp_review_inspector

.. image:: https://readthedocs.org/projects/launchpad-mp-review-inspector/badge/?version=latest
        :target: https://launchpad-mp-review-inspector.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




CLI tool to view the MPs that you have reviewed for a given launchpad project.


* Free software: GNU General Public License v3
* Documentation: https://launchpad-mp-review-inspector.readthedocs.io.

Usage
-----

Find the Merge Proposals that launchpad.net user philroche has reviewed for the lp:livecd-rootfs.::

    cli.py --reviewer-launchpad-username philroche --launchpad-git-repo lp:livecd-rootfs

Find the Merge Proposals that launchpad.net user philroche has proposed and has also self reviewed for the lp:livecd-rootfs.::

    cli.py --reviewer-launchpad-username philroche --proposer-launchpad-username philroche --launchpad-git-repo lp:livecd-rootfs

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
