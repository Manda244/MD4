#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 09:40:16 by marasolo            #+#    #+#            #
#   Updated: 2026/06/16 07:45:07 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def read_file(file_name: str) -> str:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    file: typing.IO[str]
    try:
        file = open(file_name)
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")

    content: str = file.read()
    print("---")
    print()
    print(content)
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")
    return content


def save_file(file_name: str, content: str) -> None:
    file: typing.IO[str]
    try:
        file = open(file_name, "w")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    file.write(content)
    file.close()
    print(f"Data saved to '{file_name}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    content = read_file(sys.argv[1])
    if content is None:
        return

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
    new_file_name: str = input("Enter new file name (or empty): ")
    if new_file_name == "":
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_file_name}'.")
        save_file(new_file_name, new_content)


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(e)
