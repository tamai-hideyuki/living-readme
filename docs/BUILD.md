# Build

SVGは `src/` 配下のパーツから生成します。READMEで使うファイルは `assets/` に出力されます。

## コマンド
```bash
python3 scripts/build_assets.py
```

## 構成
- `src/template.svg`: 共通テンプレート
- `src/defs/*.svg`: defs（グラデーションやフィルタ）
- `src/bodies/*.svg`: 本体の要素
- `src/scenes/*.json`: 出力設定
- `assets/*.svg`: 生成物
