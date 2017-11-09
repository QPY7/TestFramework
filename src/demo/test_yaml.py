# -*- coding:utf-8 -*_
import yaml

yaml_str = """
name: 灰蓝
age: 0
job: Tester
"""

y = yaml.load(yaml_str)
print(y)