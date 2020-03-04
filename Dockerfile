FROM python:3.7
LABEL maintainer="gutianci@pwrd.com"

# 将文件复制到镜像中。
COPY . /flask-sampleproject

# venv
WORKDIR /flask-sampleproject
RUN python3 -m venv .venv

ENV VIRTUAL_ENV='/flask-sampleproject/.venv'
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 声明我们的程序运行需要的环境变量
# 可以在 run 时覆盖
# 作用：
# 1. 文档。
# 2. 提供一个默认值。
# Required:
ENV DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{localhost}/{db_name}?charset=utf8'
# Opional:
ENV FLASK_APP="app:create_app()"
ENV FLASK_ENV=production
ENV PORT=5000

VOLUME ["/flask-sampleproject/log"]
EXPOSE 5000
CMD ["python", "run.py"]
