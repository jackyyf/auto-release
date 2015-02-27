from hashlib import sha1

class Conf:
	shared_secret = sha1('__SOME_RANDOM_CHARACTER_HERE!__').hexdigest()