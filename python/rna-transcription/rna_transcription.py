dna2rna = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    output = ''
    try:
        for n in dna_strand:
            output+=dna2rna[n]
        return output
    except KeyError:
        raise ValueError("Not good")
