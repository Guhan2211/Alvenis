python3.6 -i /var/www/guhan_pythonanywhere_com_wsgi.py




Traceback (most recent call last):
  File "/var/www/guhan_pythonanywhere_com_wsgi.py", line 16, in <module>
    from run import app as application  # noqa
  File "/home/Guhan/mysite/run.py", line 1, in <module>
    from library.startup import app
  File "/home/Guhan/mysite/library/startup.py", line 4, in <module>
    from library.getchannel import fradd,stri,las,tym
  File "/home/Guhan/mysite/library/getchannel.py", line 9, in <module>
    r = http.request('GET', 'https://api.thingspeak.com/channels/591147/feeds.json?results=100')
  File "/usr/lib/python3.6/site-packages/urllib3/request.py", line 68, in request
    **urlopen_kw)
  File "/usr/lib/python3.6/site-packages/urllib3/request.py", line 89, in request_encode_url
    return self.urlopen(method, url, **extra_kw)
  File "/usr/lib/python3.6/site-packages/urllib3/poolmanager.py", line 322, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/usr/lib/python3.6/site-packages/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  File "/usr/lib/python3.6/site-packages/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  File "/usr/lib/python3.6/site-packages/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  File "/usr/lib/python3.6/site-packages/urllib3/connectionpool.py", line 638, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/usr/lib/python3.6/site-packages/urllib3/util/retry.py", line 398, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.thingspeak.com', port=443): Max retries exceeded with url: /channels/591147/feeds.json?results=100 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f91380b54a8>: Failed to establish a new connection: [Errno 111] Connection refused',))
>>> 