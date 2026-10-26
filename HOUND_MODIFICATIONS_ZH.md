# Hound 改動與 C、D 組實驗整理

整理日期：2026-10-24。Workspace：`/Users/williamtang/Documents/Codex/2026-07-16/new-chat`。

GitHub 文件發布版：2026-10-26。本次發布說明文件，實驗數據仍對應下述歷史批次。

目前分享入口為 [Tang-Chieh/hound](https://github.com/Tang-Chieh/hound) 與 [整合實驗 repo](https://github.com/Tang-Chieh/Hound_price_manipulation_experiments)。下文 `Hound_general/`、`Hound_focus_price_manipulation/` 與對應 HEAD 是該歷史實驗的程式來源記錄；目前正式 fork 的 `main` 為 price-focused、`general-auditing` 為 general 版本。歷史本機路徑與當時 remote 名稱不應視為目前 clone／重現的入口，請以各 repo README 為準。

## 摘要

本文件依照 `SMARTAUDITFLOW_MODIFICATIONS_ZH.md` 的結構，整理 Hound 原本的工作流程、Codex OAuth gateway 連線方式、dataset repo 輸入、price-manipulation prompt、直接輸出 `PredictionCase` 的修改，以及正式 LLM Judge 的執行與報告。

目前 C、D 執行的是兩個獨立的本機 Hound 程式副本，remote 分別為 `Tang-Chieh/Hound_general` 與 `Tang-Chieh/Hound_focus_price_manipulation`。最近一次 Hound 執行在 2026-10-22 開始，2026-10-23 使用其既有 predictions 重新呼叫 LLM Judge；本文件整理時沒有重新執行分析。

最近已完成的結果是 **24 repos、43 筆 ground truth**。之後的執行設定已依使用者要求排除 `margintrading`，對應目前 **23 repos、42 筆 ground truth**；下文的歷史成績仍是 24-repo 結果，不能當成排除後的成績。

## 1. 原本 Hound 如何運作

Hound 接收 repository 路徑，透過 project、source ingestion、graph 與 agent investigation 逐步探索程式，不需要先把 repo 串成一個巨大的 Solidity snippet。

1. **Project creation**：註冊 repo 路徑，建立 Hound project 儲存位置。
2. **Ingestion／Graph Modeling**：掃描來源，建立 manifest、source cards、bundles 與 graphs，保留程式碼到來源檔案的參照。cards 是 agent 可載入的程式片段；graph 用來協助探索結構與關係。
3. **Planning／Strategist**：參考 graph、既有 hypotheses、調查歷史及 coverage，產生下一步 investigation goals。
4. **Scout**：讀取相關 graph nodes 與實際程式碼，收集 investigation 所需的脈絡，交給 Deep Think。
5. **Deep Think／Strategist**：分析 Scout 準備的 context，提出有程式證據的 hypotheses、root cause、attack vector 與後續 guidance；Scout 可依 guidance 繼續探索。
6. **Finalize／QA**：審查符合條件的 hypotheses，確認或拒絕，保留理由。未被定案的 hypothesis 可能仍維持 proposed 等狀態。
7. **Report**：從 project 資料產生 Hound HTML security report。

Planning、Scout、Deep Think 之間會互動，不是將完整 repo 一次全部塞給一個模型。Deep Think 是 Hound 的模型呼叫角色／方法，不是另外訓練的一個專用模型。

Hound 的 `confirmed` 是工具內部的審查狀態；是否對應本專案 ground truth，仍須由後面的 benchmark Evaluation 比較。

## 2. Codex OAuth gateway：如何使用訂閱授權

Hound 仍使用 OpenAI-compatible provider。實驗設定將請求送往本機 gateway，由 gateway 與 auth broker 使用既有的 Codex OAuth 授權。

```text
Hound 的各模型角色
    → llm/openai_provider.py / OpenAI Python SDK
    → http://127.0.0.1:14000/v1
    → 本機 auth gateway + auth broker
    → Codex OAuth session
    → openai-codex/gpt-5.6-luna
```

### 2.1 Provider 與環境設定

主要檔案為兩個 Hound repo 的 `llm/openai_provider.py`、`config.group-example.yaml`，以及 workspace 下的實驗 YAML 與 runner。

實驗使用的關鍵設定如下；token 由使用者自己的本機授權環境提供：

```yaml
openai:
  api_key_env: HOUND_GATEWAY_TOKEN
  base_url: http://127.0.0.1:14000/v1
models:
  agent:
    provider: openai
    model: openai-codex/gpt-5.6-luna
```

- `HOUND_CONFIG`：指定實驗 YAML。
- `HOUND_GATEWAY_TOKEN`：提供本機 gateway 所要求的 bearer token。
- `OPENAI_BASE_URL`：將 OpenAI-compatible client 指向本機 gateway。
- `HOUND_OPENAI_USE_RESPONSES=1`：強制使用 Responses 路徑。這對帶 `openai-codex/` 前綴的模型名稱很重要，不能只依 `gpt-5` 開頭的自動判斷。

`HOUND_GATEWAY_TOKEN` 是本機 gateway 的存取憑證，不是公開 OpenAI API 的付費 API key，也不等於 OAuth access token。OAuth credential 由 gateway／broker runtime 管理。

`openai_provider.py` 的 Responses structured-output 路徑會將 schema 提示加入 instructions，要求 JSON，並在本機解析、驗證。這不保證每次模型回應的格式都正確；解析失敗仍須依程式的 retry／fallback 邏輯處理。

最近一輪 Hound 使用 `hound-subscription-gpt56-luna-retry.yaml`，各模型角色設定為 `openai-codex/gpt-5.6-luna`，context 設為 64,000 tokens。這是實驗的 context 設定，不是宣稱模型的最大 context window 就是 64,000。

### 2.2 Finalize 的程式修正

`commands/finalize.py` 改用 `utils/config_loader.py` 的 `load_finalize_config()`，讓 Finalize 和其他命令一樣尊重 `HOUND_CONFIG`，並保留 CLI 的 platform／model override。

這解決 Finalize 可能回到預設 config、因而沒有沿用本機 gateway 與指定模型的問題。此修改是配置解析修正；Finalize 的漏洞審查指令沒有因此改成 price-only。

相關 regression tests 在 `tests/test_finalize_config.py`，涵蓋環境設定及 CLI override 的配置保留。本文沒有重新執行整套 Hound 測試。

## 3. Dataset 如何作為 Hound 輸入

### 3.1 選擇哪些 repos

最近的實驗以 SCAR 的 `dataset/downstream-stage1/pilot-v1/ground_truth/` 對應的 repo IDs 選取來源。Hound 實際讀取的程式碼位於：

```text
prototype-reusable-dataset/candidate-repos/<repo_id>/
```

runner 使用 repo ID 選擇程式碼；ground-truth finding 的漏洞描述、位置、impact 與 mitigation 不會放入 Hound 分析 prompt。Ground truth 內容是在獨立的 Judge 階段才加入比較。

最近一次使用的 `ground_truth_snapshot/` 已逐檔以 JSON 內容比對 SCAR commit `5cab8f68217607117f9403d2adb9481ec5d0ec10`，24 repos、43 筆 findings 的內容一致。

### 3.2 Hound 自己的 ingestion 與 context

`commands/graph.py` 使用 `ingest/manifest.py` 的 `RepositoryManifest` 及 `ingest/bundles.py` 的 `AdaptiveBundler`，建立／讀取 manifest、cards 與 bundles。Scout 再依 investigation 載入程式片段。

這套輸入方式保留 repo 目錄與多檔案結構。它沒有套用 SmartAuditFlow 的 flatten／snippet 清理程式，也沒有將所有 `.sol` 的 import、pragma 刪除後串成單檔。實際納入範圍仍受 Hound 的 ingestion、whitelist、sampling 與 context 管理影響，不能只因輸入了 repo 路徑就宣稱完整讀過所有原始碼。

### 3.3 最近實驗的 graph 控制

為了讓 C、D 使用相同的 graph 輸入，最近一輪：

- 23 個原有 repo 沿用歷史 Group A 的 manifest／graphs。
- 新加入的 `margintrading` 用 general Hound 建立一次共用 graph，供 C、D 使用。
- C、D 都重新執行 audit、Finalize、report／PredictionCase export。

因此最近的 C、D 不是全部從 graph build 重新開始；也不能根據本輪模型設定推論歷史 graph 都由 `gpt-5.6-luna` 重新建立。這些 graph 是共用的既有實驗輸入。

### 3.4 之後排除 margintrading

`subscription-gateway-pilot/experiment_repo_policy.py` 設定：

```python
EXCLUDED_REPO_IDS = frozenset({"margintrading"})
```

`run_hound_cd_latest_gt.py`、`run_23_repos_groups_cd.py` 和 `run_four_stage_llm_judge.py` 都會套用排除規則。之後 Hound 與 Judge 的選取範圍為目前剩餘 23 repos／42 筆 GT；原始 ground truth 與歷史 24-repo 結果保留。

## 4. Price-manipulation prompt：具體改了什麼

### 4.1 C、D 的設定

| 項目 | Group C：Hound_general | Group D：Hound_focus_price_manipulation |
|---|---|---|
| Planning／Scout／Deep Think 分析範圍 | General auditing | Price manipulation |
| `--mission` | 未使用 | 未使用 |
| Graph Modeling 的 price-focused prompt | 沒有 | 沒有 |
| Finalize 的 price-focused prompt | 沒有 | 沒有 |
| Deep Think finding 欄位 | 兩組都新增 | 兩組都新增 |
| Hound 直接輸出 PredictionCase | 有 | 有 |

這裡應描述為「三個分析指引聚焦 price manipulation」，不能描述成 Graph、Planning、Scout、Deep Think、Finalize 全部都改成 price-only。

### 4.2 共用 scope 的原文

Group D 的 `analysis/strategist.py` 加入：

```text
AUDIT SCOPE:
This audit exclusively targets price manipulation vulnerabilities.
Focus planning and vulnerability analysis on this category. Do not intentionally
investigate or report unrelated vulnerability classes. Preserve the original
auditing methodology, exploration behavior, and evidence requirements.
```

`analysis/agent_core.py` 加入對應的 Scout scope，將第三句改為 `Focus exploration on this category.`，並保留不刻意調查無關漏洞、維持原方法與證據要求的指引。

這份程式中的共用 scope 本身是上述簡短文字；不能把討論過的 reserves、TWAP、freshness 等所有建議清單，都說成已逐條加入實際 prompt。

### 4.3 每個分析階段的改動

| 階段／檔案 | 原本指引 | Group D 的具體修改 |
|---|---|---|
| Planning：`analysis/strategist.py` | 規劃一般安全調查，例子包含高影響權限問題。 | 將共用 scope 接到 planning system prompt；將 `HIGH-IMPACT AUTH` 例子換成 `PRICE-MANIPULATION PATHS: Price and oracle inputs affecting financial outcomes`；將 permission-check 例子換成 price-path safeguards；新增追蹤 manipulable price input 到 financial operation 的調查例子。 |
| Scout：`analysis/agent_core.py` | 收集程式與 facts，Deep Think 可從 context 找出其他漏洞。 | 在 Scout system prompt 附加 price scope；把交給 Strategist 分析的「其他漏洞」改為「其他 price manipulation 漏洞」。Scout 仍負責收集證據，保留載入實際程式碼後才呼叫 Deep Think 的角色分工。 |
| Deep Think：`analysis/strategist.py` | `Look for ALL types of vulnerabilities`，並允許提出與目前 goal 不同的其他漏洞。 | 改為 `Look for price manipulation vulnerabilities`；要求 `Trace attacker-influenceable prices or valuations into financially sensitive operations and check relevant protections`；把 system、user 及額外 hypotheses 的範圍都限制為 price manipulation。 |
| Graph Modeling | 建立圖與 source 關係。 | 沒有加入 Group D 的 price scope，最近實驗使用共用 graph。 |
| Finalize／QA | 審查 hypotheses 的證據與狀態。 | 沒有加入 price-only 審查指令；保留原邏輯，另有上一節所述的 config 修正。 |

Planning 原有的 investigation 規劃方法、coverage／history 輸入與去重要求仍保留；Deep Think 也保留 root-cause evidence、有效節點與程式位置、既有防護及 false-positive guardrails。

### 4.4 目前兩個副本的細節差異

兩組主要比較 general scope 與 price scope，但不能宣稱其他 prompt 的每個字都完全相同。例如 C 的 legacy pipe-separated hypothesis prompt 明確要求 `Suggested Mitigation`，D 對應的部分文字仍是九欄格式；兩組主要的 strict-JSON 分支則都有要求 `mitigation`。D 的 schema／review 提示也有少量措辭差異。

這是目前程式比對發現的限制。若要做嚴格的「只改 scope」消融實驗，應先統一非 scope 的 fallback／output 提示，再另做實驗；本文沒有修改這些分析 prompt。

## 5. Hound output 如何符合 LLM Judge input

直接輸出不只是把最後一份 HTML 換個副檔名；修改涵蓋模型生成欄位、儲存與 report export 三層。

### 5.1 Deep Think 提早生成 Finding 欄位

兩組 `analysis/strategist.py` 的 `HypothesisItemJSON` 新增／保存 `description`、`impact`、`vulnerable_code`、`mitigation`。其中 source location 使用 `VulnerableCodeItemJSON`：`file`、`contract`、`function`，以及 optional `start_line`／`end_line`。

在原本分析 prompt 後，strict-JSON 分支具體加入：

```text
Each hypothesis must include the direct Finding fields
title,description,impact,vulnerable_code,mitigation,
plus finding analysis fields
type,root_cause,attack_vector,node_ids,affected_code,severity,confidence,reasoning.
```

位置要求使用 loaded code 中的確切資訊；行號提供兩個或都不提供，位置不確定時使用 `[]`，不猜測。`impact` 要說明具體後果；`mitigation` 要依 root cause 提出具體建議，不能聲稱修補已實作或已驗證。

`mitigation` 是這次 Deep Think 模型依指引生成的建議，不是 report script 人工截取 QA comment 補上的文字。模型或 fallback 分支仍可能漏掉欄位，因此「要求輸出」不代表每次都能保證內容存在或正確。

### 5.2 儲存與傳遞

- `analysis/strategist.py`：解析模型輸出，將 finding 欄位放入候選 hypothesis；review 路徑保留／保守調整建議 mitigation。
- `analysis/agent_core.py`：把 mitigation、finding description、impact 與 vulnerable-code 資訊傳給 hypothesis 儲存流程。
- `analysis/concurrent_knowledge.py`：Hypothesis 資料模型保存這些欄位，讓 report 階段能從 `hypotheses.json` 取得資料。

### 5.3 Report command 直接序列化

`hound.py` 與 `commands/report.py` 增加選項：

```bash
python hound.py report <project> \
  --output /absolute/path/to/report.html \
  --repo-id <repo_id> \
  --prediction-case-output /absolute/path/to/predictions/<repo_id>.json
```

`--repo-id` 與 `--prediction-case-output` 必須一起提供。原本的 HTML report 仍產生，另外由 Hound report command 直接寫出：

```json
{
  "repo_id": "example-repo",
  "detector_metadata": {
    "detector_version": "hound-direct-prediction-case-v1",
    "llm_model": "openai-codex/gpt-5.6-luna"
  },
  "predictions": [
    {
      "finding_id": "hyp_example",
      "title": "AMM spot price can affect collateral valuation",
      "description": "Evidence-grounded explanation from Hound.",
      "impact": "Concrete financial consequence described by the model.",
      "vulnerable_code": [
        {"file": "contracts/Pool.sol", "contract": "Pool", "function": "borrow"}
      ],
      "mitigation": "Model-suggested remediation addressing the stated root cause.",
      "severity": "high"
    }
  ]
}
```

上面是格式示意，不是本次實驗的真實 finding。

export 的實際規則：

1. 只匯出 Hound `status == confirmed` 的 hypotheses；proposed、rejected 不進入主要 predictions。
2. finding ID、title、description、impact、mitigation 來自已儲存的 hypothesis；repo ID 與 detector metadata 由 runtime 補入。
3. 對 location 檢查非空 file／contract／function，以及行號是否為有效、成對的正整數區間。這是格式檢查，沒有保證符號一定對上原始碼，也沒有替模型重新查證位置。
4. 不合格的 location 被過濾，finding 本身仍可保留，因而可能輸出 `vulnerable_code: []`。
5. impact 或 mitigation 缺失時，仍有 `Not provided in the Hound output.` fallback。不能把這種 placeholder 當成模型提供的有效內容。
6. report export 不額外呼叫模型補寫 impact／mitigation；它直接序列化 Hound 已有資料。原生 HTML report 的生成流程則仍可使用 reporting 模型。

### 5.4 最近結果的 output 檢查

對最近 24-repo predictions 逐筆檢查：

| 項目 | C | D |
|---|---:|---:|
| 匯出 predictions | 112 | 41 |
| mitigation 為空或上述 placeholder | 0 | 0 |
| impact 為空或上述 placeholder | 0 | 0 |
| vulnerable_code 為空陣列 | 35 | 13 |

這只能證明最近這批文字欄位有內容，不能保證每個 mitigation 都正確或充分。空位置也表示定位資訊仍有缺漏，可能影響 Judge 的 L 分數；不能宣稱所有 output 欄位的語意都完整。

本次主要 predictions 沒有 `verdict`。SCAR 正式 evaluator 接受這種 legacy input，產生 report version 0.2 的單視圖報告。範例中的 version 0.3 三視圖報告需要 `verified`／`needs_review` 標籤；目前沒有建立這個 mapping，也沒有將 Hound confirmed 直接假定為獨立驗證的 verified。

## 6. 完整流程與重現方式

```text
ground_truth 對應的 repo IDs → 套用排除 margintrading 的實驗政策
                     ↓
dataset 的原始 repo 路徑 → 建立 Hound project
                     ↓
新建 ingestion／graph，或為實驗控制而載入固定 manifest／graphs
                     ↓
Planning → Scout 載入 graph／source → Deep Think → hypotheses
              ↑                  │
              └──── guidance ────┘
                     ↓
Finalize／QA → confirmed hypotheses
                     ↓
Hound HTML report + 直接輸出 PredictionCase JSON
                     ↓
SCAR evaluate_directory：驗證 input、組裝 manifest
                     ↓
LLM Judge 逐批比較 predictions 與本專案 ground truth，回傳 R／L／I／M
                     ↓
正式 evaluator 計算門檻／matching／metrics
                     ↓
manifest.json + judge_artifact.json + report.json + 原生 report.md
```

### 6.1 單 repo 的 Hound 流程

以下需先安裝對應 Hound repo 的依賴、完成自己的 gateway OAuth 登入並設定環境變數。以 C 的程式目錄為例，D 改用另一個 checkout：

```bash
cd /Users/williamtang/Documents/Codex/2026-07-16/new-chat/Hound_general
python hound.py project create my-audit /absolute/path/to/repo
python hound.py graph build --project my-audit --auto
python hound.py agent audit --project my-audit \
  --mode sweep --iterations 5 --plan-n 1 --time-limit 30
python hound.py finalize my-audit
python hound.py report my-audit \
  --output /absolute/path/to/report.html \
  --repo-id example-repo \
  --prediction-case-output /absolute/path/to/predictions/example-repo.json
```

這是「從新的 repo project 開始」的操作流程。若要重現最近 C、D 的實驗控制，應在 audit 前載入相同歷史 manifest／graphs，而不是用這條 graph build 指令重新產生不同的圖。

最近批次實際借用 `hound-subscription-pilot/.venv/bin/python` 作為 Python 環境，但執行的 `hound.py` 分別在新的 C、D 程式目錄。舊 repo 的 Python 環境與分析程式來源是兩件事。

`run_hound_cd_latest_gt.py` 記錄最近的批次設定並套用 repo 排除政策；它的 dataset、RUN_ROOT、baseline graph 路徑是本機固定路徑，執行前須改為新輸出目錄。它會拒絕覆寫已存在的歷史 run。不要直接執行舊 `run_23_repos_groups_cd.py` 就假設模型相同：該歷史模組的 default 仍有 `gpt-6-luna`，最近批次是由外層 runner 明確覆寫成 `gpt-5.6-luna`。

### 6.2 只重跑 Judge

最近已將 `run_four_stage_llm_judge.py` 改用 SCAR 的正式 `EvaluationConfig` 與 `evaluate_directory()`。它預設匯入隔離保存的 SCAR commit `5cab8f6` evaluator source，可用 `BENCHMARK_EVAL_SOURCE` 指定其他正式 evaluator checkout；不使用原本自行撰寫的簡化 Markdown renderer。

以下命令使用既有 C predictions，套用目前排除政策，因此會選 23 repos／42 筆 GT。D 將 `group-c` 路徑改成 `group-d`，並使用另一個新 output directory：

```bash
cd /Users/williamtang/Documents/Codex/2026-07-16/new-chat/subscription-gateway-pilot
../hound-subscription-pilot/.venv/bin/python run_four_stage_llm_judge.py \
  --predictions-dir results/hound_24_repo_cd_latest_gt_20261022/group-c/llm_judge/inputs/predictions \
  --ground-truth-dir results/hound_24_repo_cd_latest_gt_20261022/ground_truth_snapshot \
  --output-dir results/judge_reproduce_20261024_without_margintrading/group-c \
  --model gpt-5.6-luna --weight-profile end-to-end-v2 --batch-size 10
```

這個命令會真正重新呼叫 Judge，需要有效 gateway 授權；output directory 內不能已有 Evaluation artifacts。本文只提供命令，沒有為了文件再次執行。

Judge 的 gateway client 相容層只將回應解析成正式 evaluator 要求的 JSON shape，不自行計算模型分數。匹配與 metrics 由 SCAR 負責。`report.md` 由 SCAR 自帶 `write_evaluation_markdown()` 從 canonical artifacts 渲染，含完整設定、repo summaries、matched scores、Judge rationales 與未匹配 findings。

## 7. 最近一輪實驗結果與實際覆蓋程度

下面是 **2026-10-22 Hound 結果 + 2026-10-23 重新呼叫 Judge** 的 24-repo 成績；沒有套用後來要求的 margintrading 排除。

| 指標 | Group C | Group D |
|---|---:|---:|
| Repositories | 24 | 24 |
| Ground-truth findings | 43 | 43 |
| Predictions | 112 | 41 |
| 本輪新 Judge 模型回應 | 36 | 32 |
| Matched prediction／GT pairs | 6 | 9 |
| Total matched weight | 5.6000 | 7.9000 |
| Pooled soft precision | 0.0500 | 0.1927 |
| Pooled soft recall | 0.1302 | 0.1837 |
| Macro soft F1 | 0.0578 | 0.1394 |
| Pooled soft F1 | 0.0723 | 0.1881 |

模型為 `gpt-5.6-luna`，Judge prompt 是 `benchmark-judge-v3`，權重為 `end-to-end-v2`：R 0.40、L／I／M 各 0.20，threshold 0.50，greedy matching。R／L／I／M 分別評估 root cause、localization、impact、mitigation 的對應程度。Matched weight 是分數總和，不是找到漏洞的整數筆數。

本輪 response IDs 已與前次 Judge artifacts 比對，C、D 都沒有重用前次 IDs；報告與 canonical renderer 的輸出一致。

### 7.1 「全部 repo 有跑」不等於「全部程式碼看完」

| 執行與 coverage 記錄 | C | D |
|---|---:|---:|
| Hound audit／Finalize／export 完成 | 24/24 | 24/24 |
| Nodes visited（合計） | 1,064/1,233 | 1,026/1,233 |
| Cards analyzed（合計） | 1,597/8,584，18.6% | 1,547/8,584，18.0% |
| 達到 30 分鐘 audit 限制 | `2021-08-notional` | 無 |

每 repo audit 設定為最多 5 iterations、`--plan-n 1`、30 分鐘上限。Finalize 和 reporting 在 audit 之後另外執行，因此 30 分鐘不是整個 repo pipeline 的絕對牆鐘上限。

cards／nodes 是 Hound 自己的探索統計，不能直接當成 source-line、branch 或漏洞覆蓋率。未達時間限制也不代表所有 cards 都分析完；整個 repo 流程 exit 0 也不代表全面審計完成。

本輪 D 的 soft-match 指標高於 C，但這是單次、有限探索預算下的比較。未匹配 prediction 可能是 ground truth 未收錄的其他問題，也可能是誤報，不能單憑未匹配就判定全部為 false positive。

## 8. 程式、版本與完整產物

| 內容 | 位置／版本 |
|---|---|
| Group C 分析程式 | `Hound_general/`；檢查時本機 HEAD：`39554b0`；remote：`Tang-Chieh/Hound_general` |
| Group D 分析程式 | `Hound_focus_price_manipulation/`；檢查時本機 HEAD：`2bb2352`；remote：`Tang-Chieh/Hound_focus_price_manipulation` |
| Hound snapshot 的 upstream 基礎 | repo README 記錄 `d558f15925046063e38e7a69ea3ac03bb36caa3c`；不代表追到 upstream 最新版本 |
| 最近的 Hound 批次 runner | `subscription-gateway-pilot/run_hound_cd_latest_gt.py` |
| 共用實驗 runner | `subscription-gateway-pilot/run_23_repos_groups_cd.py` |
| 之後的 repo 排除政策 | `subscription-gateway-pilot/experiment_repo_policy.py` |
| 正式 Judge runner | `subscription-gateway-pilot/run_four_stage_llm_judge.py` |
| 正式 evaluator source snapshot | `subscription-gateway-pilot/evaluator-sources/scar-5cab8f6/`；SCAR commit `5cab8f68217607117f9403d2adb9481ec5d0ec10` |

最近實驗的共同根目錄：

```text
subscription-gateway-pilot/results/hound_24_repo_cd_latest_gt_20261022/
├── ground_truth_snapshot/
├── selection_ordered.json
├── experiment_manifest.json
├── shared_graph_baselines/
├── group-c/
│   ├── run_summary.json
│   ├── <repo_id>/report.html 與各階段 logs
│   ├── hound-home/.hound/projects/
│   └── llm_judge/
│       ├── inputs/predictions/
│       └── benchmark_eval_native_rerun_20261023/
│           ├── manifest.json
│           ├── judge_artifact.json
│           ├── report.json
│           └── report.md
└── group-d/
    └── 與 group-c 對應的目錄結構
```

正式報告在原實驗機的 Workspace 相對位置（本次未一併上傳最新 artifacts）：

- Group C：`subscription-gateway-pilot/results/hound_24_repo_cd_latest_gt_20261022/group-c/llm_judge/benchmark_eval_native_rerun_20261023/report.md`
- Group D：`subscription-gateway-pilot/results/hound_24_repo_cd_latest_gt_20261022/group-d/llm_judge/benchmark_eval_native_rerun_20261023/report.md`
- [正式 evaluator README（固定 SCAR commit）](https://github.com/fffuuuming/prototype/blob/5cab8f68217607117f9403d2adb9481ec5d0ec10/src/benchmark_eval/README.md)

兩個 Hound repo README 內保存的 2026-10-12／13 成績是更早的 23-repo 實驗，不能與這次 24-repo／43 筆 GT 的成績混用。最近的 Hound／Judge 結果位於上述本機 workspace；本次發布說明文件不代表這批最新完整結果也已同步至 GitHub。

分享與重現需要 source repos、模型設定及自己的登入授權。報告不包含 OAuth credential、gateway bearer token 或 API key。
