import hashlib


class Md5Cracker:

    def __init__(self, hashed, salt):
        self.hash = hashed
        self.salt = salt

    def start(self, filename='md5_cracker/wordlist.txt'):

        with open(filename, 'r') as fp:

            for plaintext_password in fp:
                plaintext_password = plaintext_password.strip()
                print(plaintext_password, end=': ')
                attempt = hashlib.md5(str.encode('{}{}'.format(plaintext_password, self.salt))).digest()
                print(attempt.hex())
                if attempt.hex() == self.hash:
                    print('SUCCESS!!!!')
                    print('password is {}'.format(plaintext_password))
                    exit()


