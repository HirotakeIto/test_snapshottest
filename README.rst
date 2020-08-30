=====================
test_snapshottest
=====================

snapshottestの使い方をメモします。
特にpandas dataframeの記述統計をテストする方法を注記します。

使い方
========
* テスト実行
``` cmd
pytest tests/test1.py
```

* テスト更新
``` cmd
pytest tests/test1.py --snapshot-update
```

注記
========
* テスト結果が保存される場所
上述の様にテストを実行した場合 `tests/snapshots`

* テストの中で記述統計を出力するための格納場所
上述の様にテストを実行した場合 `tests/data`

コードの実行によって得られた結果は`tests/data`にcsvファイルとして格納され、その格納された結果は`tests/snapshots`に保存された以前のテスト結果と比較される。


