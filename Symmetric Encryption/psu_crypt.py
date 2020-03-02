import codecs
class Solution(object):
    keyschedule=[]
    # key=0xabcdef0123456789abcd

    def key_schedule(self,x):
        self.key=x
        key=bin(x)
        key=str(key)[2:]
        limitarray={1:[0,8],2:[8,16],3:[16,24],4:[24,32],5:[32,40],6:[40,48],7:[48,56],8:[56,64],9:[64,72],10:[72,80]}
        groupdict={0:[10,9,8,7],1:[6,5,4,3],2:[2,1,10,9],3:[8,7,6,5],4:[4,3,2,1]}
        for x in range(20):
            x%=5
            for j in range(3):
                for k in range(4):
                    key=key[1:]+key[0]
                    keytobereturned=key[limitarray[groupdict[x][k]][0]:limitarray[groupdict[x][k]][1]]
                    self.keyschedule.append(int(keytobereturned,2))

    def nsplit(self,s, n):#Split a list into sublists of size "n"
        return [s[k:k+n] for k in range(0, len(s), n)]

    def f_function(self,hex_value):
        f_table=[
            0xa3,0xd7,0x09,0x83,0xf8,0x48,0xf6,0xf4,0xb3,0x21,0x15,0x78,0x99,0xb1,0xaf,0xf9,
            0xe7,0x2d,0x4d,0x8a,0xce,0x4c,0xca,0x2e,0x52,0x95,0xd9,0x1e,0x4e,0x38,0x44,0x28,
            0x0a,0xdf,0x02,0xa0,0x17,0xf1,0x60,0x68,0x12,0xb7,0x7a,0xc3,0xe9,0xfa,0x3d,0x53,
            0x96,0x84,0x6b,0xba,0xf2,0x63,0x9a,0x19,0x7c,0xae,0xe5,0xf5,0xf7,0x16,0x6a,0xa2,
            0x39,0xb6,0x7b,0x0f,0xc1,0x93,0x81,0x1b,0xee,0xb4,0x1a,0xea,0xd0,0x91,0x2f,0xb8,
            0x55,0xb9,0xda,0x85,0x3f,0x41,0xbf,0xe0,0x5a,0x58,0x80,0x5f,0x66,0x0b,0xd8,0x90,
            0x35,0xd5,0xc0,0xa7,0x33,0x06,0x65,0x69,0x45,0x00,0x94,0x56,0x6d,0x98,0x9b,0x76,
            0x97,0xfc,0xb2,0xc2,0xb0,0xfe,0xdb,0x20,0xe1,0xeb,0xd6,0xe4,0xdd,0x47,0x4a,0x1d,
            0x42,0xed,0x9e,0x6e,0x49,0x3c,0xcd,0x43,0x27,0xd2,0x07,0xd4,0xde,0xc7,0x67,0x18,
            0x89,0xcb,0x30,0x1f,0x8d,0xc6,0x8f,0xaa,0xc8,0x74,0xdc,0xc9,0x5d,0x5c,0x31,0xa4,
            0x70,0x88,0x61,0x2c,0x9f,0x0d,0x2b,0x87,0x50,0x82,0x54,0x64,0x26,0x7d,0x03,0x40,
            0x34,0x4b,0x1c,0x73,0xd1,0xc4,0xfd,0x3b,0xcc,0xfb,0x7f,0xab,0xe6,0x3e,0x5b,0xa5,
            0xad,0x04,0x23,0x9c,0x14,0x51,0x22,0xf0,0x29,0x79,0x71,0x7e,0xff,0x8c,0x0e,0xe2,
            0x0c,0xef,0xbc,0x72,0x75,0x6f,0x37,0xa1,0xec,0xd3,0x8e,0x62,0x8b,0x86,0x10,0xe8,
            0x08,0x77,0x11,0xbe,0x92,0x4f,0x24,0xc5,0x32,0x36,0x9d,0xcf,0xf3,0xa6,0xbb,0xac,
            0x5e,0x6c,0xa9,0x13,0x57,0x25,0xb5,0xe3,0xbd,0xa8,0x3a,0x01,0x05,0x59,0x2a,0x46]
        return f_table[hex_value]

    def g_function(self,word,round,decrypt):
        if decrypt:
            self.gfunctionkeyschedule=self.keyschedule[round*12:round*12+12]
        else:
            self.gfunctionkeyschedule=self.keyschedule[round*12:round*12+12]
        w0=word>>8
        w1=(w0<<8)^word
        g1=w0
        print("the g1 for round" + str(round) + "is"+ hex(g1))
        g2=w1
        print("the g2 for round" + str(round) + "is"+ hex(g2))
        g3=self.f_function(g2^self.gfunctionkeyschedule[0])^g1
        print("the g3 for round" + str(round) + "is"+ hex(g3))
        g4 = self.f_function(g3^ self.gfunctionkeyschedule[1])^ g2
        print("the g4 for round" + str(round) + "is"+ hex(g4))
        g5 = self.f_function(g4 ^ self.gfunctionkeyschedule[2])^ g3
        print("the g5 for round" + str(round) + "is"+ hex(g5))
        g6 = self.f_function(g5 ^ self.gfunctionkeyschedule[3]) ^ g4
        print("the g6 for round" + str(round) + "is"+ hex(g6))
        # return  (g5<<4) | (g6>>4)
        return (g5<<8|g6)

    def g_function_1(self,word,round):
        w0=word>>8
        w1=(w0<<8)^word
        g1=w0
        print("the g1 for round" + str(round) + "is"+ hex(g1))
        g2=w1
        print("the g2 for round" + str(round) + "is"+ hex(g2))
        g3=self.f_function(g2^self.gfunctionkeyschedule[4])^g1
        print("the g3 for round" + str(round) + "is"+ hex(g3))
        g4 = self.f_function(g3^ self.gfunctionkeyschedule[5])^ g2
        print("the g4 for round" + str(round) + "is"+ hex(g4))
        g5 = self.f_function(g4 ^ self.gfunctionkeyschedule[6])^ g3
        print("the g5 for round" + str(round) + "is"+ hex(g5))
        g6 = self.f_function(g5 ^ self.gfunctionkeyschedule[7]) ^ g4
        print("the g6 for round" + str(round) + "is"+ hex(g6))
        # return  (g5<<4) | (g6>>4)
        return (g5<<8|g6)

    def concatenate(self, a, b):
        sizeof_b = 0
        # get size of b in bits
        while((b >> sizeof_b) > 0):
            sizeof_b += 1
        # align answer to nearest 4 bits (hex digit)
        sizeof_b += sizeof_b % 4
        return (a << sizeof_b) | b

    def feistel_function(self,r0,r1,round,decrypt=False):
        t0=self.g_function(r0,round,decrypt)
        print("the t0 for round" + str(round) + "is"+ hex(t0))
        t1=self.g_function_1(r1,round)
        print("the t1 for round" + str(round) + "is"+ hex(t1))
        f0=(t0+2*t1+(self.gfunctionkeyschedule[8]<<8|self.gfunctionkeyschedule[9]))%(2**16)
        print("the f0 for round" + str(round) + "is"+ hex(f0))
        f1=((2*t0)+t1+(self.gfunctionkeyschedule[10]<<8|self.gfunctionkeyschedule[11]))%(2**16)
        print("the f1 for round" + str(round) + "is"+ hex(f1))
        return f0,f1

    def whitening_step(self,w0,w1,w2,w3):
        key=self.key>>16
        k0 =  key >> 48
        k1 = (key >> 32)^(k0<<16)
        k2 = (key >> 16)^((k1<<16))^(k0<<32)
        k3 = key ^(k2<<16)^(k1<<32)^(k0<<48)  
        r0=w0^k0
        r1=w1^k1
        r2=w2^k2
        r3=w3^k3
        return r0,r1,r2,r3,k0,k1,k2,k3

    def encrypt(self,word,key):
        self.key_schedule(key)
        w0 =  word >> 48
        w1 = (word >> 32)^(w0<<16)
        w2 = (word >> 16)^((w1<<16))^(w0<<32)
        w3 = word ^(w2<<16)^(w1<<32)^(w0<<48)
        r0,r1,r2,r3,k0,k1,k2,k3=self.whitening_step(w0,w1,w2,w3)
        for x in range(20):
            f0,f1=self.feistel_function(r0,r1,x)
            r0,r1,r2,r3=r2^f0,r3^f1,r0,r1
        # y0,y1,y2,y3=r2,r3,r0,r1
        c0,c1,c2,c3=r2^k0,r3^k1,r0^k2,r1^k3
        ciphertext=(c0<<48|c1<<32|c2<<16|c3)
        print("The ciphertext is "+ hex(ciphertext))
        return c0,c1,c2,c3,hex(ciphertext)

    def decrypt(self,word,key):
        self.key_schedule(key)
        w0 =  word >> 48
        w1 = (word >> 32)^(w0<<16)
        w2 = (word >> 16)^((w1<<16))^(w0<<32)
        w3 = word ^(w2<<16)^(w1<<32)^(w0<<48)
        r0,r1,r2,r3,k0,k1,k2,k3=self.whitening_step(w0,w1,w2,w3)
        for x in range(19,-1,-1):
            f0,f1=self.feistel_function(r0,r1,x,decrypt=True)
            r0,r1,r2,r3=r2^f0,r3^f1,r0,r1
        x0,x1,x2,x3=r2^k0,r3^k1,r0^k2,r1^k3
        plaintext=(x0<<48|x1<<32|x2<<16|x3)
        print("The plaintext is "+ hex(plaintext))
        return hex(plaintext)
        
    def encrypt_method(self):
        k=open("key.txt","r")
        key=k.read()
        with open("plaintext.txt", "r") as f:
            mytext=f.read(8)
            while mytext:
                mytext=int(mytext.encode('utf-8').hex(),16)
                c0,c1,c2,c3,ciphertext = self.encrypt(mytext,int(key,16))
                ciphertext=ciphertext[2:]
                while(len(ciphertext)<16):
                    ciphertext="0"+ciphertext
                print(ciphertext)
                c=open("ciphertext.txt","a")
                c.write(ciphertext)
                c.close()
                mytext = f.read(8)

    def decrypt_method(self):
        f = open("ciphertext.txt", "r")
        ciphertext=f.read()
        f=open("key.txt","r")
        key=f.read()
        for i in range(0,len(ciphertext),16):
            mytext=ciphertext[i:i+16]
            mytext=int(mytext,16)
            plaintext = self.decrypt(mytext,int(key,16))
            print(plaintext)
            finalplaintext=''
            for i in range(2,len(plaintext),2):
                char=plaintext[i:i+2]
                finalplaintext+=chr(int(char,16))
            f=open("plaintext.txt","a")
            f.write(finalplaintext)
            f.close()

sol=Solution()
#Use the below methods interchangeably. For encryption use encrypt_method
# For decryption use decrypt_method.
# sol.encrypt_method()
sol.decrypt_method()


