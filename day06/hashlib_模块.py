

import hashlib
hash = hashlib.sha512()
hash.update('admin'.encode())
print(hash.hexdigest())
hash.update("123".encode())
print(hash.hexdigest())
#c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
#7fcf4ba391c48784edde599889d6e3f1e47a27db36ecc050cc92f259bfac38afad2c68a1ae804d77075e8fb722503f3eca2b2c1006ee6f6c7b7628cb45fffd1d


import hmac
h = hmac.new("yangfl".encode())
h.update("hello hello.".encode())
print(h.hexdigest())
#ae3c749e41d45e76c038b0eda861a785