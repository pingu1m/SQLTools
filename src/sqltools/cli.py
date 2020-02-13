import argparse, time
import os
import sys

known_drivers = ['local', 's3']


class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local', 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--type', '-T', help="Type of database to backup Options are: mysql, postgres", required=True)
    parser.add_argument('--host', '-H', help="Hostname of the database", required=True)
    parser.add_argument('--user', '-U', help="User of the database", required=True)
    parser.add_argument('--password', '-p', help="Password of the database")
    parser.add_argument('--port', '-P', help="Port of the database, if not provided will use default ports")
    parser.add_argument('--db', help="Name of the database to backup", required=True)
    parser.add_argument('--driver', '-d', help="URL of the database to backup",
                        nargs=2,
                        metavar=('DRIVER', 'DESTINATION'),
                        action=DriverAction,
                        required=True)
    return parser


def main():
    import boto3
    from sqltools import postgres, mysql, storage

    args = create_parser().parse_args()

    if args.password:
        password = args.password
    else:
        password = os.environ['SQL_USER_PASSWORD']

    if args.type == 'mysql':
        print("Building sqltools:mysql image")
        mysql.build()
        print("Running mysqldump on the docker image")
        dump = mysql.dump(args.host, args.user, password, args.db, args.port)
    elif args.type == 'postgres':
        print("Building sqltools:postgres image")
        postgres.build()
        print("Running pg_dump on the docker image")
        dump = postgres.dump(args.host, args.user, password, args.db, args.port)
    else:
        print(f"Please enter a valid database type, provide type was {args.type}")
        print("Valid types are 'mysql', 'postgres'")
        sys.exit(1)

    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        file_name = storage.dump_file_name(args.db, timestamp)
        print(f"Backing db up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing db locally to {args.destination}")
        storage.local(dump.stdout, outfile)
