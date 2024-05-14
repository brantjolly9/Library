"""
Function to clean names from a variety of formats:
First Last
First M. Last / First Middle Last
F. M. Last
First Last, Jr.
First Last & First Last

Format to finish:
First Middle 'de Last' , 'van Last' etc

Will output a list of dictionaries:
[
    {
    first
    middle
    last
    suffix
    }
]

"""
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
    name = author_name.lower().replace(",", "")
    authors = []
    author_dicts = []
    
    # Seperate multiple authors then put into list for rest of funct
    if("&" in name):
        authors = name.split(" & ")
    else:
        authors.append(name)

    for author in authors:
        author_dict = {
            "first": None,
            "middle": None,
            "last": None,
            "suffix": None
        }
        # Fix for the few instances of First Middle 'de Last'
        # if " de " in author:
        #     print(author)

        names = author.split(" ")
        if names[-1].endswith('.') or "jr" in names[-1]:
            author_dict["suffix"] = names.pop(-1)

        #! Maybe a better way
        match len(names):
            case 1:
                author_dict["last"] = names[0]
            case 2:
                author_dict["first"] = names[0]
                author_dict["last"] = names[1]
            case 3:
                author_dict["first"] = names[0]
                author_dict["middle"] = names[1]  
                author_dict["last"] = names[2]
        author_dicts.append(author_dict)

    # Return List of Author dicts
    return author_dicts

clean_names = []
for sample in sample_list:
    clean_names.append(clean_name(sample))

pprint(clean_names, indent=4, sort_dicts=False)
