from typing import Optional

from . import docker

# docker build github.com/pingu1m/sqltools-mysql -t sqltools:mysql
# docker run --rm -it --network host sqltools:mysql mysqldump -h'127.0.0.1' -u'user' -p"password" -P'3306' sampledb


def dump(host: str, user: str, password: str, db: str, port: Optional[str] = '3306'):
    return docker.run_tool('sqltools:mysql', commands=['mysqldump', f"-h{host}", f"-u{user}", f"-p{password}", f"-P{port}", db])


def build():
    docker.build(['github.com/pingu1m/sqltools-mysql', '-t','sqltools:mysql'])
