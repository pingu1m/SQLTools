import subprocess
import sys
from typing import List, Optional


def run_tool(image: str, commands: List[str], envs: Optional[List[str]] = None):
    try:
        exec = get_run_string(commands, image, envs)
        print(f"Running: {' '.join(exec)}")
        output = subprocess.Popen(exec, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(f"1 {output.stdout}, 2 {output.stderr}")
        return output

    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def build(build_list: List[str]):
    try:
        print(f"Running: docker build "+ " ".join(build_list))
        return subprocess.run(['docker','build'] + build_list, stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

# docker run --rm -it --network host --entrypoint "" -v `pwd`:/backup schnitzler/mysqldump mysqldump --opt -h 127.0.0.1 -u user -p"password" "--result-file=/backup/dumps.sql" sampledb


def get_run_string(commands: List[str], image: str, envs: Optional[List[str]] = None):
    if envs:
        return ['docker', 'run', '--rm', '-it', '--network', 'host'] + envs + [image] + commands
    else:
        return ['docker', 'run', '--rm', '-it', '--network', 'host', image] + commands


