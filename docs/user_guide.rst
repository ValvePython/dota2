User Guide
**********

This part of the documentation is a quick start for writing applications that
interact with the game coordinator for Dota 2.


Initialization
==============

Below is a example how to login and get a session with game coordinator.
See `steam's docs <http://steam.readthedocs.io/en/stable/>`_ 
for details about :class:`SteamClient <steam:steam.client.SteamClient>`.

.. note::
    You won't see any output running the code above.
    In order to peek inside we need to setup debug logging.
    See the :ref:`logging_config` section


.. code:: python

    from steam import SteamClient
    from dota2 import Dota2Client

    client = SteamClient()
    dota = Dota2Client(client)

    @client.on('logged_on')
    def start_dota():
        dota.launch()

    @dota.on('ready')
    def do_dota_stuff():
        # talk to GC

    client.cli_login()
    client.run_forever()


Working with events
===================

This module makes use of `gevent <http://www.gevent.org/>`_
and `gevent-eventemitter <https://github.com/rossengeorgiev/gevent-eventemitter>`_.
Working with events is similiar to ``EventEmitter`` in javascript.
Nevertheless, here is quick rundown.

To catch an event we need to register a callback

.. code:: python

    @dota.on('my event')
    def do_stuff(a, b):
        print "Hey!"

    dota.on('my event', do_stuff)
    dota.once('my event', do_stuff)  # call do_stuff just one time
    dota.wait_event('my event')      # blocks and returns arguments, if any

.. note::
    ``wait_event`` may block forever, so use the ``timeout`` parameter

Emitting an event is simple

.. code:: python

    dota.emit("my event")
    dota.emit("my event", 1, [3,4,5])  # optional arguments


That's it. For more details see `gevent-eventemitter <https://github.com/rossengeorgiev/gevent-eventemitter>`_.


Fetch player profile card
=========================

You've probably seen the profile cards in Dota 2.
They contain player selected stats, such trophies, number of matches, or MMR.

We can request that data using an API from the :doc:`dota2.features` module.

Let's get Dendi's profile card. All we need is his account id, which is ``70388657``.

.. code:: python

    @dota.on('ready')
    def fetch_profile_card():
        dota.request_profile_card(70388657)

    @dota.on('profile_card'):
    def print_profile_card(account_id, profile_card):
        if account_id == 70388657:
            print str(profile_card)

The profile card request also happens to be a job.
``request_profile_card`` returns a ``job id`` and we can wait for it instead.
However, we will not get the same parameters as from ``profile_card``

.. note::
    Listening for the ``job id``` will only give you one arugment: the protobuf message

.. code:: python

    @dota.on('ready')
    def fetch_profile_card():
        jobid = dota.request_profile_card(70388657)
        profile_card = dota.wait_msg(jobid, timeout=10)

        if profile_card:
            print str(profile_card)

.. note::
    Not every request returns a ``job id``, see the API documentation for details

Running the code above will output something like this:

.. code::

    account_id: 70388657
    background_def_index: 0
    slots {
      slot_id: 0
      stat {
        stat_id: k_eStat_FirstMatchDate
        stat_score: 1314309005
      }
    }
    slots {
      slot_id: 1
      stat {
        stat_id: k_eStat_SoloRank
        stat_score: 6775


.. _logging_config:

Configure console logging
=========================

Here is a basic configuration to get debug messages in the console.

.. code:: python

    import logging

    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

The we run the program and the console ouput should look something like this:

.. code::

    [2016-01-01 12:34:56,000] DEBUG CMClient: Connect initiated.
    [2016-01-01 12:34:56,000] DEBUG Connection: Attempting connection to ('208.78.164.13', 27018)
    [2016-01-01 12:34:56,000] DEBUG Connection: Connected.
    [2016-01-01 12:34:56,000] DEBUG CMClient: Emit event: 'connected'
    [2016-01-01 12:34:56,000] DEBUG SteamClient: Emit event: 'connected'
    [2016-01-01 12:34:56,000] DEBUG SteamClient: Attempting login
    [2016-01-01 12:34:56,000] DEBUG CMClient: Incoming: <Msg <EMsg.ChannelEncryptRequest: 1303>>
    [2016-01-01 12:34:56,000] DEBUG CMClient: Emit event: <EMsg.ChannelEncryptRequest: 1303>
    ...


