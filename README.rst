| |pypi| |license| |docs|
| |sonar_maintainability| |sonar_reliability| |sonar_security|

Supports Python ``2.7+`` and ``3.4+``.

Module based on `steam <https://github.com/ValvePython/steam/>`_
for interacting with Dota2's Game Coordinator. If you've used
`node-dota2 <https://github.com/RJacksonm1/node-dota2>`_ then
this module should feel right at home. Check out the documentation
to get started.

**Documentation**: http://dota2.readthedocs.io

Contributions and suggestion are always welcome.


Installation
------------

Install latest version from PYPI::

    pip install dota2

Install the current dev version from ``github``::

    pip install git+https://github.com/ValvePython/dota2
    
    # if you are installing over existing install
    # note: "only-if-needed" will only update dependecies if needed
    pip install -U --upgrade-strategy only-if-needed git+https://github.com/ValvePython/dota2



.. |pypi| image:: https://img.shields.io/pypi/v/dota2.svg?style=flat&label=latest%20version
    :target: https://pypi.python.org/pypi/dota2
    :alt: Latest version released on PyPi

.. |license| image:: https://img.shields.io/pypi/l/dota2.svg?style=flat&label=license
    :target: https://pypi.python.org/pypi/dota2
    :alt: MIT License

.. |docs| image:: https://readthedocs.org/projects/dota2/badge/?version=latest
    :target: http://dota2.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_dota2&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_dota2
    :alt: SonarCloud Rating

.. |sonar_reliability| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_dota2&metric=reliability_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_dota2
    :alt: SonarCloud Rating

.. |sonar_security| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_dota2&metric=security_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_dota2
    :alt: SonarCloud Rating
