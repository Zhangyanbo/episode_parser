# 自动提取影视剧情节


## 安装

```bash
python setup.py install
```

## 使用

### 模糊搜索

未完成

### 简单搜索

爬取数据：

```python
import eparser
from eparser import reader

baidu = reader.baidu('https://baike.baidu.com/item/亮剑/10639926')
```

搜索情节：

```python
baidu.search('牺牲')

'''output:
{'[7/30]第7集': ['八路军副参谋长左权在指挥机关与部队突围时壮烈牺牲'],
 '[14/30]第14集': ['为减少部队人员伤亡，李云龙仍旧选择了牺牲秀芹，并向着城墙上开了炮']}
'''
```

