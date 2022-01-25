import Encryption


debug = 0  # show all generated keys if debug set as 1

message = 1337  # message represented as a number


def main():
    encrypt = Encryption.Encryption()
    if debug == 1:
        encrypt.print_keys()
    enc_msg = encrypt.encrypt_starter(message)
    print(enc_msg)
    dec_msg = encrypt.decrypt_starter(enc_msg)
    print(dec_msg)


if __name__ == '__main__':
    main()
