import sys

def read_input_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.strip().split('\t')
            data.append((columns[4], columns[3]))
    return data

def is_connected(gene1, gene2):
    gene_number1 = int(gene1.split('_')[-1][1:])
    gene_number2 = int(gene2.split('_')[-1][1:])
    distance = abs(gene_number1 - gene_number2)
#    print(f"Checking distance between {gene1} and {gene2}: {distance}")
    return distance <= 5

def get_subject_gene(query_gene, data):
    for subject_gene, q_gene in data:
        if q_gene == query_gene:
            return subject_gene
    return None


def count_core_components_in_column(column_data):
    core_components = [
        '05_TssA', '17_TssB', '16_TssC', '15_TssD', '14_TssE',
        '13_TssF', '12_TssG', '06_TssH', '04_TssK', '03_TssL', '10_TssM'
    ]
    present_core_components = [component for component in core_components if any(component in gene for gene in column_data)]
    core_count = len(present_core_components)
    return core_count

def main():
    if len(sys.argv) != 2:
#        print("Usage: python script_name.py input_file_path")
        return

    input_file_path = sys.argv[1]
    data = read_input_file(input_file_path)

#    print("Data:", data)
#    print("Query Genes:", [item[0] for item in data])

    fourth_column_data = [item[0] for item in data]  
    core_count = count_core_components_in_column(fourth_column_data)

    print(f"Number of core components: {core_count}")



    filtered_data = []
    for subject_gene, query_gene in data:
        gene_number_parts = query_gene.split('_')[2]
        if len(gene_number_parts) > 1:
            gene_number_part = gene_number_parts[1]
            if gene_number_part.isdigit():
                gene_number = int(gene_number_part)
                if 1 <= gene_number <= 18:
                    filtered_data.append(query_gene)
#                    print(f"Adding {query_gene} to filtered data")

    filtered_data.sort(key=lambda gene: int(gene.split('_')[-1][1:]))

    loci = []
    current_locus = []
    
    for gene in filtered_data:
        if not current_locus:
            current_locus.append(gene)
#            print(f"Starting new locus with gene {gene}")
        else:
            last_gene = current_locus[-1]
            if is_connected(last_gene, gene):
                current_locus.append(gene)
#                print(f"Adding {gene} to current locus")
            else:
#                print(f"Gene {last_gene} is not connected to {gene}, ending current locus")
                if len(current_locus) >= 3:
                    loci.append(current_locus)
#                    print(f"Adding locus: {', '.join(current_locus)}")
                current_locus = []
#                print("Locus disconnected, resetting current locus")
    
    if len(current_locus) >= 3:
        loci.append(current_locus)
#        print(f"Adding locus: {', '.join(current_locus)}")

    print("Number of T6SS loci:", len(loci))

    for i, locus in enumerate(loci, start=1):
        subject_genes = []
        for query_gene in locus:
            subject_gene = get_subject_gene(query_gene, data)
            if subject_gene:
                subject_genes.append(subject_gene)
        
        if subject_genes:
            subject_genes_str = ", ".join(subject_genes)
            print(f"Locus {i}: {subject_genes_str}")



        else:
            print(f"Locus {i}: No subject genes found")



if __name__ == "__main__":
    main()
