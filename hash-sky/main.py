import sys
import hashlib

def hash_md5():
    md5 = hashlib.md5(text_hash.encode())
    print(md5.hexdigest())

def hash_sha1():
    sha1 = hashlib.sha1(text_hash.encode())
    print(sha1.hexdigest())

def hash_sha224():
    sha224 = hashlib.sha224(text_hash.encode())
    print(sha224.hexdigest())

def hash_sha256():
    sha256 = hashlib.sha256(text_hash.encode())
    print(sha256.hexdigest())

def hash_sha384():
    sha384 = hashlib.sha384(text_hash.encode())
    print(sha384.hexdigest())

def hash_sha512():
    sha512 = hashlib.sha512(text_hash.encode())
    print(sha512.hexdigest())


hash_algorithm = str (sys.argv[1])
text_hash = str(sys.argv[2])

if hash_algorithm == "md5" :
    hash_md5()

elif hash_algorithm == "sha1" :
    hash_sha1()

elif hash_algorithm == "sha224" :
    hash_sha224()

elif hash_algorithm == "sha256" :
    hash_sha256()

elif hash_algorithm == "sha384" :
    hash_sha384()

elif hash_algorithm == "sha512" :
    hash_sha512()
