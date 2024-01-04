# coding=utf-8

class Class_Binary:
    def exec_Binary(self, source_text,original_base,target_base):
        Binary_type=original_base+'_'+target_base
        all_result = ''
        all_text = source_text.split(" ")
        result_text=[0,'']
        for text in all_text:
            result_text = getattr(self, 'Binary_'+Binary_type)(text)
            all_result += str(result_text[1]).replace('0o', '').replace('0x', '').replace('0b', '') + ' '
        if all_result != "":
            return [result_text[0],all_result,result_text[2]]
        else:
            return [result_text[0],'转换失败！',result_text[2]]


    def Binary_2_8(self, text):
        try:
            result = int(text, 2)
            result_text = str(oct(result))
        except Exception as e:
            return [0,'您输入的不是2进制','2->8']
        return [1,result_text,'2->8']

    def Binary_2_10(self, text):
        try:
            result = int(text, 2)
            result_text = str(result)
        except Exception as e:
            return [0,'您输入的不是2进制','2->10']
        return [1,result_text,'2->10']

    def Binary_2_16(self, text):
        try:
            result_text = str(hex(int(text, 2)))
        except Exception as e:
            return [0,'您输入的不是2进制','2->16']
        return [1,result_text,'2->16']


    def Binary_8_2(self, text):
        try:
            result = int(text, 8)
            result_text = str(bin(result))
        except Exception as e:
            return [0,'您输入的不是8进制',"8->2"]
        return [1, result_text,"8->2"]

    def Binary_8_10(self, text):
        try:
            result = int(text, 8)
            result_text = str(result)
        except Exception as e:
            return [0,'您输入的不是8进制',"8->10"]
        return [1, result_text,"8->10"]

    def Binary_8_16(self, text):
        try:
            result = int(text, 8)
            result_text = str(hex(result))
        except Exception as e:
            return [0,'您输入的不是8进制',"8->16"]
        return [1, result_text,"8->16"]

    def Binary_10_2(self, text):
        try:
            s = int(text)
            result_text = str(bin(s))
        except Exception as e:
            return [0,'您输入的不是10进制',"10->2"]

        return [1, result_text,"10->2"]

    def Binary_10_8(self, text):
        try:
            s = int(text)
            result_text = str(oct(s))
        except Exception as e:
            return [0,'您输入的不是10进制',"10->8"]
        return [1, result_text,"10->8"]

    def Binary_10_16(self, text):
        try:
            s = int(text)
            result_text = str(hex(s))
        except Exception as e:
            return [0,'您输入的不是10进制',"10->16"]
        return [1, result_text,"10->16"]

    def Binary_16_2(self, text):
        try:
            result_text = str(bin(int(text, 16)))
        except Exception as e:
            return [0,'您输入的不是16进制',"16->2"]
        return [1, result_text,"16->2"]

    def Binary_16_8(self, text):
        try:
            result = int(text, 16)
            result_text = str(oct(result))
        except Exception as e:
            return [0,'您输入的不是16进制',"16->8"]
        return [1, result_text,"16->8"]

    def Binary_16_10(self, text):
        try:
            result = int(text, 16)
            result_text = str(result)
        except Exception as e:
            return [0,'您输入的不是16进制',"16->10"]
        return [1, result_text,"16->10"]

    def func_Numeric_Conversion(self, source_text,key1,key2):
        try:
            return_Data = ''
            if key1 != '' and key2 != '':
                all_text = source_text.split(" ")
                all_result = ''
                for text in all_text:
                    # # print(text)
                    from_ = int(key1)
                    to_ = int(key2)
                    # from_进制转换为十进制
                    ten_num = sum([int(i) * from_ ** n for n, i in enumerate(text[::-1])])
                    # print(ten_num)
                    # 十进制转换为to_进制
                    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
                    b = []
                    while True:
                        s = ten_num // to_  # 商
                        y = ten_num % to_  # 余数
                        b = b + [y]
                        if s == 0:
                            break
                        ten_num = s
                    b.reverse()
                    for i in b:
                        return_Data += str(a[i])
                    all_result += return_Data + ' '
                return 1,all_result
        except Exception as e:
            return [0, e]
