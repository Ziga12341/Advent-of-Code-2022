from collections import defaultdict

with open("input.txt", "r", encoding="utf-8") as file:
    file_system = []
    # root_folder = "$ cd /"
    current_path = ["/"]
    changed_file = [line[:-1] for line in file if line != "$ ls\n" and line != "$ cd /\n"]
    first_folder = []
    for line_in_changed_file in changed_file:
        if line_in_changed_file[0].isdigit():
            line_in_changed_file = line_in_changed_file.split(" ")[0]
            first_folder.append(line_in_changed_file)
        elif not line_in_changed_file.startswith("$"):
            path = "/".join(current_path)
            first_folder.append("dir " + path + "/" + line_in_changed_file[4:])

        if line_in_changed_file.startswith("$ cd ") and len(first_folder) > 0:
            changed_file = changed_file[len(first_folder) + 1:]
            print(changed_file)
            new_dir = ("/".join(current_path), first_folder)
            file_system.append(new_dir)
            print("-----------------", new_dir)
            first_folder = []

        if line_in_changed_file.startswith("$ cd .."):
            current_path.pop()  # cd out of the directory
        # elif not line_in_changed_file == root_folder and line_in_changed_file.startswith("$ cd "):
        elif line_in_changed_file.startswith("$ cd "):
            current_path.append(line_in_changed_file[5:])   # cd into the subdir

    file_system.append(("/".join(current_path), first_folder))

    print("main is:", file_system)

    all_file_system = []
    for folder in file_system:
        root, files = folder
        files_with_ints = []

        for file_in_folder in files:
            if file_in_folder[0].isdigit():
                files_with_ints.append(int(file_in_folder))
            elif file_in_folder.startswith("dir"):
                file_in_folder = file_in_folder[4:]
                files_with_ints.append(file_in_folder)
            else:
                files_with_ints.append(file_in_folder)

        files_with_ints_and_root = root, files_with_ints
        all_file_system.append(files_with_ints_and_root)


print(all_file_system)

to_dict = defaultdict(dict)
inside_dict = defaultdict(dict)
file_system_in_dict = defaultdict(list)
for root, files in all_file_system:
    print((root, files))
    for file in files:
        to_dict[root][file] = {}

dir_sizes = defaultdict(int)


def fix_tree_structure(current_dir, dict_subdir):
    """
    Fixes the directory structure recursively.

    :param current_dir: name fo the directory that is being processed
    :param dict_subdir: the directory being processed
    :return: size of the current processed sub-directory
    """
    if not dict_subdir:
        return 0

    # 841510
    # {'/': {'fcqv': {}, 'fcv': {}, 72939: {}, 236918: {}, 'jvwfwrg': {}, 'tzwpllhq': {}, 'vglf': {}, 28586: {}}, 'fcqv': {'fhg': {}, 277152: {}, 269351: {}, 'thbb': {}}, 'fhg': {'jljrdvw': {}}, 'jljrdvw': {101940: {}}, 'thbb': {144311: {}, 178246: {}, 48521: {}, 284713: {}, 96717: {}}, 'fcv': {'ffhwwg': {}, 275505: {}, 179689: {}, 69265: {}, 38365: {}, 'vcqsrw': {}, 247592: {}, 'znzpm': {}}, 'ffhwwg': {'hlqf': {}, 179995: {}, 176263: {}, 242533: {}, 21991: {}, 117790: {}, 186465: {}, 236863: {}, 117473: {}, 218749: {}, 'dsqwrdnq': {}, 261158: {}, 51165: {}, 240618: {}, 'ffhwwg': {}, 201345: {}, 128709: {}, 284209: {}, 'qldfrhm': {}, '$ cd ffhwwg': {}, 13278: {}, 165094: {}, 'wjj': {}, 145399: {}, 'hlw': {}, 258985: {}}, 'hlqf': {30443: {}}, 'vcqsrw': {'bzlnsjmv': {}, 'rvbtnz': {}, 224487: {}, 255340: {}}, 'bzlnsjmv': {272548: {}}, 'rvbtnz': {165670: {}}, 'znzpm': {'mjwnsw': {}}, 'mjwnsw': {219638: {}}, 'jvwfwrg': {'ffhwwg': {}, 42104: {}, 'hzjpg': {}, 'jwl': {}, 'nmz': {}, 243217: {}, 'tdjtv': {}, 'wdn': {}, 35406: {}, 'mctsws': {}, 69374: {}, 130055: {}, 212356: {}, 176717: {}, 141078: {}, 'jgvf': {}, 170488: {}}, 'hzjpg': {241535: {}, 'ddrwfq': {}, 'mqwww': {}, 29329: {}, 91380: {}, 'wctwz': {}, 210633: {}, 'wlrmbtdg': {}, 172051: {}}, 'ddrwfq': {11756: {}}, 'mqwww': {149750: {}}, 'wctwz': {277720: {}}, 'wlrmbtdg': {14154: {}, 'hgdjv': {}, 'qldfrhm': {}, 48920: {}, 101228: {}, 159676: {}}, 'hgdjv': {'hlw': {}}, 'hlw': {229687: {}, 244567: {}, 15123: {}, 'chgwjl': {}, 'dsz': {}, 165192: {}, 40771: {}, 46495: {}, 122203: {}, 175167: {}, 'ttr': {}, 70960: {}, 139875: {}}, 'qldfrhm': {254189: {}, 14471: {}, 163165: {}, 10880: {}, '$ cd qldfrhm': {}, 'ffhwwg': {}, 'jwl': {}, 15164: {}, 188544: {}, 255566: {}, 'tbngqwb': {}, 59898: {}, 'bwcg': {}, 104797: {}, 273814: {}, 182685: {}, 190595: {}, 'stpvb': {}, 105499: {}, 'zldj': {}, 221567: {}, 'rsztzjcm': {}, 33248: {}, 114731: {}, 276521: {}, 260238: {}, 270180: {}, 'czwwzj': {}, 50884: {}, 'mjpzgbww': {}, 252028: {}, 'rzqj': {}}, 'jwl': {277778: {}, 'ghgf': {}, 'gqlmq': {}, 163875: {}, 'mjm': {}, 'qgq': {}, 179926: {}, 'zjv': {}, 105997: {}, 161061: {}, 40245: {}, 268818: {}, 161866: {}, 'nsvjcpc': {}, 'nwdvblg': {}, 171528: {}, 'qqmb': {}, 282266: {}, 45969: {}, 'bzq': {}, 215828: {}, 'jjmndb': {}, 'pjzqjbd': {}, 'pmslv': {}, 'smfg': {}, 'wmjjwh': {}, 130858: {}, 112258: {}, 62087: {}}, 'ghgf': {181540: {}}, 'gqlmq': {'ffhwwg': {}, 283989: {}, 'jwl': {}, 'pqdqntr': {}, 62581: {}}, 'zjv': {102693: {}}, 'pqdqntr': {159376: {}}, 'mjm': {273410: {}, 8169: {}, 87728: {}, 221237: {}}, 'qgq': {'dgq': {}, 'hlw': {}, 164971: {}, 'jwl': {}, 158534: {}, 251561: {}, 282035: {}}, 'dgq': {'ffhwwg': {}, 237291: {}, 70142: {}, 55607: {}}, 'nmz': {51802: {}, 128617: {}}, 'tdjtv': {'jvwfwrg': {}, 'mdmwf': {}, 'rlpbrq': {}}, 'mdmwf': {'ffhwwg': {}, 15609: {}, 205721: {}}, 'rlpbrq': {120058: {}, 194704: {}, 256467: {}}, 'wdn': {170094: {}, 'gqmghw': {}, 150252: {}, 243953: {}, 123382: {}, 96220: {}, 'ztqbhjr': {}}, 'gqmghw': {'tlgbcrh': {}}, 'tlgbcrh': {281457: {}}, 'ztqbhjr': {271212: {}, 'nbhq': {}, 'vfmmj': {}, 260079: {}}, 'nbhq': {179096: {}, 150184: {}}, 'vfmmj': {57445: {}, 40329: {}}, 'tzwpllhq': {33596: {}, 16963: {}, 161107: {}, 'jwv': {}, 152431: {}, 'qldfrhm': {}, 'swmwvl': {}, 'wzpth': {}}, 'jwv': {'bgswd': {}, 188795: {}, 'jvwfwrg': {}, 'jwl': {}, 'mbcb': {}, 'qldfrhm': {}, 30173: {}, 193577: {}}, 'bgswd': {'hdgt': {}, 216966: {}}, 'hdgt': {70441: {}}, 'mctsws': {257337: {}}, 'mbcb': {'fbhhq': {}, 'rgjwh': {}}, 'fbhhq': {'vnn': {}}, 'vnn': {55629: {}}, 'rgjwh': {7826: {}}, 'nsvjcpc': {43660: {}}, 'nwdvblg': {'cltj': {}, 'fds': {}}, 'cltj': {86970: {}, 111805: {}, 247438: {}}, 'fds': {49560: {}, 234970: {}, 133376: {}}, 'qqmb': {139542: {}}, 'tbngqwb': {'jwl': {}, 273706: {}, 76731: {}}, 'swmwvl': {32187: {}, 'gsj': {}, 83763: {}, 93113: {}}, 'gsj': {'fpzj': {}, 152202: {}}, 'fpzj': {83665: {}}, 'wzpth': {'snhss': {}}, 'snhss': {'hlw': {}}, 'vglf': {'gdjmt': {}, 'hnnw': {}, 'htqzfcc': {}, 'nqf': {}, 269558: {}, 116732: {}, 'tvmqzwmn': {}, 72822: {}}, 'gdjmt': {214742: {}}, 'hnnw': {'ffhwwg': {}, 217384: {}, 153385: {}, 'jwl': {}, 'shdt': {}, 143935: {}, 90319: {}, 101043: {}}, 'dsqwrdnq': {129823: {}}, 'bzq': {199534: {}}, 'jjmndb': {'cbfdqtc': {}, 'gnjlnz': {}, 'hlw': {}, 201443: {}, 'lzlwstch': {}, 175514: {}, 'qldfrhm': {}, 144450: {}, 'ssh': {}, 'tbdhtqn': {}, 150014: {}, 240619: {}}, 'cbfdqtc': {39125: {}, 264178: {}, 180897: {}}, 'gnjlnz': {217994: {}}, 'chgwjl': {284909: {}}, 'dsz': {47411: {}}, 'ttr': {'fgbgl': {}, 'qsflswrq': {}, 5609: {}, 250311: {}}, 'fgbgl': {203288: {}}, 'qsflswrq': {222611: {}, 143339: {}}, 'lzlwstch': {'ffhwwg': {}, 'hwmzp': {}, 'jvwfwrg': {}, 'ndpbn': {}, 'qllzhd': {}}, 'hwmzp': {54571: {}}, 'ndpbn': {160215: {}}, 'qllzhd': {41306: {}, 162845: {}}, 'bwcg': {181254: {}}, 'stpvb': {221672: {}}, 'zldj': {'jwl': {}}, 'ssh': {65814: {}, 'jvwfwrg': {}, 70744: {}}, 'tbdhtqn': {37228: {}, 69069: {}, 'rmrwm': {}, 166294: {}}, 'rmrwm': {118846: {}}, 'pjzqjbd': {259092: {}, 89322: {}}, 'pmslv': {82637: {}}, 'smfg': {'gfbpcr': {}, 'sghtlzqv': {}}, 'gfbpcr': {23958: {}}, 'sghtlzqv': {275943: {}, 149592: {}, 285215: {}, 179076: {}}, 'wmjjwh': {198333: {}, 59553: {}, 91883: {}, 7054: {}}, 'shdt': {27781: {}, 255994: {}, 'mrgppm': {}, 'mwvgmjmb': {}, 'nsbrbcq': {}, 263384: {}, 251640: {}, 16959: {}}, 'mrgppm': {'ghzhzzp': {}, 'jwl': {}, 'tgpm': {}}, 'ghzhzzp': {'bqplqq': {}, 'vtqgwsj': {}}, 'bqplqq': {234131: {}}, 'vtqgwsj': {260109: {}}, 'tgpm': {'hlw': {}, 167788: {}}, 'mwvgmjmb': {142087: {}}, 'nsbrbcq': {'hljjp': {}}, 'hljjp': {125853: {}}, 'htqzfcc': {'cqs': {}, 'dsnpcnv': {}, 'ffhwwg': {}, 90664: {}, 92316: {}, 'mftm': {}, 'mmgn': {}, 'qqvzvw': {}, 166400: {}, 'vtf': {}, 'wrbwbdt': {}}, 'cqs': {232548: {}, 35933: {}}, 'dsnpcnv': {115805: {}}, 'rsztzjcm': {268313: {}, 283644: {}, 'jhdcdm': {}, 84130: {}, 31286: {}}, 'jhdcdm': {212461: {}}, 'wjj': {89758: {}, 163105: {}}, 'mftm': {278389: {}}, 'mmgn': {28122: {}}, 'qqvzvw': {'mjw': {}, 'qldfrhm': {}, 'zbmpdwtc': {}}, 'mjw': {'cvn': {}, 'dlgzc': {}, 10631: {}, 206351: {}, 136824: {}, 116870: {}}, 'cvn': {146142: {}}, 'dlgzc': {130120: {}}, 'czwwzj': {'cpwwqrph': {}, 19863: {}, 'snl': {}, 83915: {}}, 'cpwwqrph': {'jvwfwrg': {}}, 'snl': {'btngcvt': {}, 'ffhwwg': {}, 53428: {}, 220232: {}}, 'btngcvt': {172859: {}, 'tgcqmbrn': {}}, 'tgcqmbrn': {149905: {}}, 'mjpzgbww': {52355: {}, 5856: {}, 146211: {}}, 'rzqj': {'jmjszd': {}, 134481: {}, 187382: {}}, 'jmjszd': {81971: {}}, 'zbmpdwtc': {193744: {}, 231403: {}}, 'vtf': {2562: {}}, 'wrbwbdt': {'brzwbmc': {}, 29261: {}}, 'brzwbmc': {'ggh': {}, 174287: {}, 'jwl': {}, 247329: {}, 'thm': {}, 83546: {}, 231269: {}}, 'ggh': {'cqrmsltg': {}, 18724: {}}, 'cqrmsltg': {'ffhwwg': {}, 'jvwfwrg': {}, 41263: {}, 'tcjr': {}}, 'tcjr': {'hnngpdc': {}, 153685: {}, 93502: {}, 226658: {}}, 'hnngpdc': {243203: {}}, 'thm': {228008: {}, 167850: {}, 'jvwfwrg': {}}, 'jgvf': {150671: {}}, 'nqf': {'rglrpqd': {}}, 'rglrpqd': {276785: {}, 224128: {}}, 'tvmqzwmn': {47655: {}, 233646: {}, 237245: {}, 185131: {}}}
    for k, v in dict_subdir.items():
        # if it is a directory
        if type(k) is str:
            directory = to_dict[k]
            dict_subdir[k] = directory
            to_dict[k] = None
            dir_sizes[current_dir] += fix_tree_structure(k, directory)
        else:
            dir_sizes[current_dir] += k

    return dir_sizes[current_dir]


to_dict = dict(to_dict.items())
print(to_dict)
for k, v in to_dict.items():
    fix_tree_structure("/", v)
print(to_dict)
print(dir_sizes)

sum_all = 0
for k, v in dir_sizes.items():
    if v <= 100_000:
        sum_all += v
print(sum_all)

disk_space = 70_000_000
patch_space = 30_000_000
used_space = dir_sizes["/"]
print(used_space)
unused_space = disk_space - used_space
print(unused_space)
we_need_at_least = patch_space - unused_space
print(we_need_at_least)

all_dir_size = []
for k, v in dir_sizes.items():
    if v >= we_need_at_least:
        all_dir_size.append(v)

print(sorted(all_dir_size)[0])