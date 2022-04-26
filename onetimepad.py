# This function performs xor on hex strings
def xor2str(C1, C2):
	C1 = C1.decode('hex')
	C2 = C2.decode('hex')

	result = ""
	for c1, c2 in zip(C1, C2):
		result += chr(ord(c1)^ord(c2))
	return result.encode("hex")

def main():

	# This is the message I created and fed to the application
	MSG = "I love her so much I could die!!".encode("hex")
	# This is the encrypted message given by the application
	C1 = "928f973ee2d5967d928462ed119eb5e15fa49a61e144f4335778c162b998748e"
	# This is my message encrypted by the application
	C2 = "ee9fcc62a4838f2cc5c571ac4e89eead0fff831bf015ad77032ad937e6c8629b"
	#Performing xor on both ciphertexts
	xoredCiphers = xor2str(C1,C2)
	# Performing xor on the resulting hex with the message
	xoredMsg = xor2str(xoredCiphers, MSG)
	# display decrypted message
	print(xoredMsg.decode('hex'))

if __name__ == "__main__":
    main()
