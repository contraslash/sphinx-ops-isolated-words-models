#!/usr/bin/env python

import os

import generate_dict
import generate_phone_set_from_dict
import generate_filler
import generate_transcriptions

ETC_FOLDER_NAME = "etc"
PROJECT_NAME = "ops_aphasia"
TRANSCRIPT_FILE = "transcription.txt"


def execute_script_with_args_if_file_does_not_exists(script, file, *args):
    # print(script)
    # print(file)
    # print(args)
    if not os.path.exists(file):
        print("Creating {}".format(file))
        script(*args)
    else:
        print("{} already exists".format(file))


if __name__ == "__main__":

    # Configuration Folder
    if not os.path.exists(ETC_FOLDER_NAME):
        print("Creating etc folder")
        os.makedirs(ETC_FOLDER_NAME)
        print("etc folder created")

    # Dictionary file
    dict_file = os.path.join(ETC_FOLDER_NAME, "{}.dic".format(PROJECT_NAME))
    execute_script_with_args_if_file_does_not_exists(
        generate_dict.execute_script,
        dict_file,
        TRANSCRIPT_FILE,
        dict_file
    )
    # Phone file
    phone_file = os.path.join(ETC_FOLDER_NAME, "{}.phone".format(PROJECT_NAME))
    execute_script_with_args_if_file_does_not_exists(
        generate_phone_set_from_dict.execute_script,
        phone_file,
        dict_file,
        phone_file
    )

    filler_file = os.path.join(ETC_FOLDER_NAME, "{}.filler".format(PROJECT_NAME))
    execute_script_with_args_if_file_does_not_exists(
        generate_filler.execute_script,
        filler_file,
        filler_file,
    )

    fileids_file = os.path.join(ETC_FOLDER_NAME, "{}.fileids".format(PROJECT_NAME))
    execute_script_with_args_if_file_does_not_exists(
        generate_transcriptions.execute_script,
        fileids_file,
        ETC_FOLDER_NAME,
        PROJECT_NAME,
        TRANSCRIPT_FILE
    )
