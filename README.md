# Git Batch Cloner

Git clone repos in a batch

## Prerequisite
* Python 3.6
* [pipenv](http://pipenv.org)

### Install Dependency

```sh
pipenv install
```

## Usage

```sh
pipenv run python cloner.py [-h] [-u URL_COLUMN] [-p PATH_COLUMN] [-o OUTPUT_DIR]
                            [-e ERROR_OUTPUT]
                            input_file

```

* positional arguments:
    * `input_file`
        * Input csv file

* optional arguments:
    * `-h`, `--help`
        * show this help message and exit
    * `-u URL_COLUMN`, `--url-column URL_COLUMN`
        * Url column name(default: url)
    * `-p PATH_COLUMN`, `--path-column PATH_COLUMN`
        * Path column name (default: path)
    * `-o OUTPUT_DIR`, `--output-dir OUTPUT_DIR`
        * Directory to clone to
    * `-e ERROR_OUTPUT`, `--error-output ERROR_OUTPUT`
        * Error log file name (default: error_log.csv)

## AUTHORS
[Lee-W](https://github.com/Lee-W/)
