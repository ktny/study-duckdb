## start

docker compose run db bash

```sh
python gen_csv 1000000
```

## DuckDB

```sh
# DuckDB起動
./duckdb test.duckdb

# DuckDB起動（複数同時Read可能、Write不可）
./duckdb --readonly test.duckdb

# CSVからテーブル作成
create table test as select * from read_csv_auto("data/1m.csv");

# テーブルをparquetでエクスポート
copy test to 'data/1m.parquet' (FORMAT PARQUET);

# parquetからテーブル作成
create table test_p as select * from read_parquet("data/1m.parquet");

# parquetに対して直接クエリを作成
select * from read_parquet("data/1m.parquet");

# DuckDBの設定確認
select * from duckdb_settings();
```

## その他のduckdb上での操作

```sh
# データベース確認
.database

# テーブル確認
.tables
```
