# Markdown 标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
# Markdown 段落

末尾加两个空格  
末尾加两个空格  

不加空格
不加空格

用空行还换行

用空行还换行

## 字体

*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___

## 分隔线

***

* * *

*****

- - -

----------

## 删除线

RUNOOB.COM
GOOGLE.COM
~~BAIDU.COM~~

## 下划线

<u>
something
<u>

## 脚注

生成一个脚注1[^footnote].
[^footnote]: 这里是 **脚注** 的 *内容*.

生成一个脚注2[^foot].
[^foot]:这里是**脚注2**的*内容*.

# Markdown 列表

* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项
- 第二项
- 第三项

## 嵌套
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第一个元素

## Markdown 区块

> 区块引用

> 菜鸟教程

> 学的不仅是技术更是梦想

## embeded

> 最外层

> > 第一层嵌套

> > > 第二层嵌套

## 区块中使用列表

> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项

## 列表中使用区块

* 第一项
    > 菜鸟教程
    > 学的不仅是技术更是梦想
* 第二项

# Markdown 代码

`printf()` 函数

## 代码区块

代码区块使用 4 个空格或者一个制表符（Tab 键）。

    int a;
    int b;
    
    local function some()
    end
    
```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```

# Markdown 链接

这是一个链接 [菜鸟教程](https://www.runoob.com)

## 高级链接

链接也可以用变量来代替，文档末尾附带变量地址：
这个链接用 1 作为网址变量 [Google][1]
这个链接用 runoob 作为网址变量 [Runoob][runoob]
然后在文档的结尾为变量赋值（网址）

  [1]: http://www.google.com/
  [runoob]: http://www.runoob.com/

# Markdown 图片

![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png)

![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png "RUNOOB")

这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾位变量赋值（网址）

[1]: http://static.runoob.com/images/runoob-logo.png

# Markdown 表格

| 表头   | 表头   |
| ----   | ----   |
| 单元格 | 单元格 |
| 单元格 | 单元格 |

## 对齐方式

| 左对齐 | 右对齐 | 居中对齐 |
| :----- | ----:  | :----:   |
| 单元格 | 单元格 | 单元格   |
| 单元格 | 单元格 | 单元格   |


# Markdown 高级技巧

## 支持的 HTML 元素

使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑

## 转义

**文本加粗** 
\*\* 正常显示星号 \*\*

## Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

```
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  小括号
#   井字号
+   加号
-   减号
.   英文句点
!   感叹号
```

## 公式

$$x^2+y^2=1$$
