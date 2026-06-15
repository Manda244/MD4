#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 11:43:22 by marasolo            #+#    #+#            #
#   Updated: 2026/06/15 19:22:50 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def read_file(file_name: str) -> str:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    file: typing.IO[str]
    try:
        file = open(file_name)
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}")
        sys.stderr.flush()
        return

    content: str = file.read()
    print("---")
    print()
    print(content)
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")
    return content


def save_file(file_name: str, content: str) -> str:
    file: typing.IO[str]
    try:
        file = open(file_name, "w")
    except OSError as e:
        sys.stderr.write(f"Error opening file '{file_name}': {e}")
        sys.stderr.flush()
        return
    file.write(content)
    file.close()
    print(f"Data saved to '{file_name}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    content = read_file(sys.argv[1])
    lines: list[str] = content.splitlines()
    new_content: str = ""
    for line in lines:
        new_content += line + "#" + "\n"
    print()
    print("Transform data:")
    print("---")
    print()
    print(new_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_name: str = sys.stdin.readline().rstrip("\n")

    if new_file_name == "":
        print("No file name provided.")
        return
    else:
        print(f"Saving data to '{new_file_name}'.")
        save_file(new_file_name, new_content)


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(e)
