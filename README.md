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
6.对比两份core文件中指定源文件中的变量，并输出差异(Finish);  
6.对比两份core文件的数据区的内存（异常和正常设备的core文件），输出不同点()；  

## 变更履历  
2023-04-05：完成功能：对比两份core文件（正常和出现异常情况下）中指定源文件的内容，并标注差异项。  
功能结果如下：
其中 右侧的 core1 是发生异常时保存内存数据，右侧是正常时导出的内存数据，对比两份数据，出现异常时，使用 ‘x’标注，否则不进行标注。  
此外，由于变量的结构长度可能会超过显示用的文本框，因此根据文本框和变量长度，进行自动换行处理。  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/varCompare.png)
结果分析如下：  
通过比对发现，结构体 Mgr_st *pMgr->cmd 数值不同（OK时为99，NG时为97）  
实际项目中存在差异的变量会有很多，需要结合源码进行分析。  
  
2023-04-24：上传基础代码  
显示寄存器信息如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showreg.png)

显示反汇编如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showASM.png)

显示变量值如下：  
![image](https://github.com/oldChen3/coredump_analyse_tool/blob/main/img/showvar.png)
