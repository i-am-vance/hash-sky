import sys
import hashlib

def hash_sha256():
    sha256 = hashlib.sha256(text_hash.encode())
    print(sha256.hexdigest())
def hash_sha1():
    sha1 = hashlib.sha1(text_hash.encode())
    print(sha1.hexdigest())


hash_algorithm = str (sys.argv[1])
text_hash = str(sys.argv[2])

if hash_algorithm == "sha256" :
    hash_sha256()
elif hash_algorithm == "sha1" :
    hash_sha1()