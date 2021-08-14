import logging

logger = logging.getLogger(__name__)

# 断言应根据具体项目调整
def common_assert(response, case):
    logger.info("正在调用断言公共方法。。。")
    # 获取响应数据
    result = response.json
    # 获取预期数据
    expect = case.get("expect")
    # 断言响应状态码status code
    assert response.status_code == expect.get("code"), "错误！响应status_code：%s，预期status_code：%s" %(response.status_code, expect.get("code"))
    # 断言success
    assert result.get("success") == expect.get("result").get("success"), "错误！响应success：%s，预期success：%s" %(result.get("success"), expect.get("success"))
    # 断言错误码code
    assert result.get("code") == expect.get("result").get("code"), "错误！响应code：%s，预期code：%s" %(result.get("code"), expect.get("code"))
    # 断言message
    assert result.get("message") == expect.get("result").get("message"), "错误！响应msg：%s，预期msg：%s" %(result.get("message"), expect.get("message"))
