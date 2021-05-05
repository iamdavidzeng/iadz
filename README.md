# iadz
iadz is a personal repo use for starting different tutorial

```
git clone git@github.com:iamdavidzeng/iadz.git

cd /path/to/iadz/python
```

## Prerequisites
- [Python3](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Initiate dev environment
1. Use virtualenv initial your virtual python environment first.
```
virtualenv -p python3 .env
```
2. Activate your virtual environment
```
source .env/bin/activate
```
3. Install packages
```
pip install -e ".[dev]"
```