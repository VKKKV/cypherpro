# coding=utf-8
import collections
import random
import re
import string
# from Crypto.Cipher import AES


class Class_Encrypt:
    def func_Kaiser(self, source_text, key=3):
        result_text = ""
        for c in source_text:
            if 'a' <= c <= 'z':
                result_text += chr(ord('a') + ((ord(c) - ord('a')) + key) % 26)
            elif 'A' <= c <= 'Z':
                result_text += chr(ord('A') + ((ord(c) - ord('A')) + key) % 26)
            else:
                result_text += c
        return {"status": 1, "result_text": result_text, "algorithm": "凯撒密码"}