def create_codon_dict(file_path):
    codonamino_dict = {}
    with open(file_path) as file:
        codonamino_dict = {row.strip().split('\t')[0]: row.strip().split('\t')[2] for row in file.readlines()}
    return codonamino_dict # Replace the pass with your code


