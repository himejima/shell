#!/bin/sh

# 実際に使うときは
# 検索対象ディレクトリを更新しましょう。

# find [検索対象ディレクトリ]
# -type ファイルタイプ
# -not -name "検索パターン"

find ./sample-file/ -type f -not -name "*.*"
