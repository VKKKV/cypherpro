# coding=utf-8
import re
import base64
import html
import urllib.parse


def de_base(base_type, input_str):
  match base_type:
      case 'base16':
          return base64.b16decode(input_str.encode())
      case 'base32':
          return base64.b32decode(input_str.encode())
      case 'base64':
          return base64.b64decode(input_str.encode())
      case 'base85_ASCII85':
          return base64.a85decode(input_str.encode())
      case 'base85_RFC1924':
          return base64.b85decode(input_str.encode())
      case _:
          return 'Unsupported base type'



def de_ASCII(selected_encoding, input_str):
    spaced = lambda input_str : ' ' in input_str
    if selected_encoding == "二进制":
        return binary_to_ascii(input_str, spaced)
    elif selected_encoding == "八进制":
        return octal_to_ascii(input_str, spaced)
    elif selected_encoding == "十进制":
        # 对于十进制，如果是连续的，需要特殊处理
        return decimal_to_ascii(input_str, spaced)
    elif selected_encoding == "十六进制":
        return hex_to_ascii(input_str, spaced)
    
def binary_to_ascii(binary_str, spaced=True):
    if spaced:
        return ''.join([chr(int(b, 2)) for b in binary_str.split()])
    else:
        return ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])

def octal_to_ascii(octal_str, spaced=True):
    if spaced:
        return ''.join([chr(int(o, 8)) for o in octal_str.split()])
    else:
        # 在八进制中，每个ASCII字符通常由3位表示
        return ''.join([chr(int(octal_str[i:i+3], 8)) for i in range(0, len(octal_str), 3)])

def decimal_to_ascii(decimal_str, spaced=True):
    if spaced:
        return ''.join([chr(int(d)) for d in decimal_str.split()])
    else:
        # 十进制解码需要另外的逻辑来处理连续字符串
        # 这部分可以根据具体情况设计
        pass

def hex_to_ascii(hex_str, spaced=True):
    if spaced:
        return ''.join([chr(int(h, 16)) for h in hex_str.split()])
    else:
        return ''.join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])

########################################################################

def de_unicode(source_text,encode_type="utf-8"):
    result_text = bytes(source_text, encoding=encode_type).decode('unicode_escape')
    return result_text.strip()




class Class_Decode:
    def func_url(self,encode_type,source_text):
        result_text = str(urllib.parse.unquote(source_text, encode_type))
        return result_text.strip()



    def func_escape_u(self,encode_type,source_text):
        try:
            text = source_text.replace('%u', '\\u').replace('%U', '\\u')
            result_text = bytes(text, encoding=encode_type).decode('unicode_escape')
        except Exception as  e:
            return [0, '解码失败',"Escape_u编码"]
        return [1, result_text.strip(),"Escape_u编码"]
    def func_html(self,encode_type,source_text):
        try:
            result_text = html.unescape(source_text)
        except Exception as  e:
            return [0, '解码失败',"html编码"]
        return [1, result_text.strip(),"html编码"]

    # 得到分割数据 返回list
    def get_split_data(self, text):
        if ':' in text:
            text = text.split(":")
        elif ' ' in text:
            text = text.split(" ")
        elif ';' in text:
            text = text.split(";")
        elif ',' in text:
            text = text.split(",")
        else:
            list22 = []
            list22.append(text)
            text = list22
        return text
