# 評価ファースト意思決定Skill

`evaluation-first-decision`は、重要な判断を「推薦」から始めず、
成功条件、ガードレール、証拠、代替案、最小実験、停止条件を先に設計するSkillです。

## できること

- リリースや本番公開の `GO / PILOT / HOLD / STOP` 判定
- AI・SaaS・アーキテクチャ・自動化の導入判断
- 価格、購入、優先順位、事業方針の比較
- 事実、仮定、未確認事項、制約の分離
- 最小の安全な実験とロールバック設計
- 最大の反証と「結論を変える証拠」の明示

## 配置

このリポジトリには同じSkillを2か所へ収録しています。

- Codex: `.agents/skills/evaluation-first-decision/`
- Claude Code: `.claude/skills/evaluation-first-decision/`

両者は同一内容で、`python3 scripts/verify-skill-sync.py` により差分を検出します。

## このリポジトリ内で使う

リポジトリのルートまたは配下でCodex／Claude Codeを起動します。

### Codex

```text
$evaluation-first-decision Androidの新バージョンを本番公開してよいか判定して
```

### Claude Code

```text
/evaluation-first-decision Androidの新バージョンを本番公開してよいか判定して
```

既存のオーケストレーション用 `/task` コマンドとは独立して呼び出せます。
判断後の実装までオーケストレーターへ任せる場合は、先にこのSkillで判定カードを作り、
その判定カードを `/task` の入力に含めてください。

## すべてのリポジトリで使う

### macOS / Linux

```bash
sh scripts/install-evaluation-first-decision.sh
```

### Windows PowerShell

```powershell
.\scripts\install-evaluation-first-decision.ps1
```

インストーラーは既存の同名Skillを削除せず、タイムスタンプ付きのバックアップへ移動してから配置します。

配置先:

- Codex: `~/.agents/skills/evaluation-first-decision/`
- Claude Code: `~/.claude/skills/evaluation-first-decision/`

追加直後に一覧へ表示されない場合は、CodexまたはClaude Codeのセッションを再起動します。

## 推奨する呼び出し方

判断対象だけでなく、確認済み事実、期限、変更可能範囲、既知の失敗を一緒に渡します。

```text
$evaluation-first-decision

判断対象:
Android v47を本番公開してよいか。

確認済み:
- 課金回復の実機テストは成功
- 認証回帰テストは成功
- 既知の500エラーは再現しない
- 段階公開と即時停止が可能

制約:
- 公開期限は9月5日
- コード変更は行わず判定だけ返す
```

## 出力

Skillは次を返します。

- `GO / PILOT / HOLD / STOP`
- 確信度とリスク水準
- 証拠台帳
- 事前スコアカード
- 現状維持を含む選択肢比較
- 最大の反証
- 最小の安全な実験
- 判定を変える条件
- 次に行う一つの行動

## 更新方法

`.agents/skills/evaluation-first-decision/` と
`.claude/skills/evaluation-first-decision/` の同じファイルを更新し、次を実行します。

```bash
python3 scripts/verify-skill-sync.py
```

評価ケースは `references/eval-cases.md` に追加します。
実際の利用で誤発動、重要項目の欠落、不要な長文化が見つかった場合は、
抽象的な注意書きよりも具体的なテストケースを先に追加してください。
