import pandas as pd

def extract_vectors_from_xlsx(sheet_name='2010_0_20220111.xlsx'):
    # 读取xlsx文件
    df = pd.read_excel(sheet_name)
    
    # 列的索引
    value_column_index = 1  # 第二列的索引（从0开始）
    check_column_index = 4  # 第五列的索引（从0开始）
    
    # 初始化列表，用于存储分组向量
    vectors = []
    
    # 临时向量列表
    temp_vector = []
    
    # 遍历数据框的每一行
    for index, row in df.iterrows():
        # 第二列的数值
        value = row[value_column_index]
        # 第五列的值
        check_value = row[check_column_index]
        
        # 判断第五列是否为空
        if pd.notnull(check_value):
            # 如果第五列不为空，将当前的 temp_vector 加入 vectors 列表
            if temp_vector:
                vectors.append(temp_vector)
            # 清空 temp_vector，并继续下一组
            temp_vector = []
        # 将第二列的数值加入 temp_vector 列表
        temp_vector.append(value)
    
    # 如果最后的 temp_vector 还没有加入 vectors，则添加最后一个分组
    if temp_vector:
        vectors.append(temp_vector)
    
    return vectors

def save_vectors_to_file(vectors, output_file):
    # 打开文件进行写入
    with open(output_file, 'w') as f:
        # 遍历向量列表
        for vector in vectors:
            # 将向量转换为字符串，并使用逗号分隔
            vector_str = ','.join(map(str, vector))
            # 写入文件，每个向量作为一行
            f.write(vector_str + '\n')

# 文件路径和工作表名称
sheet_name = '2010_0_20220111.xlsx'  # 替换为工作表名称
output_file = 'output_vectors_2.txt'  # 输出文件路径

# 从 Excel 文件中提取向量
result_vectors = extract_vectors_from_xlsx(sheet_name)

# 将提取出的向量保存到文件中
save_vectors_to_file(result_vectors, output_file)

print(f"Vectors have been saved to {output_file}.")
