# 设计思路

脚手架是一个很早之前就考虑的工作.  
早在初版完成时就有打算.  
但是，最初的脚手架只是考虑生成那些相同的、底层的代码，并没有从架构上看应该怎样去生成.  
——尽管生成结果可能相同，但是意义上差别会很大.  

## core version VS language framework

架构从两个层面上做考虑：  
核心版本（OS）  
语言框架  

对于同一语言框架，不论其核心版本使用的是哪个，使用这个语言框架生成的架构其实是相同的：  
核心控制的是核心的数据结构和调用方式，而不是这种语言的调用方式  

举例而言  
如果一个核心版本CA选定了两种前后端语言B1和F1，而另一个核心版本CB选定的前后端语言是B1和F2  
那么，CA和CB的后端框架是相同的，都会使用B1的文件架构  
并且，由于YTLA框架下的特性命名规则要求  
type - structure(card/module) - subtype  
而文件架构定义往往是针对subtype层级的  

YTLA之所以会在架构上规定如此严格，正是因为有着严格的脚手架设计、高度自动化、以及对生成式AI的利用考量.  

scaffold脚手架所做的事情是：
为用户生成一套足以支持应用正常运行"Hello World"级别的基础文件.  
——尽管里面可能有很多用不上的文档生成.或者说，因为要生成的基础文件可能会很多，让人手工拷贝又繁琐、又容易遗漏出错  
这种场合下，使用脚手架无疑是受益的.

## 如何区分上述二者？

简单来说，core version是在这个core下的特定产物  
比如，card，在classic里特指的是side card  
而card和module都是subtype的实现  

而language framework则更看重一个语言框架下的特性
比如，flask的blueprint，vue的pinia store和composable api  

一般而言，language framework的实现优先级是高于core version的  
这可以理解为，如果有一个复用的类型，那么在scaffold中肯定是先考虑language framework层面的实现，再把core version的特性添加进去.  

## doc本身

docs目录本身是一个比较特殊的考虑.  
其实类似的将来会有很多，比如openAPI的接入（这个也是已经考虑了的问题）.  
从docs来看，其实是一个更高层面的设计概念.  
它不取决于语言框架用的是何种，也不考虑设计的核心版本  
而是作为YTLA这个产品本身的统一规则生成的.  
（这就是为什么会考虑openAPI。openAPI作为一种规范合约，在各种语言中都成立）