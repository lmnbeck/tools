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