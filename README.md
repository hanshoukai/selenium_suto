# selenium_suto
分别采用unittest和pytest编写的web端UI自动化测试框架Demo

## se_auto_unittest_htmltestrunner
为Python + selenium + unittest +httprunner编写
testcase目录下的test*.py文件每一个是一个单独的验证点

## se_auto_pytest_no_conftest
和unittest一样，test*.py文件中每个方法生成一个driver，打开一次浏览器

## se_auto_pytest_conftest
conftest为session级别
只会生成一个driver打开一次浏览器，去执行所有的test*.py文件中全部的方法
