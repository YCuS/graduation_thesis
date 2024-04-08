
import os
import pandas as pd
import re

# 定义一个函数来提取中文内容
def extract_chinese_text(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')  # 匹配中文字符的正则表达式
    result = pattern.findall(text)
    return result

# 指定包含Excel文件的文件夹路径
folder_path = 'F:/diabetes_datasets/Shanghai_T2DM'

# 存储所有提取到的中文词条的列表
chinese_words = []

# 遍历文件夹内的所有Excel文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                # 检查第6列是否有内容
                if not pd.isnull(row[5]):
                    chinese_text = row[5]
                    chinese_words.extend(extract_chinese_text(chinese_text))
        except Exception as e:
            print(f"无法处理文件 {filename}: {str(e)}")

# 去除重复的词条
unique_chinese_words = list(set(chinese_words))
file_name = "result.txt"

# 打开文件以写入模式
with open(file_name, "w") as file:
    # 将列表中的每个元素写入文件
    for item in unique_chinese_words:
        file.write(item + "\n")
# 打印提取的中文词条
# for word in unique_chinese_words:
#     print(word)
