import subprocess
import sys

# docker run -it -e PGPASSWORD=password --network host postgres:12-alpine  pg_dump  -h localhost -U user sampledb > pg-backup.sql
# docker run -it --network host mysql:5.7 /usr/bin/mysqldump -h 127.0.0.1 -u user --password=password sampledb > mysql-backup.sq
pg_docker = ['docker','run', '-it', '-e','PGPASSWORD=password', '--network',
             'host', 'postgres:12-alpine', 'pg_dump' ]
def dump(url):
    try:
        return subprocess.Popen(pg_docker + [url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1]
    db_name = db_name.split("?")[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"

