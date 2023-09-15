Mình nhận được một chương trình Python, trông khá rối mắt vì đám comment, nhưng mà không sao, ta chỉ cần quan tâm những cái chính thôi :v
Chương trình sẽ kiểm tra từng mảnh của flag thông qua các hàm, nên việc bây giờ là dịch ngược lại các hàm đó là xong.
Tại hàm entry:
````
def entry(f): 
    seed(10) 
    f = list(f) 
    f.reverse() 
    f = "".join(i for i in f) 
    print("Entry complete") 
    flag = stage1(f) 
    return flag
````
Hàm entry sẽ đảo input và gọi đến hàm stage1. Mình sẽ dịch ngược lại hàm như sau:
````
def entry(r):
    flag = list(r)
    flag.reverse()
    flag = "".join(x for x in r)
    return flag
````
Tại hàm stage1:
````
def stage1(a): 
    a = list(a) 
    b = list(string.ascii_lowercase) 
    for o in range(len(a)): 
        a[o] = chr(ord(a[o])^o) 
    z = "".join(x for x in a) 
    for y in range(len(z)): 
        b[y%len(b)] = chr((ord(z[y])^ord(a[y]))+len(b)) 
    print("Stage 1 complete") 
    flag = stage2(z) 
    return flag
````
Tại vòng lặp đầu tiên, từng kí tự dưới dạng mã ASCII tại vị trí o trong xâu sẽ XOR với vị trí đó. Tại vòng lặp thứ hai chỉ thay đổi b, nên mình không cần chú ý tới nó. Hàm stage1 sẽ được dịch ngược lại như sau:
````
def stage1(r):
    r = list(r)
    for i in range(len(r)):
        r[i] = chr(ord(r[i]) ^ i)
    r = "".join(x for x in r)
    return r
````
Tại hàm stage2:
````
def stage2(b): 
    t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-') 
    for q in range(len(b)): 
        t += chr(ord(b[q])-randint(0,5)) 
    print("Stage 2 complete") 
    flag = finalstage(t) 
    return flag
````
Trong vòng lặp trên, từng kí tự dưới dạng mã ASCII sẽ trừ đi 1 giá trị ngẫu nhiên trong khoảng 0 đến 5. Nhưng tại hàm entry có xuất hiện hàm seed(10), cho nên output sẽ như nhau, chính vì thế ta chỉ cần seed random cùng một số và thêm hàm randint(0,5) để đảo lại.
````
def stage2(r):
    seed(10)
    inp = ""
    for i in range(len(r)):
        inp += chr(ord(r[i]) + randint(0,5))
    return inp
````
Tại hàm finalstage:
````
def finalstage(w): 
    h=0 
    w = list(w) 
    w.reverse() 
    w = "".join(g for g in w) 
    flag = 'flag'.replace('flag', 'galf').replace('galf', '') 
    while h < len(w): 
        try: 
            flag += w[h+1] + w[h] 
        except: 
            flag += w[h] 
        h+=2 
    print("Final Stage complete") 
    return flag
````
Đầu tiên hàm sẽ đảo ngược input, sau đó sẽ đảo vị trí 2 kí tự cạnh nhau. Mình dịch ngược hàm này như sau:
````
def finalstage(r):
    flag = ""
    i = 0
    while i < len(r):
        try:
            flag += r[i+1] + r[i]
        except:
            flag += r[i]
        i += 2
    flag = list(flag)
    flag.reverse()
    flag = "".join(x for x in flag)
    return flag
````
Mình sẽ để chương trình dịch ngược sau. Và ta sẽ nhận được flag: `PCTF{H0w_D1d_y0U_br34k_my_1337_c0de?}`
