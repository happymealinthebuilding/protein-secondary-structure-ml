from Bio.PDB import PDBList

pdb_ids = [
    "1CRN",
    "1A8M",
    "2PTC",
    "1BTA",
    "4HHB"
]

pdbl = PDBList()

for pdb in pdb_ids:
    pdbl.retrieve_pdb_file(pdb, pdir="../data/raw", file_format="pdb")

print("Downloaded PDB files")