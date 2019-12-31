import argparse
import csv
import os
from typing import Tuple, Optional

import git


def clone_repo(url: str, path: str) -> Tuple[bool, str]:
    try:
        git.Git().clone(url, path)
        return (True, f'Cloning "{url}" succeeded')
    except git.GitCommandError as e:
        return (False, str(e))


def batch_clone(urls_and_paths: Tuple[str, str], error_output_filename: str):
    errors = list()
    for url, path in urls_and_paths:
        status, message = clone_repo(url, path)
        print(message, "\n")

        if not status:
            errors.append((url, path, message))

    if errors:
        with open(error_output_filename, "w") as error_output_file:
            HEADER = ("Url", "Path", "Error Message")

            csv_writer = csv.writer(error_output_file)
            csv_writer.writerow(HEADER)
            csv_writer.writerows(errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input csv file")
    parser.add_argument(
        "-u", "--url-column", default="url", help="Url column name(default: url)"
    )
    parser.add_argument(
        "-p", "--path-column", default="path", help="Path column name (default: path)"
    )
    parser.add_argument("-o", "--output-dir", help="Directory to clone to")
    parser.add_argument(
        "-e",
        "--error-output",
        default="error_log.csv",
        help="Error log file name (default: error_log.csv)",
    )
    args = parser.parse_args()

    urls_and_paths = list()
    with open(args.input_file) as input_file:
        rows = csv.DictReader(input_file)
        url_column_name = args.url_column
        path_column_name = args.path_column
        output_dir = args.output_dir
        for row in rows:
            url = row[url_column_name]
            if not output_dir:
                path = row[path_column_name]
            else:
                path = os.path.join(output_dir, row[path_column_name])
            urls_and_paths.append((url, path))

    batch_clone(urls_and_paths, args.error_output)
