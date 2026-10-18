# Hound 個人 fork：分支與執行說明

Upstream：<https://github.com/scabench-org/hound>。本 fork 從 upstream commit `83ce761952b00d9090ac0911b5e618bf3753087f` 開始，保留原專案 Git history。

## 分支

| 分支 | 分析用途 | 共同輸出功能 |
|---|---|---|
| `main`（預設） | Planning、Scout、Deep Think 聚焦 price manipulation | 原生 report ＋ direct PredictionCase |
| `general-auditing` | 原始 general auditing 範圍 | 原生 report ＋ direct PredictionCase |

main 的三個分析任務使用 price scope，不需要另外輸入 `--mission`。Graph Builder 與 Finalize 的 scope prompts 沿用 upstream；兩個分支共用 Deep Think structured output、Finding 保存及 export 修改。

general-auditing 是共用功能的基底；main 在其上加入 price-focused 指引。未來共用修正可以先放在 general，再同步至 main；price-specific 變更只放 main。

## 安裝與切換

建議 Python 3.12 或 3.13。

```bash
git clone https://github.com/Tang-Chieh/hound.git
cd hound
git remote add upstream https://github.com/scabench-org/hound.git
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

預設 main 為 price-focused；一般分析改用：

```bash
git switch general-auditing
# 回到 price-focused
git switch main
```

切換前請先處理未提交修改，並為兩種分析使用不同 project，避免沿用另一組的 hypotheses 或 investigation state。

## 模型設定

使用自己的 provider API 設定時，參考 upstream README 與 `config.yaml.example`。若已有相容的本機 Codex gateway，可使用 `config.group-example.yaml`（指定 `openai-codex/gpt-5.6-luna`）：

```bash
cp config.group-example.yaml config.yaml
export HOUND_GATEWAY_TOKEN='<your-local-gateway-token>'
export HOUND_OPENAI_USE_RESPONSES=1
```

範例 gateway URL 為 `http://127.0.0.1:14000/v1`。登入及啟動 gateway 的說明在 Private 整合實驗 repo；本 fork 不包含憑證。Finalize 會沿用選定的 `HOUND_CONFIG`／model 設定。

## 執行

```bash
python hound.py project create my-price-audit /absolute/path/to/solidity-repo
python hound.py graph build my-price-audit --init --iterations 1
python hound.py agent audit --project my-price-audit --iterations 5 --time-limit 30
python hound.py finalize my-price-audit
python hound.py report my-price-audit --repo-id example-repo \
  --prediction-case-output outputs/example-repo.json
```

graph／audit／finalize／report 會依設定呼叫模型。這是一般使用範例；重現既有 23-repo C/D 實驗需沿用相同 graph／manifest，請遵循 Private 整合 repo 的 README。

## 改動

- Deep Think schema 加入 description、impact、vulnerable_code、mitigation，並保存到 hypothesis。
- report 新增成對參數 `--prediction-case-output`／`--repo-id`，只輸出 confirmed findings，同時保留原生報告。
- mitigation 由模型建議，exporter 讀取已保存值；缺少時使用明確 placeholder，不代表建議已獨立驗證。
- Finalize 沿用選定 provider／model 配置。
- 補上 clean install 依賴、CLI package 設定及 regression tests。
- main 另加入 price manipulation scope。

Public fork 保存程式、設定範例、測試、說明，以及最新 C/D 的完整實驗結果與評估報告，兩個分支都有相同結果。請由 [實驗索引](../experiments/README.md) 查看。評估 manifest 本身包含此次比對的 Ground Truth 文字；獨立 Ground Truth dataset、LLM Judge 程式與完整重現工具仍保存在 Private 整合 repo。

## 測試

```bash
python -m pytest -q tests
```

自動 CI 在 main、general-auditing 執行 Python 3.12／3.13 pytest，不需模型登入。upstream 的完整 Ruff style workflow 保留為手動執行，未為此次移植大規模格式化原專案。
