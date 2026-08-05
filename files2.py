
# import json
# data = {
#     "name":    "Alice",
#     "scores":  [88, 92, 95],
#     "active":  True,
#     "address": None
# }

# # Serialize: Python → JSON string
# json_str = json.dumps(data, indent=2)
# print(json_str)

# # Deserialize: JSON string → Python
# loaded = json.loads(json_str)
# print(loaded["name"])   # "Alice"

# Write to file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=2)

# from pathlib import Path
# a="C:\\Users\\Mahesh\\Desktop\\pythonapr\\python-apr-2026\\test\\test1\\test2"
# p=Path(a) / "test3"
# p.mkdir(parents=True, exist_ok=True)

# for f in Path(".").glob("*.json"):
#     print(f.name)

# class Dummy:
#     pass

# print(dir(Dummy))

def read_file_safe(filepath):
    try:
        with open(filepath, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError:
        print(f"No permission to read: {filepath}")
        return None
    except UnicodeDecodeError:
        print("File encoding issue — try encoding='latin-1'")
        return None

print(read_file_safe("output.txt"))