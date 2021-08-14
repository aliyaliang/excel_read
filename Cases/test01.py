from Base.file_tool import FileTool
import pytest
from Api.api import Api
from Base.common_assert import common_assert
import logging

logger = logging.getLogger(__name__)


class Test01:
    # 1.实例化获取工具类对象
    tool = FileTool("case01_add_goods.xlsx")

    # 2.读取excel ->将数据从excel中读取并写入到json文件中
    tool.read_excel()

    # 3.测试方法
    @pytest.mark.parametrize("case", tool.read_json())
    def test01(self, case):
        logger.info("正在执行调用执行数据：%s" %case)
        try:
            # 调用 执行接口方法
            r = Api(case).run_method()
            print("响应数据为 %s" %r.text)
            print("响应状态码：%s" %r.status_code)
            # 断言
            common_assert(r, case)
            # 将执行结果写入报告
            Test01.tool.write_excel(case.get("x_y", "执行成功"))
        except Exception as e:
            Test01.tool.write_excel(case.get("x_y", "执行失败！原因：%s" %e))
            logger.error("错误，原因：%s" %e)
            raise
