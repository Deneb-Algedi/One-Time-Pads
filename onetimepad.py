import codecs

decode_hex = codecs.getdecoder("hex_codec")

"""This function performs xor on two strings"""
def xor2str(C1, C2):
	C1 = decode_hex(C1)[0]
	C2 = decode_hex(C2)[0]
	
	result = ""
	for c1, c2 in zip(C1, C2):
		result += chr((c1)^(c2))
	
	return(result.encode("utf-8").hex())

def main():
	# This is the message I created and fed to the application
	MSG = "I love her so much I could die!!".encode("utf-8").hex()
	# This is the encrypted message given by the application
	C1 = "928f973ee2d5967d928462ed119eb5e15fa49a61e144f4335778c162b998748e"
	# This is my message encrypted by the application
	C2 = "ee9fcc62a4838f2cc5c571ac4e89eead0fff831bf015ad77032ad937e6c8629b"
	#Performing xor on both ciphertexts
	xoredCiphers = xor2str(C1,C2)
	# Performing xor on the resulting hex with the message
	xoredMsg = xor2str(xoredCiphers, MSG)
	# display decrypted message
	print(str(decode_hex(xoredMsg)[0], 'utf-8')) # different way to perform same operation print(str(codecs.decode(bytes(xoredMsg, encoding='utf-8'), "hex"),'utf-8'))

if __name__ == "__main__":
    main()
