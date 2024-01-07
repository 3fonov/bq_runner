"""Console script for bq_runner."""

import fire


def help() -> None:
    print("bq_runner")
    print("=" * len("bq_runner"))
    print("Run BigQuery sql in command line intelligently")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
