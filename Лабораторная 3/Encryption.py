import random
import math


class Encryption:
    def __init__(self):
        self.p = self._genprimekey()
        self.q = self._genprimekey()

        self.pqs = (self.p - 1) * (self.q - 1)
        self.n = self.p * self.q

        self.d = self._genrelprimekey()
        self.e = self._genrelbackdmod()

    def encrypt_starter(self, message):
        encrypted_message = (message ** self.d) % self.n
        return encrypted_message

    def decrypt_starter(self, message):
        decrypted_message = (message ** self.e) % self.n
        return decrypted_message

    def print_keys(self):
        print("""
        Ключ p: {}
        Ключ q: {}
        Ключ d: {}
        Ключ e: {}
        """.format(self.p, self.q, self.d, self.e))

    def _RabinMiller(self, n):
        n_1 = n - 1
        s = 0
        temp = n_1
        while (temp % 2) == 0:
            temp = temp // 2
            s = s + 1
        d = temp
        a_set = []
        for i in range(int(math.log(n))):
            a_set.append(random.randint(2, n - 1))
        for a in a_set:
            x = (a ** d) % n
            if x != 1:
                flag = 1
                for k in range(s):
                    x2 = (a ** ((2 ** k) * d)) % n
                    if x2 == n - 1:
                        flag = 0
                        break
                if flag == 1:
                    return False
        return True

    def _genprimekey(self):
        while True:
            key = random.randint(100, 1000)
            if key % 2 == 1:
                if self._RabinMiller(key):
                    break
        return key

    def _genrelprimekey(self):
        while True:
            key = random.randint(100, 1000)
            if self._Euclid(key, self.pqs):
                    break
        return key

    def _Euclid(self, key, sec_number):
        sub = max(key, sec_number)
        res = min(key, sec_number)

        while sub != 0:
            tmp = sub
            sub = res % sub
            res = tmp

        if res == 1:
            return True
        else:
            return False

    def _genrelbackdmod(self):
        e = random.randint(100, 1000)
        while (e * self.d) % self.pqs != 1:
            e = e + 1
        return e