# Script.py using polars and matplotlib to set data and see some plot

import os
import polars as pl
import matplotlib.pyplot as plt
from lib import load_data

my_data = "Auto.csv"


# Calculate mean, median, standard deviation of each columns
def calculate_stat(dataset):
    data = load_data(dataset)
    data_desc = data.describe()
    print(data_desc)
    return data_desc


# Make a boxplot of each columns in csv file
def build_boxplot(dataset):
    data = load_data(dataset)
    numeric_columns = data.select_dtypes(include=["number"]).columns

    directory_path = (
        "C:/Users/User/.git/Suim-Park-Individual-Project-1/Outputs"  # 원하는 경로로 변경
    )
    folder_name = "Graphs"
    save_folder = os.path.join(directory_path, folder_name)

    # 폴더가 존재하지 않는 경우 폴더를 생성
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for column in numeric_columns[1:7]:
        plt.figure()  # 새로운 그래프 생성
        plt.boxplot(data[column].to_list())  # Box Plot 그리기
        plt.title(f"{column} Box Plot")  # 그래프 제목 설정
        plt.xlabel("Value")  # x축 레이블 설정
        plt.ylabel("Distribution")  # y축 레이블 설정

        save_path = os.path.join(save_folder, f"boxplot {column}.png")
        plt.savefig(save_path)

        plt.show()
    return


if __name__ == "__main__":
    calculate_stat(my_data)
    build_boxplot(my_data)