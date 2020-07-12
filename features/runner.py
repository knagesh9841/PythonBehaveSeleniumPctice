import pathlib
from datetime import datetime
import subprocess
import argparse
import os


def get_unique_run_id():
    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    elif os.environ.get("CUSTOM_BUILD_NUMBER"):
        unique_run_id = os.environ.get("CUSTOM_BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime("%d_%B_%Y_%H_%M_%S")

    os.environ['UNIQUE_RUN_ID'] = unique_run_id

    return unique_run_id


def create_output_directory(prefix='results_'):
    global run_id
    curr_file_path = pathlib.Path(__file__).parent.absolute()
    dir_to_create = os.path.join(curr_file_path, prefix + run_id)
    os.mkdir(dir_to_create)
    print(f"Output Directory Created {dir_to_create}")
    return dir_to_create


if __name__ == '__main__':
    run_id = get_unique_run_id()
    print("Unique ID = "+run_id)
    output_dir = create_output_directory()
    json_out_dir = os.path.join(output_dir, "json_report_out.json")

    parser = argparse.ArgumentParser()
    parser.add_argument('--behave_options', type=str, required=False, help="String of behave Options")
    args = parser.parse_args()
    options = args.behave_options
    command = f'behave {options} -f json.pretty -o "{json_out_dir}"'
    print(f"Executing Command {command}")
    rs = subprocess.run(command, shell=True)


