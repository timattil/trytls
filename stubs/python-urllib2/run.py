import sys
import ssl
import urllib2


host = sys.argv[1]
port = sys.argv[2]
cafile = sys.argv[3] if len(sys.argv) > 3 else None

try:
    urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
except ssl.CertificateError:
    print("VERIFY FAILURE")
except urllib2.URLError as exc:
    if not isinstance(exc.reason, ssl.SSLError):
        raise
    print("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")
