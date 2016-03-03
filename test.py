#-*- coding: utf-8 -*-
import LEA

def main():

	#키(key) 키 길이는 16바이트, 24바이트 또는 32바이트
	key = bytearray(b"blacksnakeblacksnake1234")
	print(key)

	#평문
	input_str = "abc123가나다"
	print("입력값 : " + input_str)

	##### 암호화
	print("Encrypt Start")

	pt = bytearray(input_str, "utf8")
	print("bytes : " + str(pt))

	'''
		LEA.ECB(do_enc, key, PKCS5Padding)
		do_enc(bool) : 암호화(True) 복호화(False) 여부 
		key(bytearray) : 마스터 키. 키 길이는 16바이트, 24바이트 또는 32바이트
		PKCS5Padding : PKCS5 패딩을 사용하여 암.복호화를 할 것인지 설정
	'''
	leaECB = LEA.ECB(True, key, True)

	ct = leaECB.update(pt)
	ct += leaECB.final()

	print(ct)

	print("Encrypt End")

	
	##### 복호화
	print("Decrypt Start")

	leaECB = LEA.ECB(False, key, True)
	pt = leaECB.update(ct)
	pt += leaECB.final()

	print(pt)
	decrypt_output = pt.decode('utf8')
	print("결과는 : " + decrypt_output)

	print("Decrypt End")


if __name__ == "__main__":
    main()
   