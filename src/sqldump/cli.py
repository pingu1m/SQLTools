import argparse


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
    parser.add_argument('--type', help="URL of the database to backup",
                        required=True)
    parser.add_argument('--driver',
                        help="URL of the database to backup",
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser
