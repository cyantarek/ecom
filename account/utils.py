import hashlib

def hash_gen(email):
	h = hashlib.sha256(email.encode("utf-8"))
	return h.hexdigest()