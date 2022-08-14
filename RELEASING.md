### 打包发布流程

```shell
# 环境准备
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade build
pip3 install --upgrade twine

# 免登陆: 创建token文件
touch ~/.pypirc
[testpypi]
  username = __token__
  password = pypi-ABCDEFGC5weXBpLm9yZwIkOGU0NmYwN2

# 构建和上传
python3 -m build
python3 -m twine upload --repository pypi dist/*
```
