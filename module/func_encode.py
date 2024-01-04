# coding=utf-8
from random import random
import base64
import html
import urllib.parse


# base
def en_base(base_type, input_str):
  match base_type:
      case 'base16':
          return base64.b16encode(input_str.encode())
      case 'base32':
          return base64.b32encode(input_str.encode())
      case 'base64':
          return base64.b64encode(input_str.encode())
      case 'base85_ASCII85':
          return base64.a64encode(input_str.encode())
      case 'base85_RFC1924':
          return base64.b64encode(input_str.encode())
      case _:
          return 'Unsupported base type'


# 处理字符串转换
def process_string(s, conversion_function):
    return ' '.join([conversion_function(char) for char in s])

def en_ASCII(selected_encoding, user_input):
    if selected_encoding == "二进制":
        return process_string(user_input, ascii_to_binary)
    elif selected_encoding == "八进制":
        return process_string(user_input, ascii_to_octal)
    elif selected_encoding == "十进制":
        return process_string(user_input, ascii_to_decimal)
    elif selected_encoding == "十六进制":
        return process_string(user_input, ascii_to_hex)

# ASCII转换函数
def ascii_to_binary(char):
    return format(ord(char), '08b')

def ascii_to_octal(char):
    return format(ord(char), 'o')

def ascii_to_decimal(char):
    return str(ord(char))

def ascii_to_hex(char):
    return format(ord(char), 'x')

# unicode
def en_unicode(source_text):
    return source_text.encode('unicode_escape')





def func_base36(self, encode_type, source_text):
    result_text = str(base36.loads(source_text))
    return [1, result_text,"Base36"]

def func_base58(self, encode_type, source_text):
    result_text = base58.b58encode(source_text.encode(encode_type)).decode()  # 加密
    return [1, result_text,"Base58"]

def func_base62(self, encode_type, source_text):
    try:
        text = base62.encode(int(source_text))
    except:
        return [0, 'base62只能对数字编码',"Base62"]
    # print(text)
    # result_text = str(text, encoding='utf-8')
    return [1, text,"Base62"]

def func_base64(self, encode_type, source_text):
    text = base64.b64encode(source_text.encode(encode_type))
    result_text = str(text, encoding=encode_type)
    return [1, result_text,"Base64"]

def func_base64_zidingyi(self, encode_type, source_text, n):
    try:
        STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        CUSTOM_ALPHABET = n.encode(encode_type)
        encode_typeTRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
        result_text = base64.b64encode(source_text.encode(encode_type)).translate(encode_typeTRANS).decode()
        return [1, result_text,"Base64(自定义)"]
    except Exception as e:
        return [0, str(e),"Base64(自定义)"]

def func_bae85_ASCII85(self, encode_type, source_text):
    result_text = base64.a85encode(source_text.encode(encode_type)).decode(encode_type)  # 加密
    return [1, result_text,"Base85(ASCII85)"]

def func_bae85_RFC1924(self, encode_type, source_text):
    result_text = base64.b85encode(source_text.encode(encode_type)).decode()  # 加密
    return [1, result_text,"Base85(RFC1924)"]

def func_base91(self, encode_type, source_text):
    result_text = base91.encode(source_text.encode(encode_type))  #
    return [1, result_text,"Base91"]

def func_base92(self, encode_type, source_text):
    result_text = py3base92.encode(source_text)
    return [1, result_text,"Base92"]

def func_Str_Hex(self, encode_type, source_text):
    result = ''
    for i in source_text:
        single = str(hex(ord(str(i))))
        result = result + single
    result_text = (str(result)).replace('0x', '')
    return [1, result_text,"Str->Hex"]

def func_shellcode(self, encode_type, source_text):
    result = ''
    for i in source_text:
        single = str(hex(ord(str(i))))
        result = result + single
    result_text = (str(result)).replace('0x', '\\x')
    return [1, result_text,"Shellcode"]
