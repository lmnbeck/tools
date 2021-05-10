# 2.22输出\n等
print(r'd:\nmdf.xlsx')
print('d:\\nmdf.xlsx')

# 查询类型用type（）

# 2.24数据类型转换 str（） int（） float（）
## int（）转换浮点数，小数直接舍弃
a = 88
b = str(a)
print(type(a))
print(type(b))

a = '88'
b = int(a)
print(type(a))
print(type(b))

# 2.3.1 列表
class1 = ['李白', '王维', '孟浩然', '王昌龄', '王之涣']
## 列表元素个数用len(列表名)统计
len(class1)
## 列表切片 "左闭右开"
print(class1[:-2])
## 添加元素用append()
class1.append('80')
print(class1)
## 列表转换为字符串: '连接符'.join(列表名)
a = ' '.join(class1)
print(a)
## 字符串转换为列表: 字符串.split('分隔符')
print(a.split(' '))

# 2.3.2 字典 {key:value, key2: value2, ......}
class2 = {'李白':85, '王维': 95, '孟浩然': 75, '王昌龄': 65, '王之涣': 55}
## 提取键值
score= class2['王维']
print(score)
## 遍历字典
print(class2.items())

# 2.3.3 元组合集合
## 元组是用小括号的不可修改的列表
a = ('李白', '李白', '王维', '孟浩然', '王昌龄', '王之涣')
print(a)
## 集合是一个无序的不重复序列，可用set（）创建
print(set(a))

price = 100
price += 10
print(price)

# 3 自动化整理计算机文件
## 3.1 strip()函数的技巧
str1 = 'xyzxyz-Python-zyxzyx'
str2 = str1.rstrip('zyx')
print(str2)

# 4 自动化处理PDF文件
## python版本切换：2.1. 将 python 各版本添加到 update-alternatives
'''
2.1. 将 python 各版本添加到 update-alternatives
$ which python3.8
/usr/bin/python3.8

$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

$ which python3.5
/usr/bin/python3.5

$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 2

2.2. 配置 python3 默认指向 python3.8
$ sudo update-alternatives --config python3


There are 2 choices for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.5   2         auto mode
  1            /usr/bin/python3.5   2         manual mode
  2            /usr/bin/python3.8   1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 2

选择/输入 2, 回车。

二、卸载python3.8
1、卸载python3.8
sudo apt-get remove python3.8
1
2、卸载python3.8及其依赖
sudo apt-get remove --auto-remove python3.8
1
3、清除python3.8
sudo apt-get purge python3.8
or
sudo apt-get purge --auto-remove python3.8

注释：

此方法卸载python比较彻底，所以适合更换python版本时使用。
'''
## 解决chromedriver问题
''' error message:
Exception has occurred: WebDriverException
Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
  File "/home/ubuntu/workSpace/tools/pythonWorkAutomation/downloadPDF.py", line 5, in <module>
    browser = webdriver.Chrome()
'''
### 找到chrome版本
'''
安装：
sudo apt-get install -y chromium-browser

安装信息最后：
Setting up chromium-browser-l10n (90.0.4430.72-0ubuntu0.18.04.1) ...
**90.0.4430.72**是版本号

去http://chromedriver.storage.googleapis.com/index.html 网站找到相应的版本驱动
ubuntu 安装chromedriver

// 下载对应的版本
wget -N https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
// 解压
unzip chromedriver_linux64.zip
chmod +x chromedriver
// 复制文件
cp chromedriver /usr/bin/chromedriver
————————————————

## 添加代码使得chrome正常运行
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
'''