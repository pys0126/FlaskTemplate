import traceback
from flask import Response
from typing import Union, Any
from application.util.LogUtil import write_error_log
from application.util.ResponseUtil import ResponseUtil
from application.enumeration.StatusCodeEnum import StatusCodeEnum
from application.util.TimeUtil import now_format_datetime


class BasicException(Exception):
    """
    基本自定义异常
    """

    def __init__(self, status_code: int = StatusCodeEnum.ERROR.value,
                 error_message: str = "内部错误，请稍后再试") -> None:
        """
        构造方法
        :param status_code: 异常码
        :param error_message: 异常消息
        """
        self.status_code: int = status_code
        self.error_message: str = error_message

    @staticmethod
    def exception_handle(exception: Any) -> Response:
        """
        异常钩子
        :param exception: 异常类
        :return:
        """
        basic_exception: BasicException = BasicException()
        if isinstance(exception, BasicException):
            basic_exception.status_code = exception.status_code
            basic_exception.error_message = exception.error_message
        # 打印、写入异常堆栈信息
        print(f"{now_format_datetime()}\tErrorInfo => ", exception)
        write_error_log(traceback.format_exc())
        # 返回Response
        return ResponseUtil(code=basic_exception.status_code, message=basic_exception.error_message).fail()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.error_message
