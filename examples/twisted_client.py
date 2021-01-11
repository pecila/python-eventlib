"""Example for GreenTransport and GreenClientCreator.

In this example reactor is started implicitly upon the first
use of a blocking function.
"""
from twisted.internet import ssl
from twisted.internet.error import ConnectionClosed
from eventlib.twistedutil.protocol import GreenClientCreator
from eventlib.twistedutil.protocols.basic import LineOnlyReceiverTransport
from twisted.internet import reactor

print("\n\nRead from TCP connection\n\n")

# read from TCP connection
conn = GreenClientCreator(reactor).connectTCP('www.google.com', 80)
conn.write('GET /not_found  HTTP/1.0\r\n\r\n')
conn.loseWriteConnection()
print(conn.read().decode('utf-8'))

print("\n\nRead from SSL connection line by line\n\n")

# read from SSL connection line by line
conn = GreenClientCreator(reactor, LineOnlyReceiverTransport).connectSSL('ssltest.com', 443, ssl.ClientContextFactory())
conn.write('GET /not_found HTTP/1.0\r\n\r\n')
try:
    for num, line in enumerate(conn):
        print('%3s %r' % (num, line))
except ConnectionClosed as ex:
    print(ex)

