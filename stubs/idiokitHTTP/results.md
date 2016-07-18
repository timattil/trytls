```
platform: OS X 10.11.5
runner: trytls 0.0.7 (CPython 2.7.10, OpenSSL 0.9.8zh)
stub: python 'idiokitHTTPtest.py'
  PASS badssl(False, 'expired')
  PASS badssl(False, 'wrong.host')
  PASS badssl(False, 'self-signed')
x FAIL badssl(True, 'sha256')
x FAIL badssl(True, '1000-sans')
x FAIL badssl(True, '10000-sans')
  PASS badssl(False, 'incomplete-chain')
  PASS badssl(False, 'superfish')
  PASS badssl(False, 'edellroot')
  PASS badssl(False, 'dsdtestprovider')
  PASS badssl_onlymyca(False, 'sha256')
  PASS ssllabs(False, port=10443)
  PASS ssllabs(False, port=10444)
x FAIL ssllabs(False, port=10445)
x FAIL local(True, 'localhost')
  PASS local(False, 'nothing')
```
