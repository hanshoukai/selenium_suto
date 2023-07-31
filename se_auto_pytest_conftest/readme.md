## 说明

test_po_case下的测试文件

​	1个test_*.py文件，方法从上往下依次执行 只会打开一次浏览器生成一个driver，具有连贯性

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
# 进入项目，pytest会将项目下的test文件夹中的test开头的所有用例 均执行【在同一个浏览器运行哦！！！】
cd se_auto_pytest_conftest && python -m pytest
```

