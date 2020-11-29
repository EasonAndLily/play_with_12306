# 玩转12306

Hello，陌生的开发者，你好，欢迎来到爬虫的世界！如果你是一名爬虫爱好者，如果你对Python感兴趣，如果你对技术改变世界着迷，那么，这个实战项目将帮助你取得进步！让我们开始吧！

## 项目介绍

本项目是一个在[12306](https://www.12306.cn/index/)上自动购买火车票的Python爬虫类应用程序，以学习爬虫和算法为目的实战练习项目。不管你是Python的初学者还是资深爬虫专家，只要你12306购票充满兴趣，详细你都能从中学到知识！

本项目致力于实现全自动化购票和抢票，只需要通过简单的配置，即可实现包括自动登录认证、自动刷票、自动购买等功能，目前此项目还处于开发阶段，如果你有兴趣，我们一起来完成它！

## 分支说明

本项目总共分为两个分支：master和dev。

### master分支

此分支上面的代码属于稳定版，基本上可以正常使用，如果你是初学者，那么请使用此分支来进行学习最好不过了！

### dev分支

此分支属于开发分支，作为开发者的我们经常需要将新的代码提交到这个分支上面，这个分支上面不属于稳定版本。我们会在定期将此分支的代码Merge到Master上面去，以保证Master的更新迭代！

## 项目结构说明

此项目的文件结构及功能如下：

* **README.md:** 本项目的说明文件，在入手该项目之前最好读一读！
* **run.py:** 项目的启动文件，使用此文件启动该项目。
* **requirements.txt:** 项目依赖的第三方库的说明文件。
* **.gitignore:** 里面记录了git需要忽略的文件。
* **src目录:** 此文件夹是项目的代码目录，里面包括了抢票的所有源代码。
* **src/core/main.py:** 此文件是主项目买票流程控制文件，里面控制了登陆认证，刷票，买票等的整个流程。
* **src/core/auth模块:** 此模块主要负责用户登陆认证的相关业务，主要包括验证码识别、滑块验证、用户名密码登陆等逻辑。
* **src/core/ticket模块:** 此模块主要负责刷票、购票等业务逻辑。
* **src/core/tools模块:** 此模块主要是一些工具函数，包括爬虫方法工具、cookie存储与读取、config文件校验等的工具函数。
* **src/test模块:** 此模块是本项目的测试模块，里面包含了所有的测试方法。
* **config目录:** 此目录是本项目的配置目录，包含了用户需要的配置、车站信息等
* **model目录:** 此目录包含12306图片验证码识别的算法模型，是自动识别验证码的关键。
* **doc目录:** 文档目录，包含了该项目的架构说明、处理流程图、设计模式等方面的说明。

## 本地搭建抢票程序

#### step1：安装Python3，并安装虚拟开发环境(virtualenv)

本项目的Python版本为Python3以上，基于此，我们推荐您使用虚拟开发环境来隔离Python运行环境：

* **macOS 或 Linux:**

    ```bash
    python3 -m pip install --user virtualenv
    ```

* **Windows**

    ```bash
    py -m pip install --user virtualenv
    ```

#### Step2: 创建虚拟环境并激活

安装好virtualenv之后，进入此项目文件夹中，创建虚拟开发环境：

* **macOS 或 Linux:**

    ```bash
    cd play_with_12306
    python3 -m venv env
    source env/bin/activate
    ```

* **Windows**

    ```bash
    cd play_with_12306
    py -m venv env
    .\env\Scripts\activate
    ```

#### Step3：安装依赖模块

请使用以下命令来安装依赖的模块：

```bash
pip install -r requirements.txt
```

#### Step4: 修改配置文件

在config目录下面的config.py文件中，修改下面的配置：

* CAPTCHA_IDENTIFY：识别验证码方式，1表示手动，0表示自动
* LOGIN_METHOD：认证方式，默认为1,可选范围为[0: 调用API自动登陆，1: 浏览器自动登录 2：扫码登陆]
* USERNAME：您的12306网站的用户名
* PASSWORD：您的12306网站的密码
* FROM_STATION：所购买票的始发站
* END_STATION：所购买票的终点站
* TRAIN_DATA：购票的出发日期
* TRAIN_NUMBER：列车号
* PASSENGERS：乘车人，可以添加多个，使用数组包裹，如["张三","李四"]
* SEAT_TYPE：仅仅高铁支持的作为类型
* CHOOSE_SEATS：仅仅高铁支持的座位编号

##### Step4.1: 配置浏览器自动登陆方式【如果配置LOGIN_METHOD为非1， 请忽略此步骤】

如果您在`config.py`里面配置了LOGIN_METHOD为1，则此项目使用selenium来启动浏览器登陆认证，相关的配置请参考这里：
* [浏览器登陆认证配置说明](./doc/browser_auth_config.md)

#### Step5: 运行此项目

运行此项目

```bash
python3 run.py
```

如果输出如下信息，证明您的本地抢票环境已经搭建完成：

```bash
Corrupt JPEG data: 12 extraneous bytes before marker 0xd9
题目为: ['电子秤']
选项1.热水袋
选项2.拖把
选项3.龙舟
选项4.热水袋
选项5.沙拉
选项6.海苔
选项7.电子秤
选项8.路灯
输入的图片验证码序号为：7
验证码认证成功！
```


## 开发者参考文档

待更新！

## 法律声明

本项目主要用于爬虫算法的学习交流，不以盈利赚钱为目的，切勿将此项目应用于非法抢票中，如若因此造成的法律后果，请自行承担！