#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name_module in dir(hidden_4):
        if "__" not in name_module:
            print(name_module)
