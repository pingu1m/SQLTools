from typing import Optional

from . import docker

# docker build github.com/pingu1m/sqltools-postgres -t sqltools:postgres
# docker run -it --network host -e PGPASSWORD=password sqltools:postgres  pg_dump  -h localhost -U user sampledb > pg-backup.sql


def dump(host: str, user: str, password: str, db: str, port: Optional[str] = '5432'):
    return docker.run_tool('sqltools:postgres', envs=['-e', f'PGPASSWORD={password}'],
                    commands=['pg_dump', '-h', host, '-U', user, '-p', port, db])


def build():
    docker.build(['github.com/pingu1m/sqltools-postgres', '-t','sqltools:postgres'])
