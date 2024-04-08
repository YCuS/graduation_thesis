import pandas as pd
import os


# 定义处理函数
def process_excel_file(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 获取文件名（不包括后缀）
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # 创建一个新的DataFrame来存储处理后的数据
    new_rows = []

    for index, row in df.iterrows():
        # 检查第6列是否有内容
        if not pd.isnull(row[5]):
            # 获取第1列内容
            col1_value = row[0]
            col3_value = 0
            col4_value = 0
            col5_value = 0
            col6_value = 0
            col7_value = 0
            # 从第6列内容中提取数字
            text = str(row[5])
            start = text.find("米饭")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.3
                col4_value = col4_value + rice_weight * 25.9
                col5_value = col5_value + rice_weight * 2.6
                col6_value = col6_value + rice_weight * 0.3
                col7_value = col7_value + rice_weight * 116
            text = str(row[5])
            start = text.find("青菜")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.3
                col4_value = col4_value + rice_weight * 2.4
                col5_value = col5_value + rice_weight * 1.4
                col6_value = col6_value + rice_weight * 1.1
                col7_value = col7_value + rice_weight * 14
            text = str(row[5])
            start = text.find("藕片")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 4.14
                col4_value = col4_value + rice_weight * 12.54
                col5_value = col5_value + rice_weight * 1.89
                col6_value = col6_value + rice_weight * 3.09
                col7_value = col7_value + rice_weight * 87.64
            text = str(row[5])
            start = text.find("炒饭")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 5.6
                col4_value = col4_value + rice_weight * 31.7
                col5_value = col5_value + rice_weight * 5
                col6_value = col6_value + rice_weight * 2
                col7_value = col7_value + rice_weight * 188
            text = str(row[5])
            start = text.find("苹果")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.2
                col4_value = col4_value + rice_weight * 13.7
                col5_value = col5_value + rice_weight * 0.4
                col6_value = col6_value + rice_weight * 1.7
                col7_value = col7_value + rice_weight * 53
            text = str(row[5])
            start = text.find("菠菜")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.3
                col4_value = col4_value + rice_weight * 4.5
                col5_value = col5_value + rice_weight * 2.6
                col6_value = col6_value + rice_weight * 1.7
                col7_value = col7_value + rice_weight * 28
            text = str(row[5])
            start = text.find("牛肉")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 2.5
                col4_value = col4_value + rice_weight * 1.3
                col5_value = col5_value + rice_weight * 21.3
                col6_value = col6_value + rice_weight * 0
                col7_value = col7_value + rice_weight * 113
            text = str(row[5])
            start = text.find("包菜")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.2
                col4_value = col4_value + rice_weight * 4.6
                col5_value = col5_value + rice_weight * 1.5
                col6_value = col6_value + rice_weight * 1
                col7_value = col7_value + rice_weight * 24
            text = str(row[5])
            start = text.find("鸡蛋")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 9
                col4_value = col4_value + rice_weight * 1.5
                col5_value = col5_value + rice_weight * 12.7
                col6_value = col6_value + rice_weight * 0
                col7_value = col7_value + rice_weight * 138
            text = str(row[5])
            start = text.find("鱼")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 5.2
                col4_value = col4_value + rice_weight * 0
                col5_value = col5_value + rice_weight * 16.6
                col6_value = col6_value + rice_weight * 0
                col7_value = col7_value + rice_weight * 113
            text = str(row[5])
            start = text.find("莴笋")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.1
                col4_value = col4_value + rice_weight * 2.8
                col5_value = col5_value + rice_weight * 1
                col6_value = col6_value + rice_weight * 0.6
                col7_value = col7_value + rice_weight * 15
            text = str(row[5])
            start = text.find("山药")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.2
                col4_value = col4_value + rice_weight * 12.4
                col5_value = col5_value + rice_weight * 1.9
                col6_value = col6_value + rice_weight * 0.8
                col7_value = col7_value + rice_weight * 57
            text = str(row[5])
            start = text.find("猪肉")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 2:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 6.2
                col4_value = col4_value + rice_weight * 1.5
                col5_value = col5_value + rice_weight * 20.3
                col6_value = col6_value + rice_weight * 0
                col7_value = col7_value + rice_weight * 143
            text = str(row[5])
            start = text.find("白萝卜")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 3:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.1
                col4_value = col4_value + rice_weight * 4
                col5_value = col5_value + rice_weight * 0.7
                col6_value = col6_value + rice_weight * 1.1
                col7_value = col7_value + rice_weight * 16
            text = str(row[5])
            start = text.find("胡萝卜")
            end = text.find("g", start)

            if start != -1 and end != -1:
                rice_weight = text[start + 3:end]
                rice_weight = float(rice_weight) / 100

                # 计算新的列的值
                col3_value = col3_value + rice_weight * 0.2
                col4_value = col4_value + rice_weight * 8.1
                col5_value = col5_value + rice_weight * 1
                col6_value = col6_value + rice_weight * 2.4
                col7_value = col7_value + rice_weight * 32
            if col3_value+col4_value+col5_value+col6_value+col7_value !=0:
                # 创建新行
                new_row = [
                    file_name, col1_value, col3_value, col4_value, col5_value,
                    col6_value, col7_value
                ]
                new_rows.append(new_row)

    # 将新的行添加到结果DataFrame中
    result_df = pd.DataFrame(
        new_rows, columns=["id", "time", "fat", "c", "pro", "fiber", "hit"])

    # 将结果保存到result.excel文件
    result_df.to_excel("result.xlsx", index=False)


# 指定要处理的Excel文件路径
excel_file_path = "2000_0_20201230.xlsx"

# 调用处理函数
process_excel_file(excel_file_path)
