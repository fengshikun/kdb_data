import os
from Bio.PDB import PDBParser, Chain, Model, Structure, is_aa
import warnings
from Bio.PDB.PDBExceptions import PDBConstructionWarning


warnings.filterwarnings(
    action='ignore',
    category=PDBConstructionWarning)

parser = PDBParser()


def check_ligname(dir):
    pdb_list = []
    pdb_with_ligname_list = []

    for f in os.listdir(dir):
        if f.endswith(".pdb"):
            pdb_list.append(f)
            model = parser.get_structure("0", os.path.join(".", f))[0]
            ligname = f.split("_", 1)[1].split(".", 1)[0]
            for chain in model:
                for res in chain:
                    res.detach_parent()
                    if not(is_aa(res, standard=True)):
                        if res.resname == ligname.upper():
                            print(f"{ligname} is in {f}!")
                            pdb_with_ligname_list.append(f)

    for i in pdb_list:
        if i not in pdb_with_ligname_list:
            print(f"{i} do NOT have correct ligname!")


if __name__ == '__main__':
    check_ligname(os.path.join("."))

