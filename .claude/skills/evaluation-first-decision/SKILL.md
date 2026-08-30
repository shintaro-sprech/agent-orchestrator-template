---
name: evaluation-first-decision
description: >
  重要な実装、リリース、導入、購入、価格設定、優先順位、自動化、アーキテクチャ、
  事業方針などを実行前に評価する。成功条件とガードレールを推薦より先に定義し、
  事実・仮定・未確認事項を分離し、現状維持を含む選択肢を比較して、
  最小の安全な実験、停止条件、ロールバック条件を設計し、
  GO、PILOT、HOLD、STOPのいずれかを返す。
  単純な事実確認、文章の添削、自由なアイデア出し、容易に取り消せる低リスク変更には使用しない。
license: MIT
compatibility: "Agent Skills standard; designed for Codex and Claude Code. No external scripts or services required."
metadata:
  author: shintaro-sprech
  version: "0.1.0"
  language: ja
---

# 評価ファースト意思決定

もっともらしい推薦ではなく、後から検証できる意思決定を作る。
説得力より証拠を、平均的な改善より重大な悪化の防止を優先する。

## 適用範囲

次のいずれかを含む判断に使用する。

- 本番公開、リリース、デプロイ、移行、廃止
- AI・自動化・新技術・SaaS・アーキテクチャの導入
- 購入、価格、優先順位、採用、外注、事業方針
- 顧客、利用者、売上、品質、セキュリティ、法務、信用に影響する変更
- 「進めてよいか」「GO/HOLDを判定して」「どちらを選ぶべきか」という依頼

次には通常使用しない。

- 単純な事実確認や用語説明
- 文章の添削、翻訳、要約
- 制約のないアイデア出し
- 影響が小さく、容易に取り消せる日常的な変更

このSkillは原則として判断を設計・評価する。外部送信、購入、削除、本番反映などの実行承認を代替しない。

## 基本原則

1. 評価基準を推薦より先に固定する。
2. 事実、仮定、未確認事項、制約を混ぜない。
3. 現状維持と「何もしない」を必ず比較する。
4. 主目的だけでなく、悪化させてはいけないガードレールを置く。
5. 不確実性が残る場合は、全面導入ではなく最小の安全な実験を選ぶ。
6. 停止条件とロールバックを実行前に定義する。
7. 結果を見た後で成功条件を書き換えない。
8. 高リスクかつ不可逆な判断をAIだけで最終承認しない。

## ワークフロー

### 1. 判断を一文で固定する

次を明確にする。

- 何を決めるのか
- 誰が決定者か
- 対象範囲
- 判断期限
- 現在の状態
- 何もしなかった場合
- 取り消し可能性

情報が不足していても、妥当な仮定を明記して分析を進める。
結論を左右する必須情報だけを `Unknowns` に残す。

### 2. 重要度を分類する

`LOW / MEDIUM / HIGH / CRITICAL` のいずれかに分類する。

判断材料:

- 取り消し可能性と復旧時間
- 影響人数と対象範囲
- 金銭、顧客、品質、信用への影響
- セキュリティ、プライバシー、法務、契約への影響
- 障害を検知できるか
- 証拠の量と不確実性

低リスク判断を過剰に官僚化しない。
`HIGH` または `CRITICAL` では、人間の決定者、停止条件、ロールバックを必須とする。

### 3. 証拠台帳を作る

重要情報を次の4区分に分ける。

- **Confirmed facts**: 直接確認できた事実
- **Assumptions**: 判断のために置いた仮定
- **Unknowns**: 未確認で結論を変え得る事項
- **Constraints**: 予算、期限、人員、技術、契約、運用能力など

出典がある場合は事実の近くに示す。
証拠のない数値、利用者の反応、原因、確率を作らない。

### 4. 推薦前にスコアカードを宣言する

最低限、次を定義する。

- **Primary outcome**: 最も改善したい結果
- **Baseline**: 現状または既存方式の実績
- **Success condition**: 成功と判断する条件
- **Guardrails**: 悪化させてはいけない品質、リスク、負担
- **Stop condition**: 中止またはロールバックする条件
- **Evidence source**: ログ、テスト、データ、観察、ヒアリング
- **Evaluation window**: 期間、件数、対象数、判定日

数値化できない項目は、観察可能な条件で表す。
根拠のない閾値や精密な確率は使わない。

### 5. 選択肢を比較する

最低限、次を含める。

- 提案された案
- 最も有力な代替案
- より小さな変更で済ませる案
- 現状維持または何もしない案

各案を次で比較する。

- 期待便益
- 主な欠点と最悪時の損失
- 実行・保守・運用コスト
- 可逆性
- 観測可能性
- 必要な証拠
- 実行しない場合の機会損失

### 6. 推薦案を反証する

推薦案に不利な証拠を意図的に探す。

- 失敗するとしたら最もあり得る原因は何か
- 誰が不利益を受けるか
- 指標だけ改善し、本来の目的を悪化させないか
- 成功に見える別の説明はないか
- 過去データは今回と比較可能か
- サンプル不足、選択バイアス、計測漏れはないか
- 実行しない方が合理的になる条件は何か

最大の反証を省略・矮小化しない。

### 7. 最小の安全な実験を設計する

証拠が不足する場合は、限定的・観測可能・停止可能・可逆的な実験を設計する。

必須項目:

- 対象と非対象
- 期間または件数
- ベースライン
- 成功条件
- ガードレール
- 計測方法とログ
- 人間による確認箇所
- 停止条件
- ロールバック方法
- 結果を判定する日

割合を機械的に固定しない。
必要に応じてシャドーモード、dry run、ステージング、限定ユーザー、
Feature Flag、Canary rollout、手動レビュー併用を選ぶ。

### 8. 一つの判定を返す

- **GO**: 必要な証拠があり、成功条件とガードレールを満たし、残余リスクを受容できる
- **PILOT**: 有望だが不確実性が残り、限定実験で検証できる
- **HOLD**: 結論に不可欠な証拠、権限、前提、復旧手段が不足している
- **STOP**: ガードレール違反、重大欠陥、許容不能な損失、または実施合理性の欠如が確認された

確信度は `HIGH / MEDIUM / LOW` で示し、理由を一文で付ける。
`GO寄り` など曖昧な中間判定を作らない。条件付きの場合は判定を一つ選び、条件を明記する。

### 9. 結論を変える条件を示す

必ず次を記載する。

- 結論を支持する最大の根拠
- 結論に対する最大の反証
- どの証拠が得られたら判定が変わるか
- 次に確認・実行する最小の一手

## 必須出力

以下の順序を守る。

```markdown
# Decision

**Verdict:** GO / PILOT / HOLD / STOP
**Confidence:** HIGH / MEDIUM / LOW
**Risk level:** LOW / MEDIUM / HIGH / CRITICAL
**Decision owner:** 人または役割
**Decision statement:** 一文

## Executive rationale

結論と理由を3〜6文で示す。

## Decision frame

- Current state:
- Proposed change:
- Status quo / no-action:
- Scope:
- Reversibility:
- Deadline:

## Evidence ledger

### Confirmed facts
### Assumptions
### Unknowns
### Constraints

## Predeclared scorecard

| Dimension | Baseline | Success condition | Guardrail / Stop condition | Evidence source |
|---|---|---|---|---|
| Primary outcome | | | | |
| Quality | | | | |
| Efficiency / cost | | | | |
| User / operator impact | | | | |
| Security / legal / operational risk | | | | |

## Options considered

| Option | Expected benefit | Main downside | Reversibility | Evidence quality |
|---|---|---|---|---|

## Strongest counterargument

推薦案に対する最大の反証を書く。

## Smallest safe test

- Scope:
- Duration or sample:
- Instrumentation:
- Human review:
- Success condition:
- Stop condition:
- Rollback:
- Decision date:

## What would change the verdict

判定を変える証拠または条件を書く。

## Next action

次に行う一つの行動を書く。
```

該当しない欄は削除せず `Not applicable` と理由を記載する。
ユーザーが簡潔な回答を求めた場合も、`Verdict`、根拠、最大反証、次の一手は残す。

## 禁止事項

- 推薦後に評価基準を都合よく変更する
- 一つの指標だけで全体成功と判断する
- 現状維持を比較から外す
- 重大なガードレール違反を平均値で相殺する
- 「問題が報告されていない」を成功の証拠にする
- 相関だけで因果を断定する
- 未確認情報を確定事実として書く
- 存在しない数値、引用、ログ、テスト結果を作る
- 不確実性を隠して断定的に見せる
- 分析を続けるだけで、判定と次の一手を返さない

## 追加リソース

必要な場合だけ読む。

- [評価ルーブリック](references/evaluation-rubric.md): リスク、証拠品質、ガードレール、実験方式の詳細
- [評価ケース](references/eval-cases.md): 発動・非発動テストと期待される判定例
- [Decision Card](assets/decision-card.md): 保存・共有用の記入テンプレート
