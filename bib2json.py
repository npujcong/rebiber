import json
import re
import sys
 
def normalize_title(title_str):
    title_str = re.sub(r'[^a-zA-Z]',r'', title_str) 
    return title_str.lower().replace(" ", "").strip()


def load_bib_file(bibpath="acl.bib"):
    all_bib_entries = []
    with open(bibpath) as f:
        bib_entry_buffer = []
        for line in f.readlines():
            # line = line.strip()
            bib_entry_buffer.append(line)
            if line == "}\n":
                all_bib_entries.append(bib_entry_buffer)
                bib_entry_buffer = []
    return all_bib_entries

def buil_json(all_bib_entries):
    all_bib_dict = {}
    for bib_entry in all_bib_entries:
        for entry in bib_entry:
            if entry.strip().lower().startswith("title"):
                target_bp = entry.find('=')+1
                while entry[target_bp] == ' ':
                    target_bp += 1
                title = entry.replace(entry[:target_bp], "").replace('",', "")
                # print(title) 
                bib_key = normalize_title(title)
                all_bib_dict[bib_key] = bib_entry
                break
    return all_bib_dict


if __name__ == "__main__":
    all_bib_entries = load_bib_file(sys.argv[1])
    all_bib_dict = buil_json(all_bib_entries)
    with open(sys.argv[2], "w") as f:
        json.dump(all_bib_dict, f, indent=2)
