l = len(int(input("Enter a string:")))

#randomised customer reference generator
        letters = string.ascii_uppercase

        v = input("Enter Customer Name:")
        n = len(v)
        u = v.upper()
        a = ''.join(random.choice(u) for j in range(4))
        result_str = a+v.upper()+''.join(random.choice(letters) for i in range(n))



