baldrick_circleci
=================

..
   .. image:: https://img.shields.io/pypi/v/baldrick_circleci.svg
       :target: https://pypi.python.org/pypi/baldrick_circleci
       :alt: Latest PyPI version

A plugin for baldrick for listening to circleci webhooks.

Usage
-----

This plugin supports registration of handlers for CircleCI build webhooks.

To use it in your baldrick project, import it into your ``webapp.py`` and register it as a blueprint::

  from baldrick_circleci import circleci

  app.register_blueprint(circleci)


This package also ships with an artifact checker which when imported will post commit statues with links to configured artifacts (by default it will check for the sphinx html build in ``html/index.html``). To enable this import it into your ``webapp.py``::

  from baldrick_circleci import artifact_status


The artifact checker is configured in a section of your ``pyproject.toml`` file like this::


  [ tool.botname.circleci_artifacts.sphinx ]
    url = "html/index.html"
    message = "Click details to preview the documentation build"

  [ tool.botname.circleci_artifacts.sphinx_pdf ]
    url = "pdf/pdf.pdf"
    message = "Click details to preview the pdf documentation build"

You can define as many `tool.botname.circleci_artifacts.name` sections as you
wish, each should have a `url` and a `message` key. The url is a substring that
will be matched against the full artifact URL. The message will be posted as a
commit status, with the `name` being the context used for the commit status.


Installation
------------

Install with pip::

  pip install git+https://github.com/Cadair/baldrick_circleci

Requirements
^^^^^^^^^^^^

- baldrick
- requests

Compatibility
-------------

Python 3.6+

Licence
-------

BSD 3-clause

Authors
-------

`baldrick_circleci` was written by `Stuart Mumford <stuart@cadair.com>`_.
