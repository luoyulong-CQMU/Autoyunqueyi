
说明：

    1.本程序可自动学习yunqueyi视频【高血压系列】
    2.请按下列顺序配置好环境
    3.模拟器安装好yunqueyi.apk（软件包百度找）
    4.打开yunqueyi，完成一次登录，把第一次登录的提示什么的都点掉，不然会报错。
    5.打开Appium，点击start service
    6.运行autoxue.py
    f
环境配置：

1.安装  jdk1.8，安装包百度即可；

        在环境变量中新建JAVA_HOME变量，值为JDK安装路径，如C:\Program Files\Java\jdk1.8.0_05
        新建CLASSPATH变量，值为.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar;
        Path变量中添加：%JAVA_HOME%\bin和%JAVA_HOME%\jre\bin
        
2.安装  SDK

        在环境变量中新建ANDROID_HOME，值为SDK安装路径，如C:\Program Files (x86)\Android\android-sdk
        在Path变量中添加项：%ANDROID_HOME%\platform-tools 和 %ANDROID_HOME%\tools
		打开SDK Manager.exe 安装对应的工具和包,根据安卓版本进行安装，下一步即可

3.安装  `Appium",推荐通过npm安装，这样可以一键自动学习，无需通过点击启动service appium

            “本质是一个nodejs库所以要先安装nodejs，然后使用npm安装”
     	 3.1nodejs下载地址：https://nodejs.org/zh-cn/download/ 
		 3.2下载zip包解压到自己想放的目录，然后把该目录加入Path环境变量即可。 
		 3.3运行 npm install -g appium 3.4使用appinum-doctor确认环境配置无误 npm install -g appium-doctor appium-doctor --android		

4.安装一个安卓模拟器

		推荐Android7
		
5.安装python3.8

		下载地址百度即可，同样在path中添加python安装地址，配置好环境变量。
		
6.检测环境变量配置是否成功方法：

		jdk:    cmd输入java,未提示“未找到命令”即为成功
		sdk:    cmd输入adb devices，未提示“未找到命令”即为成功
		python:	cmd输入python，未提示“未找到命令”即为成功


