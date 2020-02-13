

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def s3(client, infile, bucket, filename):
    client.upload_fileobj(infile, bucket, filename)

def dump_file_name(db_name, timestamp=None):
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"

