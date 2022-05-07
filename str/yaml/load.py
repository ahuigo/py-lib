s='''
defaults: &ref_default
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *ref_default
test:
  database: myapp_test
  <<: *ref_default
# https://www.ruanyifeng.com/blog/2016/07/yaml.html
bool: true
str1: 'a\nb'
str2: "a\nb"
str3: 'ahui''s blog'
str4: "ahui's blog"
list:
    - 1
    - 2

# convert to string
e: !!str 123
f: !!str true

# datetime
iso8601: 2001-12-14t21:59:43.10-05:00 

# 换行
data: |
  abc
  [2,4,5]
json: >
    [1,2,3]
    [2,4,5]

# +表示保留文字块末尾的换行(默认)，-表示删除字符串末尾的换行。
data2: |-
    line1
    line2

'''

import yaml
d=yaml.safe_load(s)
import json
d['iso8601']= d['iso8601'].__str__()
print(json.dumps(d, indent=4,))
print("str1:", d['str1'].encode())
print("str2:", d['str2'].encode())
