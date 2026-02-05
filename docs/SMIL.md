# SMIL（SVGアニメーション）まとめ

このドキュメントは、READMEで使うSVGアニメーション（SMIL）についての要点をまとめたものです。

## できること
- `cx`/`cy`/`r`/`opacity` などの属性を時間で変化させる
- パスの `d` を変化させて波形や形状をうねらせる
- 1つの要素に複数の `animate` を付けて複雑な動きを作る
- `defs` + `use` で部品を再利用する

## 基本構文
```svg
<animate attributeName="cx" values="100;200;100" dur="10s" repeatCount="indefinite" />
```
- `attributeName`: 変化させたい属性名
- `values`: 変化の流れ（`;` 区切りで列挙）
- `dur`: 1サイクルの時間
- `repeatCount`: 反復回数（`indefinite` で無限）

## よく使う属性
- 位置: `x`, `y`, `cx`, `cy`
- サイズ: `r`, `width`, `height`
- 透明度: `opacity`
- 形状: `d`（path）, `points`（polygon）

## 例（複合アニメーション）
```svg
<circle cx="220" cy="150" r="150" fill="url(#orangeGlow)">
  <animate attributeName="cx" values="220;620;420;180;220" dur="32s" repeatCount="indefinite" />
  <animate attributeName="cy" values="150;90;210;120;150" dur="28s" repeatCount="indefinite" />
  <animate attributeName="r"  values="140;165;150;170;140" dur="24s" repeatCount="indefinite" />
  <animate attributeName="opacity" values="0.85;0.6;0.8;0.55;0.85" dur="20s" repeatCount="indefinite" />
</circle>
```

## 部品化（再利用）
```svg
<defs>
  <symbol id="softOrb" viewBox="-100 -100 200 200">
    <circle r="80" fill="url(#glowA)">
      <animate attributeName="r" values="70;90;70" dur="20s" repeatCount="indefinite" />
    </circle>
  </symbol>
</defs>

<use href="#softOrb" x="200" y="120" />
<use href="#softOrb" x="520" y="180" />
```
- `use` は同じ動きが複製される
- 変化の差分が欲しい場合は、シンボルを複数用意するのがシンプル

## READMEでの注意点
- GitHub READMEではJavaScriptは動かない
- SMILだけで完結するアニメーションが安定
- `viewBox` を設定しておくと縮小表示でも破綻しにくい

## 推奨パターン
- 長さは `20s〜60s` 程度でループ
- `values` は往復形にすると落ち着く動きになる
- 透明度変化とサイズ変化を組み合わせると“生きてる感”が出る
