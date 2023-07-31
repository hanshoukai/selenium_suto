## 说明

test_po_case下的测试文件

​	1个test方法重启一次driver，test方法从上往下依次执行，每执行一个方法既会重启一次浏览器 重新生成一次driver

## 所需类库

> pytest 
>
> time
>
> selenium
>
> webdriver_manager[自动识别本地浏览器版本 下载对应驱动]

## 运行

```shell
# 进入项目，pytest启动，每个test方法会重新生成一个driver
cd se_auto_pytest_no_conftest && python -m pytest 
```

