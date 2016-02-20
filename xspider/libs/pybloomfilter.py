#coding=utf-8

import bitarray
import math
import cPickle


"""实现bloomfilter功能
    pip install bitarray    
"""



class Bloomfilter(object):

    def _calc_hash_num(self , capacity , error_rate ):
        """计算bloomfilter 几个重要参数
            params:
                capacity                数据容量
                error_rate              bloomfilter准确率
            return 
                k                       hash函数数目
                m                       需要m位bitmap报错`
            引用：
                http://www.cnblogs.com/haippy/archive/2012/07/13/2590351.html
        """
        #计算需要的hash函数数目
        k = -int( math.ceil(math.log(error_rate , math.e) / math.log(2 , math.e)))
        #在capacity , error_rate固定时，所需要的保存位数
        m = int(math.ceil(-capacity * math.log(error_rate , math.e) / math.log(2 , math.e) ** 2 ))
        return k , m 

    def __init__(self , capacity , error_rate ):
        """初始化bloomfilter 
            params:
                capacity                最大添加到bloomfilter字符串数量
                error_rate              允许出错比率
            return 
                None 
            raise:
                None 
            test:
                >>> b = Bloomfilter(10000000 , 0.001)
                >>> b.add("hello world!")
                >>> b+= "hello world!"
                >>> ("hello world!" in b) == True
                >>> ("a" in b) == False
        """
        k , m = self._calc_hash_num(capacity , error_rate )
        self.bitmap = bitarray.bitarray(m)
        self.k = k 
        self.m = m 
        self.capacity = capacity
        self.error_rate = error_rate
         
    def _hash(self , value , num):
        """
            params:
                value               需要计算hash值的字符串
                num                 数据偏移量，实现多个hash值
            return 
                hash_code           字符串的hash值
            raise:
                None 
            test:
                >>> b = Bloomfilter(1000000 , 0.009) 
                >>> b._hash("hello world" , 3)
                >>> b._hash("hello world" , 4)
        """
        hash_code = ord(value[0]) << num  
        code = self.c_mul(1000003, hash_code) 
        for char in value:
            hash_code = code ^ ord(char)
            hash_code = hash_code ^ len(value)
        if hash_code == -1:
            hash_code = -2
        return hash_code 

    def c_mul(self , a, b):
        return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])
    
    def _hash1(self , value , offset):
        """计算字符串hash值 ， java string hash code implement 
            params:
                    value               需要计算hash值的value 
                    offset              offset实现多个hash方法
            return 
                True
                False 
        """
        result = 0 
        for c in value:
            result = (result * offset + ord(c)) % self.m 
        return result % self.m  

    def __contains__(self , value):
        if value is None:
            raise ValueError 
        for i in range(self.k):
            hash_code = self._hash1(value , 32 + i )
            if self.bitmap[hash_code] is False:
                return False 
        return True  
    
    def add(self , value):
        for i in range(self.k):
            hash_code = self._hash1(value , 32 + i)
            self.bitmap[hash_code] = True 
       
    def __iadd__(self , value):
        self.add(value)
        return self 
        
    def __getitem__(self , value):
        return value in self

    def save(self, path):
        with open(path,"w") as f:
            f.write(cPickle.dump(self , path))
    

    @staticmethod
    def load(path):
        return cPickle.loads(path)
