## SerWice

![](docs\source\images\logo.png)

### 概述

SerWise 是为自动回复服务程序设计的 **领域特定语言(domain specific language)** 

不同于传统高级语言，Serwice语言不提供数据结构和面向对象编程，具有极强针对性，纯粹的过程式编程和自由的语法规则能够适应绝大多数场景需求，对于特殊场景，解释器为脚本编写者提供了充分可修改，可控制，可添加的内部API，考虑自动应答服务与NLP，TTS等技术的紧密联系性，解释器底层使用 **python编写**，对算法工程师和维护人员开放 ``listen`` ``speak`` ``analyzer`` ``database`` 四个方面的底层API，可以实时根据场景需求增添修改执行命令和逻辑

### installation

**安装教程**

操作系统:

- `Centos 7``
- ``Windows 10`
-  MacOS `

Python版本: 

- `3.8.8`

获取并安装SerWise解释器

1. 用以下命令下载SerWise项目包

   ```bash
   git clone https://github.com/zjl222666/DSL.git
   ```

2. 进入下载路径，使用pip工具包安装该项目包:

   ```bash
   # install for use
       # Note: use `--user` option to install the related packages in the user own directory(e.g.: ~/.local)
       pip install . --user
        
       # install for development(if you want to modify the core)
       pip install -e . --user
   ```

### doc

更多信息请参见[serWise文档](docs\build\html\index.html)

