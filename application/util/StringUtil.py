"""
字符串工具包
"""
import hashlib
import random
import re
import base64
import urllib.parse
from urllib.parse import urlparse
from uuid import uuid4


def url_encode(text: str) -> str:
    """
    url编码
    :param text: 原始文本
    :return: 编码后的字符串
    """
    return urllib.parse.quote(text)


def random_uuid() -> str:
    """
    生成随机uuid字符串
    :return: uuid字符串
    """
    result: str = str(uuid4())
    return result.replace("-", "")


def base64_encode(text: str) -> str:
    """
    base64加密
    :param text: 待加密文本
    :return: 加密后的文本
    """
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def base64_decode(text: str) -> str:
    """
    base64解密
    :param text: 待解密文本
    :return: 解密后的文本
    """
    return base64.b64decode(text).decode("utf-8")


def md5_encode(text: str) -> str:
    """
    MD5加密
    :param text: 待加密文本
    :return: 加密后的文本
    """
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


def sha1_encode(text: str) -> str:
    """
    SHA-1加密
    :param text: 待加密文本
    :return: 加密后的文本
    """
    # 创建一个新的hash对象
    sha_signature = hashlib.sha1(text.encode())
    # 获取加密后的字符串
    sha_signature_hex = sha_signature.hexdigest()
    return sha_signature_hex


def is_valid_email(text: str) -> bool:
    """
    验证是否是邮箱
    :param text: 原文本
    :return:
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, text) is not None


def is_valid_url(text: str) -> bool:
    """
    验证是否是url
    :param text: 原文本
    :return:
    """
    for t in text.split(","):
        try:
            result = urlparse(t)
            if not all([result.scheme, result.netloc]):
                return False
        except ValueError:
            return False
    return True


def is_valid_uuid(text: str) -> bool:
    """
    是否为uuid
    :param text: UUID字符串
    :return:
    """
    for t in text.split(","):
        pattern = r'^[0-9a-fA-F]{32}$'
        match = re.match(pattern, t)
        if match:
            return True
    return False


def is_valid_password(text: str) -> bool:
    """
    验证密码是否符合规则
    :param text: 原文本
    :return:
    """
    # 使用正则表达式匹配密码规则
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{6,}$'
    if re.match(pattern, text):
        return True
    else:
        return False


def generate_verification_code() -> str:
    """
    生成6位随机验证码
    :return:
    """
    code: str = ""
    for _ in range(6):
        digit = random.randint(0, 9)
        code += str(digit)
    return code
