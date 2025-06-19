## YTLA 通用框架
### 复制 - 粘贴 - 重命名， 三步开搞
### 各个文件夹下的文件用途
#### api
放各类api请求  
需要一个request，一个request modifier
#### caller
放跨各个工程的内容调用的代码
#### dao
放DB连接和执行特定SQL的代码
#### dataset
将数据直接写在py文件内，存放于此以供调用
#### func
放各类通用的函数。分ytla原装内容和各工程特制内容，特制的用Customized作区分
#### generator
自动生成器相关
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

###
开发规则
1. 后端  
    1 不论是module还是card，都是从dao层开始，然后是process层，最后是route层  
    2 对于需要从其他工程获取数据的，需要在caller层定义一个函数，然后在route层调用