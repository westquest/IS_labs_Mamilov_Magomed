# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Protocol import Protocol




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bob = Protocol()
    alice = Protocol()

    bob.connection(alice)
    bob.gen_full_key()
    alice.gen_full_key()

    message = alice.encrypt_msg("Hello")
    print(message)
    print(bob.decrypt_msg(message))

