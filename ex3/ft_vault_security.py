#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 21:49:17 by marasolo            #+#    #+#            #
#   Updated: 2026/06/16 07:43:55 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def secure_archive(file_name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name) as file:
                return True, file.read()
        except OSError as e:
            return False, str(e)
    else:
        try:
            with open(file_name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        except OSError as e:
            return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", result[1]))


if __name__ == "__main__":
    main()
