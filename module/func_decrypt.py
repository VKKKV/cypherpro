# coding=utf-8
import collections
import re
import string

from Crypto.Cipher import AES
from re import split
from py7zr import SevenZipFile
from io import BytesIO

class Class_Decrypt:

    def func_rot5(self, encode_type, source_text):
        if not bool(re.match('^[A-Za-z0-9]+$',source_text)):
            return [0, 'ROT5只能对数字解密',"ROT5"]
        result = ''
        ascii_num = string.digits
        lookup_tuple = {}

        for i in range(len(ascii_num)):
            lookup_tuple[ascii_num[i]] = ascii_num[i - 5]

        for i in source_text:
            if i not in lookup_tuple:
                b = i
            else:
                b = lookup_tuple[i]
            result += b
        return [1, result.strip(),"Rot5"]

    def func_rot13(self, encode_type, source_text):
        if not bool(re.match('^[A-Za-z0-9]+$',source_text)):
            return [0, 'Rot13只能对字母解密',"Rot13"]
        try:
            PAIRS = {
                "a": "n", "b": "o", "c": "p", "d": "q", "e": "r",
                "f": "s", "g": "t", "h": "u", "i": "v", "j": "w",
                "k": "x", "l": "y", "m": "z", "n": "a", "o": "b",
                "p": "c", "q": "d", "r": "e", "s": "f", "t": "g",
                "u": "h", "v": "i", "w": "j", "x": "k", "y": "l",
                "z": "m", "A": "N", "B": "O", "C": "P", "D": "Q",
                "E": "R", "F": "S", "G": "T", "H": "U", "I": "V",
                "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A",
                "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F",
                "T": "G", "U": "H", "V": "I", "W": "J", "X": "K",
                "Y": "L", "Z": "M"
            }
            result_text = "".join(PAIRS.get(c, c) for c in source_text)
        except Exception as  e:
            return [0, '解密失败',"Rot13"]
        return [1, result_text.strip(),"Rot13"]

    def func_rot18(self, encode_type, source_text):
        rot5_ = self.func_rot5('', source_text)[1]
        # print(rot5_)
        result = self.func_rot13('',rot5_)
        return [1, str(result[1]).strip(),"Rot18"]

    def func_rot47(self, encode_type, source_text):
        result = ''
        for i in source_text:
            if ord(i) > 126 or ord(i) < 33:
                b = i
            elif ord(i) >= 80:
                b = chr(ord(i) - 47)
            else:
                b = chr(ord(i) + 47)
            result += b
        return [1, result.strip(),"Rot47"]

    def func_kaisa(self, encode_type, source_text):
        if not bool(re.match('^[A-Za-z0-9]+$',source_text)):
            return [0, '凯撒密码只能对字母解密',"凯撒密码"]
        try:
            t = ""
            for c in source_text:
                if 'a' <= c <= 'z':  # str是可以直接比较的
                    t += chr(ord('a') + ((ord(c) - ord('a')) - 3) % 26)
                elif 'A' <= c <= 'Z':
                    t += chr(ord('A') + ((ord(c) - ord('A')) - 3) % 26)
                else:
                    t += c
            result_text = t
        except Exception as  e:
            return [0, '解密失败',"凯撒密码"]
        return [1, result_text.strip(),"凯撒密码"]

    def func_zhalan(self, encode_type, source_text):
        try:
            result_text = ''
            factors = [fac for fac in range(2, len(source_text)) if len(source_text) % fac == 0]  # 取得密文长度的所有因数
            for fac in factors:
                flag = ''
                for i in range(fac):  # 按一定的步长取几组字符，并连接起来，这里组数就等于步长数
                    flag += source_text[i::fac]
                result_text += "分为%s栏，解密结果为:%s\n" % (fac, flag)
        except Exception as  e:
            return [0, '解密失败',"栅栏密码"]
        return [1, result_text.strip(),"栅栏密码"]

    def func_zhalan_w(self, encode_type, source_text):
        try:
            result_text = ''
            for n in range(2, len(source_text)):  # 遍历所有可能的栏数
                # print(str(n) + '栏：' + ''.join(self.zhanlan_w_decode(text, n)[1]))
                result_text += "分为%s栏，解密结果为:%s\n" % (str(n), ''.join(self.zhanlan_w_decode(source_text, n)[1]))
        except Exception as  e:
            return [0, '解密失败',"栅栏密码(W型)"]
        return [1, result_text.strip(),"栅栏密码(W型)"]

    def func_peigen(self, encode_type, source_text):
        try:
            return_str = ''
            dicts = {'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y',
                     'abbab': 'N',
                     'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F',
                     'aabaa': 'E',
                     'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D',
                     'abbbb': 'P',
                     'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
            sums = len(source_text)
            j = 5  ##每5个为一组
            for i in range(int(sums / j)):
                result = source_text[j * i:j * (i + 1)].lower()
                return_str += str(dicts[result], )
            result_text = return_str
        except Exception as  e:
            return [0, '解密失败',"培根密码"]
        return [1, result_text.strip(),"培根密码"]

    def func_mosi(self, encode_type, source_text):
        try:
            dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                    '..--..': '?', '-..-.': '/', '-.--.-': '()', '-....-': '-',
                    '.-.-.-': '.', '..--.-': '_'
                    }
            msg = ''
            if ' ' in source_text:
                split_str = ' '
            elif '/' in source_text:
                split_str = '/'
            else:
                split_str = source_text.replace('.', '').replace('-', '')[0:1]
            s = source_text.split(split_str)
            for item in s:
                if item != '' and item != ' ':
                    if item in dict.keys():
                        msg += (dict[item])
                    else:
                        msg += ("(部分解密失败:" + item + ")")
            result_text = msg
        except Exception as  e:
            return [0, '解密失败',"摩斯密码"]
        return [1, result_text.strip(),"摩斯密码"]

    def func_yiwei(self, encode_type, source_text):
        try:
            inputStr = source_text
            #
            result = ''
            for j in range(26):
                result_list = []
                for i, num in zip(inputStr, range(len(inputStr))):
                    # print(i)
                    caseS1 = string.ascii_lowercase * 2
                    if i.islower:
                        caseS1 = string.ascii_lowercase * 2
                    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        caseS1 = string.ascii_uppercase * 2
                    status = caseS1.find(i)
                    if status != -1:
                        result_list.append(caseS1[status + j])
                    else:
                        result_list.append(inputStr[num])
                text2 = ("".join(result_list), "向右偏移了{}位".format(j))
                result += text2[0] + ' ' + text2[1] + '\n'
            result_text = result
        except Exception as  e:
            return [0, '解密失败',"移位密码"]
        return [1, result_text.strip(),"移位密码"]

    def func_yunying(self, encode_type, source_text):
        try:
            other_letters = []
            for s in source_text:
                if not ['0', '1', '2', '4', '8'].count(s):
                    other_letters.append(s)
            if other_letters:
                return [0, '加密字符串内只能包含0、1、2、4、8',"云影密码"]
            else:
                result_text = ''
                charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                ret = []
                plaintext = [i for i in source_text.split('0')]
                for i in plaintext:
                    tmp = 0
                    for j in range(len(i)):
                        tmp += int(i[j])
                    ret.append(charList[tmp - 1])
                result_text = ''.join(ret)
        except Exception as  e:
            return [0, '解密失败',"云影密码"]
        return [1, result_text.strip(),"云影密码"]



    def func_Polybius(self, encode_type, source_text):
        Polybius_dic = {
            '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '21': 'F', '22': 'G',
            '23': 'H', '24': 'I', '25': 'K', '31': 'L', '32': 'M', '33': 'N', '34': 'O',
            '35': 'P', '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', '51': 'V',
            '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'
        }
        list = re.findall(r'.{2}', source_text)
        cc = [Polybius_dic[i] for i in list]
        dd = ''.join(cc)
        ee=''
        if 'I' in dd:
            ee = dd.replace('I', 'J')
        result = ("{}\n{}".format(dd, ee))
        return [1, result.strip(),"棋盘密码"]

    def func_atbash(self, encode_type, source_text):
        if not bool(re.match('^[A-Za-z]+$',source_text)):
            return [0, '埃特巴什码只能对字母解密',"埃特巴什码"]
        try:
            str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
            result_text = ""
            for s in source_text:
                if s in str1:
                    if s != ' ':
                        result_text = result_text + str1[str2.index(s)]
                    else:
                        result_text = result_text + ' '
                else:
                    result_text = result_text + s
        except Exception as  e:
            return [0, '解密失败',"Atbash"]
        return [1, result_text.strip(),"Atbash"]

    def func_vigenere(self,encode_type, source_text,key):
        try:
            letter_list = string.ascii_uppercase
            letter_list2 = string.ascii_lowercase
            message =source_text.strip()
            if len(key) == 0:
                return [0, '请输入一个合法的key!',"维吉尼亚密码"]
            
            key_list = []
            for i in key:
                key_list.append(ord(i.upper()) - 65)
            plaintext = ""
            flag = 0
            for cipher in message:
                if flag % len(key_list) == 0:
                    flag = 0
                if cipher.isalpha():
                    if cipher.isupper():
                        plaintext += letter_list[(ord(cipher) - 65 - key_list[flag]) % 26]
                        flag += 1
                    if cipher.islower():
                        plaintext += letter_list2[(ord(cipher) - 97 - key_list[flag]) % 26]
                        flag += 1
                else:
                    plaintext += cipher
            if plaintext != '':
                return [1, plaintext,"维吉尼亚密码"]
            else:
                return [0, '解密失败',"维吉尼亚密码"]
        except Exception as e:
            return [0, str(e),"维吉尼亚密码"]

    def zhanlan_w_decode(self, string, n):
        '''解密'''
        array = self.generate_w(string, n)
        sub = 0
        for row in range(n):  # 将w型字符按行的顺序依次替换为string
            for col in range(len(string)):
                if array[row][col] != '.':
                    array[row][col] = string[sub]
                    sub += 1
        msg = []
        for col in range(len(string)):  # 以列的顺序依次连接各字符
            for row in range(n):
                if array[row][col] != '.':
                    msg.append(array[row][col])
        return array, msg
    def generate_w(self, string, n):
        '''将字符排列成w型'''
        array = [['.'] * len(string) for i in range(n)]  # 生成初始矩阵
        row = 0
        upflag = False
        for col in range(len(string)):  # 在矩阵上按w型画出string
            array[row][col] = string[col]
            if row == n - 1:
                upflag = True
            if row == 0:
                upflag = False
            if upflag:
                row -= 1
            else:
                row += 1
        return array
    
    def func_sifang(self,encode_type, source_text,key1,key2):
        try:
            text = source_text.upper()
            key1 = key1.upper()
            key2 = key2.upper()
            matrix = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
            pla = "abcdefghijklmnoprstuvwxyz"
            key1 = '[' + key1 + "]"
            key2 = '[' + key2 + "]"
            key1 = ''.join(collections.OrderedDict.fromkeys(key1))
            key2 = ''.join(collections.OrderedDict.fromkeys(key2))
            matrix1 = re.sub('[\[\]]', '', key1) + re.sub(key1, '', matrix)
            matrix2 = re.sub('[\[\]]', '', key2) + re.sub(key2, '', matrix)
            matrix_list1 = []
            matrix_list2 = []
            pla_list = []
            # print(matrix1)
            for i in range(0, len(matrix1), 5):
                matrix_list1.append(list(matrix1[i:i + 5]))
            for i in range(0, len(matrix2), 5):
                matrix_list2.append(list(matrix2[i:i + 5]))
            for i in range(0, len(pla), 5):
                pla_list.append(list(pla[i:i + 5]))
            cip = text.replace(' ', '')
            result = ''
            for i in range(0, len(cip), 2):
                letter = cip[i:i + 2]
                # 两个子母中第一个字母位置
                first = self.find_index1(letter[0], matrix_list1)

                # 两个子母中第二个字母位置
                second = self.find_index2(letter[1], matrix_list2)

                return_pla = ""
                return_pla += pla_list[first[0]][second[1]]
                return_pla += pla_list[second[0]][first[1]]
                result += return_pla
            if result != '':
                return [1, result.strip(),"四方密码"]
            else:
                return [0, '解密失败',"四方密码"]

        except Exception as e:
            return [0, str(e),"四方密码"]

    # 求逆元函数
    def GetInverse(self, a, m):
        for i in range(m):
            if (1 == (a * i) % m):
                return i
        return a
    def gcd(self, a, b):
        if (a < b):
            t = a
            a = b
            b = t

        while (0 != b):
            t = a
            a = b
            b = t % b
        return a

    def func_fangshe(self, encode_type, source_text,key1,key2):
        try:
            try:
                if (0 == int(key1.isdigit()) or 0 == int(key2.isdigit())):
                    return [0, '输入有误! 密钥为数字。',"仿射密码"]
                if (self.gcd(int(key1), 26) != 1):
                    key1_list = []
                    result = ''
                    for i in range(0, int(key1)):
                        if self.gcd(i, 26) == 1:
                            key1_list.append(i)
                    for z in key1_list:
                        result += 'key1:%s' % z + '   明文:' + self.fangshe_getdecrypt(int(z), int(key2)) + '\n'
                    return [0, '输入有误! key1和26必须互素。以下为爆破key1的结果\n' + result,"仿射密码"]
                else:
                    result = self.fangshe_getdecrypt(source_text,int(key1), int(key2))
                    return [1, result.strip(),"仿射密码"]

            except:
                return [0, '输入有误!',"仿射密码"]

        except Exception as e:
            return [0, str(e),"仿射密码"]

    def fangshe_getdecrypt(self, source_text,key1, key2):
        try:
            text = source_text.strip()
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 字母表
            plaintext = ""
            for ch in text:  # 遍历密文
                if ch.isalpha():  # 密文为否为字母,如果是,则判断大小写,分别进行解密
                    if ch.isupper():
                        plaintext += letter_list[self.GetInverse(key1, 26) * (ord(ch) - 65 - key2) % 26]
                    else:
                        plaintext += letter_list[self.GetInverse(key1, 26) * (ord(ch) - 97 - key2) % 26].lower()
                else:  # 如果密文不为字母,直接添加到明文字符串里
                    plaintext += ch
            return plaintext
        except:
            return

    # 查询两个密文字母位置
    def find_index1(self, x, matrix_list1):
        for i in range(len(matrix_list1)):
            for j in range(len(matrix_list1[i])):
                if matrix_list1[i][j] == x:
                    return i, j

    def find_index2(self, y, matrix_list2):
        for k in range(len(matrix_list2)):
            for l in range(len(matrix_list2[k])):
                if matrix_list2[k][l] == y:
                    return k, l
                
    def func_a1z26(self, encode_type, source_text):
        str1 = string.ascii_lowercase
        res = source_text.split("-")
        result = ""
        for i in res:
            result += str1[int(i) - 1]
        return [1, result.strip(),"A1z26密码"]