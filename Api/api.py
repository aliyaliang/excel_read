from config import host
import requests
import logging

# 加上日志
logger = logging.getLogger(__name__)


class Api:
    # 1.初始化
    def __init__(self, case):
        # 1.获取url = host+path
        self.url = host + case.get("path")

        # 2.请求方法
        self.method = case.get("method")

        # 3.请求参数类型：
        self.param_type = case.get("param_type")

        # 4.请求信息头
        self.headers = case.get("headers")

        # 5.请求参数
        self.params = case.get("params")

    # 2.查询方法
    def _get(self):
        logger.info("正在调用get请求方法。。。")
        r = requests.get(url=self.url, params=self.params, headers=self.headers)
        return r

    # 3.新增方法
    def _post(self):
        logger.info("正在调用post请求方法。。。")
        # 判断参数类型
        if self.param_type == "json":
            return requests.post(url=self.url, json=self.params, headers=self.headers)
        elif self.param_type == "Data":
            return requests.post(url=self.url, data=self.params, headers=self.headers)

    # 4.更新方法
    def _put(self):
        logger.info("正在调用put请求方法。。。")
        r = requests.put(url=self.url, json=self.params, headers=self.headers)
        return r

    # 5.删除方法
    def _del(self):
        logger.info("正在调用delete请求方法。。。")
        r = requests.delete(url=self.url, params=self.params, headers=self.headers)
        return r

    # 6.调用运行方法
    def run_method(self):
        logger.info("正在调用运行接口方法。。。")
        # 判断方法
        if self.method=="get":
            return self._get()
        elif self.method == "post":
            return self._post()
        elif self.method == "put":
            return self._put()
        elif self.method == "delete":
            return self._del()
