# coredump_analyse_tool
目的：  
1.使用图形界面分析coredump；  
2.用于分析因为变量(内存)意外被修改导致的问题(长时间偶发性问题)；  

功能：可视化分析coredump文件内容，包括有：  
1.显示异常时的寄存器信息(Finish)；  
2.显示栈调用信息(Finish)；  
3.显示异常位置的反汇编代码(Finish)；  
4.显示异常时，指定文件中全局变量此时的数值(Finish)；  
5.自动分析指定函数的参数值()；  
6.对比两份core文件的数据区的内存（异常和正常设备的core文件），输出不同点()；  

## 变更履历  
2023-04-24：上传基础代码  
显示寄存器信息如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showreg.png)

显示反汇编如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showASM.png)

显示变量值如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showvar.png)
