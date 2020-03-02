# // It returns false if n is composite and returns true if n
# // is probably prime.  k is an input parameter that determines
# // accuracy level. Higher value of k indicates more accuracy.
# bool isPrime(int n, int k)
# 1) Handle base cases for n < 3
# 2) If n is even, return false.
# 3) Find an odd number d such that n-1 can be written as d*2r. 
#    Note that since n is odd, (n-1) must be even and r must be 
#    greater than 0.
# 4) Do following k times
#      if (millerTest(n, d) == false)
#           return false
# 5) Return true.

# // This function is called for all k trials. It returns 
# // false if n is composite and returns false if n is probably
# // prime.  
# // d is an odd number such that  d*2r = n-1 for some r >= 1
# bool millerTest(int n, int d)
# 1) Pick a random number 'a' in range [2, n-2]
# 2) Compute: x = pow(a, d) % n
# 3) If x == 1 or x == n-1, return true.

# // Below loop mainly runs 'r-1' times.
# 4) Do following while d doesn't become n-1.
#      a) x = (x*x) % n.
#      b) If (x == 1) return false.
#      c) If (x == n-1) return true. 

import math
import random
class Solution(object):
    '''This function checks if a number given to it is a prime or not
    args: number- the number that is to be checked
    args:- k- k is an input parameter that determines
    accuracy level. Higher value of k indicates more accuracy.
    '''
    def Miller_Rabin(self,number,k):
        if number%2==0:
            return False
        else:
            d=0
            product=1
            div=1
            while(True):
                product*=2
                d+=1
                if math.ceil((number-1)/product)!=math.floor((number-1)/product):
                    break
                div=(number-1)/product
            m=int(div)
            for i in range(k):
                if not (self.millerTest(number,m)):
                    return False
            return True
    
    '''This function is called for all k trials. It returns 
    false if n is composite and returns false if n is probably
    prime.  
    d is an odd number such that  d*2r = n-1 for some r >= 1
    '''
    def millerTest(self,n,d):
        a=random.randrange(1,n-2)
        x=pow(a,d,n)
        if x==1 or x==n-1:
            return True
        while(d!=n-1):
            x=pow(x,2,n)
            d*=2
            if x==1:
                return False
            if x==n-1:
                return True
    
    '''This function is for generating a k-bit safe prime
    '''
    def safe_prime(self):
        p,q=0,0
        while True:
            q=random.randint(2**30,2**31-1)
            if q%12==5 and self.Miller_Rabin(q,4) and self.Miller_Rabin(2*q+1,4):
                p=2*q+1
                break
        return p,q
    
    '''This function is used for key generation
    '''
    def key_generation(self):
        p,q=self.safe_prime()
        d= random.randrange(1,p-2)
        e1=2
        e2=pow(e1,d,p)
        return e1,e2,p,d
    
    '''
    This function calls key_generation
    '''
    def generate_key(self):
        e1,e2,p,d = self.key_generation()
        f = open("pubkey.txt", "a")
        f.write(str(p)+ " "+ str(e1)+" "+ str(e2))
        f.close()
        f=open("privkey.txt","a")
        f.write(str(p)+ " "+ str(e1)+" "+ str(d))
        f.close()

    '''
    This function is used for encrypting a message
    '''
    def encrypt(self):
        with open("message.txt", "rb") as f:
            mytext=f.read(4)
            while mytext:
                m=int.from_bytes(mytext,"big")
                pubkey=open("pubkey.txt", "r")
                pubkey_text=pubkey.read()
                my_array=pubkey_text.split()
                pubkey.close()
                p=int(my_array[0])
                g=int(my_array[1])
                e=int(my_array[2])
                k=random.randrange(0,p-1)
                c1=pow(g,k,p)
                c2=(pow(e,k,p)*(m%p))%p
                cipher=open("ciphertext.txt","a")
                cipher.write(str(c1)+" "+str(c2) + " ")
                cipher.close()
                mytext=f.read(4)
    '''
    This function is used for decrypting a ciphertext
    '''
    def decrypt(self):
        privkey=open("privkey.txt","r")
        privkeytext=privkey.read().split()
        privkey.close()
        p,g,d=int(privkeytext[0]),int(privkeytext[1]),int(privkeytext[2])
        with open("ciphertext.txt","r") as ciphertext:
            cipher= ciphertext.read().split()
            for c1 in range(0,len(cipher),2):
                m=pow(int(cipher[c1]),p-1-d,p)*((int(cipher[c1+1]))%p)%p
                m=(bin(m))[2:]
                while(len(m)!=32):
                    m='0'+m
                plaintext=""
                for i in range(0,len(m),8):
                    if int(m[i:i+8],2)==0:
                        continue
                    plaintext+=chr(int(m[i:i+8],2))
                plain=open("plaintext.txt",'a')
                plain.write(plaintext)
                plain.close()




sol=Solution()
sol.generate_key()
sol.encrypt()
sol.decrypt()



