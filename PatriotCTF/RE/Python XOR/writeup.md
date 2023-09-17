Ta nhận được 1 chương trình Python mã hóa một xâu:
````
from string import punctuation

alphabet = list(punctuation)
data = "bHEC_T]PLKJ{MW{AdW]Y"
def main():
#   For loop goes here
    key = ('')
    decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
    print(decrypted)
main()
````
Mình nhận thấy rằng từng kí tự dưới dạng mã ASCII sẽ XOR với kí tự dưới dạng mã ASCII của key. Cho nên mình sẽ bruteforce để tìm flag.
````
data = "bHEC_T]PLKJ{MW{AdW]Y"
flag = ''
def main():
    for i in range(128):
        key = chr(i)
        decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
        if 'Flag{' in decrypted:
            print(decrypted)
            break
main()
````
Flag: `Flag{python_is_e@sy}`
