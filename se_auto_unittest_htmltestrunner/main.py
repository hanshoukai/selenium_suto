# /usr/bin/env python
# coding=utf-8
import unittest
# import HTMLTestRunner
import HTMLTestRunner_CN_Chart_Screen as HTMLTestRunner

# 相对路径
testcase_path = ".\\testcase"
report_path = ".\\report\\report.html"


def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


suite = creat_suite()
fp = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试结果", description="测试搜索结果")
runner.run(suite)
fp.close()
