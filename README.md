# allure pytest framework

This is pytest framework with python3, use allure to generate report.
include two test modules, one is for mysql testing, another is for math function testing.

The scripts run on windows10 system. setup environment steps follows:
1). install Java
Add it in the system environment Variables(Path), check java install successfully

    C:\WINDOWS\system32>java -version
    java version "1.8.0_202"
    Java(TM) SE Runtime Environment (build 1.8.0_202-b08)
    Java HotSpot(TM) 64-Bit Server VM (build 25.202-b08, mixed mode)

2). install allure:
download ALlure zip package(allure-2.7.0.zip), unzip this package to your pytest project folder. Add allure  to environment Variable --> System variable "Path", such as "D:\xxxx\pytest_allure_framework\allure-2.7.0\bin" into "Path". Check allure install successfully

    C:\WINDOWS\system32>allure --version
    2.7.0

3). Install all the dependencies
    pip install -r requirements.txt

4). run test cases under project folder:
    pytest can generate different format report.

    a> generate html format report:
        pytest tests --html=.\logs\log.html

    b> generate normal txt format report
        pytest tests --resultlog=log.txt

    c> use allure to generate report:
        make sure report directory exists in the root folder
        pytest src/tests --alluredir=report/

        To view the allure report on the browser.
        allure serve report/


