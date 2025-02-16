# Startup 

Remember to start Pycharm run config, because it is a customized wwwpy config (to include pudb, urwid, urwid_readline and wcwidth)
see wwwpy_dev.py in this repo.

## PuDB remote debugging

The following command is to open a local port for pudb remote debugging to show up
`stty -echo -icanon && nc -l -p 6899`

See more here:
https://documen.tician.de/pudb/starting.html#reverse-remote-debugging

# Next Steps

When component1 is loaded, click button1, it will try to start pudb remote debugging, but it will fail because sockets are not supported.

Go in remote.py lines 157-171, we should change the socket handling with some forwarding from the browser

```
PythonError: Traceback (most recent call last):
  File "remote/component1.py", line 27, in button1__click
    set_trace(reverse=True,port=12345)
  File "pudb/remote.py", line 279, in set_trace
    return debugger(
           ^^^^^^^^^
  File "pudb/remote.py", line 261, in debugger
    rdb = _current[0] = RemoteDebugger(
                        ^^^^^^^^^^^^^^^
  File "pudb/remote.py", line 157, in __init__
    self._client, (address, port) = self.get_client(
                                    ^^^^^^^^^^^^^^^^
  File "pudb/remote.py", line 192, in get_client
    client, address = self.get_reverse_socket_client(host, port)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pudb/remote.py", line 213, in get_reverse_socket_client
    raise exc
  File "pudb/remote.py", line 208, in get_reverse_socket_client
    _sock.connect((host, port))
BlockingIOError: [Errno 26] Operation in progress


```