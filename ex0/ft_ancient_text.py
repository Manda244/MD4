#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/09 18:59:38 by marasolo            #+#    #+#            #
#   Updated: 2026/06/15 17:12:38 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    file: typing.IO[str]
    try:
        file = open(file_name)
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    content: str = file.read()
    print("---")
    print()
    print(content)
    if content and not content.endswith("\n"):
        print()
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
