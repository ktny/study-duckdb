import csv
import os
import random
import string
import sys
from datetime import datetime, timedelta

DATA_DIR = "data"


def generate_random_string(length):
    """ランダムな文字列を生成します。"""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def generate_random_date():
    """ランダムな日付を生成します。"""
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


def create_csv(num_rows):
    """CSVファイルを生成します。現在の日時をファイル名に含めます。"""
    now = datetime.now()
    # testディレクトリのパスを生成
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)  # testディレクトリがない場合は作成
    filename = now.strftime("%Y%m%d_%H%M%S.csv")
    filepath = os.path.join(DATA_DIR, filename)  # ファイルパスを指定

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "str", "int", "date"])  # ヘッダー行

        for i in range(num_rows):
            row = [
                i + 1,  # ID
                generate_random_string(10),  # ランダムな文字列（10文字）
                random.randint(1, 10000),  # ランダムな数値
                generate_random_date(),  # ランダムな日付
            ]
            writer.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_csv.py [num_rows]")
        sys.exit(1)
    num_rows = int(sys.argv[1])
    create_csv(num_rows)  # コマンドライン引数から取得した行数でCSVファイルを生成
