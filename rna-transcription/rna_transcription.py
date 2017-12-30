def to_rna(dna):
    """Return translated DNA strand into it`s RNA complement """
    rna = []
    complements = {'G':'C','C':'G','T':'A','A':'U'}
    for nucleo in dna:
        if nucleo in complements:
            rna.append(complements[nucleo])
        else:
            rna = ''
            break

    return ''.join(rna)
