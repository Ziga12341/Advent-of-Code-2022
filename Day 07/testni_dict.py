from collections import defaultdict

tree = defaultdict(list)
#to_dict = [("a", [1, "d", "s", 4, "c"]), ("b", [2, 6, "q"]), ("c", [3, "i"]), ("i", [3, 2, 1])]
#to_dict = { "a": ("a", [1, "d", "s", 4, "c"]), "b": ("b", [2, 6, "q"]), "c": ("c", [3, "i"]) }
to_dict = {"a": {1: {}, "d": {}, 4: {}, "c": {}}, "b": {2: {}, 6: {}, "q": {}}, "c": {3: {}, "i": {}}, "d": {8: {}, 9: {}}, "i": {12: {}}, "q": {55: {}}}

# recursive function

def fix_tree_structure(dict_subdir, root):
    if not dict_subdir:
        return
    for key, value in dict_subdir.items():
        # if it is a directory
        if type(key) is str:
            directory = to_dict[key]
            dict_subdir[key] = directory
            to_dict[key] = None
            fix_tree_structure(directory, root)


for k, v in to_dict.items():
    fix_tree_structure(v, to_dict)

print(to_dict)

