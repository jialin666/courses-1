import pandas as pd
df_xlsx = pd.read_excel(r'E:\competitions\Statistical modeling\data\first\xi.xlsx')
unique_row_sets_xlsx = df_xlsx.apply(lambda x: set(x.dropna().unique()), axis=1)

n_rows = len(unique_row_sets_xlsx)
similarity_matrix = pd.DataFrame(index=range(n_rows), columns=range(n_rows))

for i in range(n_rows):
    for j in range(n_rows):
        if i != j:
            common_elements = len(unique_row_sets_xlsx[i].intersection(unique_row_sets_xlsx[j]))
            total_elements = len(unique_row_sets_xlsx[i].union(unique_row_sets_xlsx[j]))
            similarity = common_elements / （total_elements / 2） if total_elements > 0 else 0
            similarity_matrix.at[i, j] = similarity
        else:
            similarity_matrix.at[i, j] = 1

similarity_matrix.to_excel('E:\\competitions\\Statistical modeling\\data\\first\\similarity_matrix.xlsx', index=False)