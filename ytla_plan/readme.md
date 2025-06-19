## YTLA 通用框架
### 复制 - 粘贴 - 重命名， 三步开搞
这是一个基于python-flask制定的代码框架。
### 各个文件夹下的文件用途
#### ai_tools
以类似mcp的方式向大模型ai提问用以返回特定内容的代码 
#### api
放各类api请求  
需要一个request，一个request modifier
#### caller
放跨各个工程的内容调用的代码
#### const
存放常量
#### dao
放DB名称和执行特定SQL的代码
#### dataset
将数据直接写在py文件内，存放于此以供调用
#### func
放各类通用的函数。分ytla通用框架的代码和各工程特制内容，特制的用Customized作区分
几乎所有的功能代码都放在这里
#### instance
定制的instance可以放在这里
#### process
在工程内对已经获得的数据作任意类型的进一步处理或分析  
原本打算定义analyze的，但是和process不用做过多区分
#### routes
工程内的路由，用于定义api的路径和方法
#### schedule
对特定的工程内步骤执行定期化反复执行过程
#### script
工程内的单次的数据处理脚本，通常以读取文件或对外api获取数据后进行简单处理并储存为主
