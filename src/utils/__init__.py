# -*- coding: utf-8 -*-
import base64

# Base64 编码
def base64_encode(data):
    """
    将输入数据编码为 Base64 格式。

    :param data: 字符串或字节数据
    :return: Base64 编码后的字符串
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    encoded = base64.b64encode(data)
    return encoded.decode('utf-8')

# Base64 解码
def base64_decode(encoded_data):
    """
    解码 Base64 格式的数据。

    :param encoded_data: Base64 编码的字符串
    :return: 解码后的原始字节数据
    """
    decoded = base64.b64decode(encoded_data)
    return decoded.decode('utf-8')
