import argparse, time


known_drivers = ['local','s3']


class DriverAction(argparse.Action):
    # def __init__(self, option_strings, dest, nargs=None, **kwargs):
    #     if nargs is not None:
    #         raise ValueError("nargs not allowed")
    #     super(DriverAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(f"{namespace} - {values} - {option_string}")
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local', 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination
        # setattr(namespace, self.dest, values)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="URL of the database to backup")
    parser.add_argument('--type', '-t',help="URL of the database to backup",
                        required=True)
    parser.add_argument('--driver', '-d',
                        help="URL of the database to backup",
                        nargs=2,
                        metavar=('DRIVER','DESTINATION'),
                        action=DriverAction,
                        required=True)
    return parser


def main():
    import boto3
    from sqltools import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)

    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing db up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing db locally to {args.destination}")
        storage.local(dump.stdout, outfile)

