#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    module_names = dir(hidden_4)
    filtered_names = sorted(name for name in module_names
                            if not name.startswith("__"))
    for name in filtered_names:
        print(name)
