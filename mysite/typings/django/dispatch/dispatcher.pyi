"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
logger = ...
NONE_ID = ...
NO_RECEIVERS = ...
class Signal:
    """
    Base class for all signals

    Internal attributes:

        receivers
            { receiverkey (id) : weakref(receiver) }
    """
    def __init__(self, use_caching=...) -> None:
        """
        Create a new signal.
        """
        ...
    
    def connect(self, receiver, sender=..., weak=..., dispatch_uid=...):
        """
        Connect receiver to sender for signal.

        Arguments:

            receiver
                A function or an instance method which is to receive signals.
                Receivers must be hashable objects. Receivers can be
                asynchronous.

                If weak is True, then receiver must be weak referenceable.

                Receivers must be able to accept keyword arguments.

                If a receiver is connected with a dispatch_uid argument, it
                will not be added if another receiver was already connected
                with that dispatch_uid.

            sender
                The sender to which the receiver should respond. Must either be
                a Python object, or None to receive events from any sender.

            weak
                Whether to use weak references to the receiver. By default, the
                module will attempt to use weak references to the receiver
                objects. If this parameter is false, then strong references will
                be used.

            dispatch_uid
                An identifier used to uniquely identify a particular instance of
                a receiver. This will usually be a string, though it may be
                anything hashable.
        """
        ...
    
    def disconnect(self, receiver=..., sender=..., dispatch_uid=...):
        """
        Disconnect receiver from sender for signal.

        If weak references are used, disconnect need not be called. The receiver
        will be removed from dispatch automatically.

        Arguments:

            receiver
                The registered receiver to disconnect. May be none if
                dispatch_uid is specified.

            sender
                The registered sender to disconnect

            dispatch_uid
                the unique identifier of the receiver to disconnect
        """
        ...
    
    def has_listeners(self, sender=...):
        ...
    
    def send(self, sender, **named):
        """
        Send signal from sender to all connected receivers.

        If any receiver raises an error, the error propagates back through send,
        terminating the dispatch loop. So it's possible that all receivers
        won't be called if an error is raised.

        If any receivers are asynchronous, they are called after all the
        synchronous receivers via a single call to async_to_sync(). They are
        also executed concurrently with asyncio.gather().

        Arguments:

            sender
                The sender of the signal. Either a specific object or None.

            named
                Named arguments which will be passed to receivers.

        Return a list of tuple pairs [(receiver, response), ... ].
        """
        ...
    
    async def asend(self, sender, **named):
        """
        Send signal from sender to all connected receivers in async mode.

        All sync receivers will be wrapped by sync_to_async()
        If any receiver raises an error, the error propagates back through
        send, terminating the dispatch loop. So it's possible that all
        receivers won't be called if an error is raised.

        If any receivers are synchronous, they are grouped and called behind a
        sync_to_async() adaption before executing any asynchronous receivers.

        If any receivers are asynchronous, they are grouped and executed
        concurrently with asyncio.gather().

        Arguments:

            sender
                The sender of the signal. Either a specific object or None.

            named
                Named arguments which will be passed to receivers.

        Return a list of tuple pairs [(receiver, response), ...].
        """
        ...
    
    def send_robust(self, sender, **named):
        """
        Send signal from sender to all connected receivers catching errors.

        If any receivers are asynchronous, they are called after all the
        synchronous receivers via a single call to async_to_sync(). They are
        also executed concurrently with asyncio.gather().

        Arguments:

            sender
                The sender of the signal. Can be any Python object (normally one
                registered with a connect if you actually want something to
                occur).

            named
                Named arguments which will be passed to receivers.

        Return a list of tuple pairs [(receiver, response), ... ].

        If any receiver raises an error (specifically any subclass of
        Exception), return the error instance as the result for that receiver.
        """
        ...
    
    async def asend_robust(self, sender, **named):
        """
        Send signal from sender to all connected receivers catching errors.

        If any receivers are synchronous, they are grouped and called behind a
        sync_to_async() adaption before executing any asynchronous receivers.

        If any receivers are asynchronous, they are grouped and executed
        concurrently with asyncio.gather.

        Arguments:

            sender
                The sender of the signal. Can be any Python object (normally one
                registered with a connect if you actually want something to
                occur).

            named
                Named arguments which will be passed to receivers.

        Return a list of tuple pairs [(receiver, response), ... ].

        If any receiver raises an error (specifically any subclass of
        Exception), return the error instance as the result for that receiver.
        """
        ...
    


def receiver(signal, **kwargs):
    """
    A decorator for connecting receivers to signals. Used by passing in the
    signal (or list of signals) and keyword arguments to connect::

        @receiver(post_save, sender=MyModel)
        def signal_receiver(sender, **kwargs):
            ...

        @receiver([post_save, post_delete], sender=MyModel)
        def signals_receiver(sender, **kwargs):
            ...
    """
    ...

