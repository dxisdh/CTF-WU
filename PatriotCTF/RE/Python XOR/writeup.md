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
Mình nhận thấy rằng từng vị trí trong xâu data trên sẽ được chuyển sang mã Unicode bằng hàm ord, sau đó sẽ được chuyển sang kí tự bằng hàm chr, tiếp đó sẽ XOR với mã Unicode của key. Cho nên chúng ta chỉ cần viết chương trình đơn giản để dịch ngược lại là xong.
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
