import string

# from pika.compat import xrange

# def encrypt(message, key):
#     encrypted_message = []
#     for i in range(len(message)):
#         encrypted_message.append(key[i])
#     "".join(str(ch) for ch in encrypted_message)
#     return "".join(str(ch) for ch in encrypted_message)
#
# def decrypt(message, key):
#     decrypted_message = []
#     for i in range(len(message)):
#         index = key.indx(message[i])
#         decrypted_message.append(string.ascii_uppercase[index])
#     return"".join(str(ch) for ch in decrypted_message)


# str = "abcdefghijklmnopqrstuv"
# for i in xrange(0, len(str)):
#     print(str[i])

def log_execution(func):
    def wrapper():
        print("Starting function")
        result = func()
        print("Finished function")
        return result

    return wrapper


@log_execution
def run_test():
    print("Running test")

run_test()



