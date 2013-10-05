# A collection of text encoding and obfuscation functions

from django.conf import settings
import hashlib
from Crypto.Cipher import AES
from base64 import urlsafe_b64encode, urlsafe_b64decode

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
	"""Converts an integer to a base36 string."""
	if not isinstance(number, (int, long)):
		raise TypeError('number must be an integer')

	base36 = ''
	sign = ''

	if number < 0:
		sign = '-'
		number = -number

	if 0 <= number < len(alphabet):
		return sign + alphabet[number]

	while number != 0:
		number, i = divmod(number, len(alphabet))
		base36 = alphabet[i] + base36

	return sign + base36

def base36decode(number):
	return int(number, 36)

def GenRandomStr(length):
    alphabet = string.letters[0:52] + string.digits
    return "".join([random.choice(alphabet) for i in range(length)])

def GenRandomHash():
	return hashlib.sha256(GenRandomStr(64)).hexdigest()

def GenSaltedHash(s):
	return hashlib.sha256(s + settings.SECRET_KEY).hexdigest()

class AESCipher(object):
	def __init__(self, bits, key=None):
		assert bits in (128, 192, 256)
		self.bits = bits
		self.BS = bits / 8
		if key:
			self.key = key
		else:
			self.key = hashlib.sha256(settings.SECRET_KEY).hexdigest()[:self.BS]
		self._cipher = AES.new(self.key, AES.MODE_ECB)
		self._pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS) 
		self._unpad = lambda s : s[0:-ord(s[-1])]
		self._b64pad = lambda s: s + (4 - len(s) % 4) * "="
		self._b64unpad = lambda s: s.replace("=", "")

	def encrypt(self, pt):
		return self._b64unpad(urlsafe_b64encode(self._cipher.encrypt(self._pad(str(pt)))))

	def decrypt(self, ct):
		return self._unpad(self._cipher.decrypt(urlsafe_b64decode(self._b64pad(ct))))

AESCipher = AESCipher(128)