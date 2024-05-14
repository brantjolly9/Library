from pprint import pprint

sample_list = [
    "Thomas C. Foster, Jr. & Paul Delany",
    "Ronald T. Takaki",
    "Mark Anthony Neal",
    "Emile Delavenay",
    "Misc",
    "T. S. Elliot",
    "Hector St. John de Crevecoeur"
]
def clean_name(author_name = str()):
    name = author_name.lower()
    authors = []
    author_dicts = []
    
    # Remove "MISC" Authors first
    if(author_name == "misc"):
        return "misc"
    
    # Seperate multiple authors then put into list for rest of funct
    if("&" in author_name):
        authors = author_name.split("&")
    else:
        authors.append(name)

    for author in authors:
        author_dict = {
            "first": None,
            "middle": None,
            "last": None,
            "suffix": None
        }
        if " de " in author:
            print("ahhhh")
            print(author)
        names = author.split(" ")
        if names[-1].endswith('.') or "jr" in names[-1]:
            author_dict["suffix"] = names.pop[-1]

        match len(names):
            case 1:
                author_dict["last"] = names[0]
            case 2:
                author_dict["first"] == names[0]
                author_dict["last"] == names[-1]
            case 3:
                author_dict["first"] = names[0]
                author_dict["middle"] = names[1]  
                author_dict["last"] = names[2]
        author_dicts.append(author_dict)
    return author_dicts

for sample in sample_list:
    author_dicts = clean_name(sample)
    pprint(author_dicts, indent=4)
