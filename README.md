# 简介
flask web app 样板程序。使用 Docker 进行构建和分发。

本应用部分参考自 [12-factor](https://12factor.net/) 原则。


# 依赖：
- Flask 框架
- DB：
  - ORM: Flask-SQLAlchemy
  - MySQL + mysql-connector-python
- 部署： waitress


# 手动部署
```bash
$ git clone <repo>
$ cd flask-sampleproject

$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple # 清华 pypi 镜像。

# 在运行应用或单元测试前需要设置好环境变量，示例见项目根目录中的 env.*.sh.example 文件。
# run test
$ python -m unittest discover

# run dev app
## 首先应该先为此项目创建数据库。
$ flask create_table # 创建数据库表。
$ flask run

# run production app
$ python run.py
```

# Docker
## 构建镜像：
```bash
$ docker image build --tag=flask-sampleproject .
```

## 运行：
```bash
$ cp docker.env.example docker.env
# 并填入环境变量

$ docker run \
  --name='flask-sampleproject' \
  --network=host \
  --env-file='docker.env' \
  -v "$PWD/log":/flask-sampleproject/log \
  -d flask-sampleproject
```

## 使用 docker-compose 启动：
```bash
$ docker-compose up -d
```


# 管理：
日志
- 文件：`log/warning.log`
- `docker-compose logs flask-sampleproject`

其他：
- `docker-compose exec flask-sampleproject bash`：进入容器 bash 命令行交互。
- `docker-compose exec flask-sampleproject flask shell`：进入容器 flask shell 交互。
