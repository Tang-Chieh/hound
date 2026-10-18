# Hound C/D 實驗結果：gpt-5.6-luna

本目錄保存已完成的最新 C、D 實驗。`main` 與 `general-auditing` 分支都提供兩組完整結果，方便比較；結果不會因目前 checkout 的分支而改變。

| 設定 | Group C | Group D |
|---|---|---|
| 分析範圍 | General auditing | Price manipulation |
| Hound model | `openai-codex/gpt-5.6-luna` | 同左 |
| Judge model | `gpt-5.6-luna` | 同左 |
| Repo 數 | 23 | 23 |
| Ground Truth findings | 25 | 25 |
| Mission | 無 | 無 |
| 執行上限 | 每 investigation 最多 5 iterations；每 repo audit 最多 30 分鐘 | 同左 |
| Graph／manifest | 重用同一批既有輸入，未重新建圖 | 同左 |
| Findings 格式 | Hound 直接輸出 PredictionCase | 同左 |
| Predictions | 118 | 38 |
| Pooled soft precision | 0.0288 | 0.1750 |
| Pooled soft recall | 0.1360 | 0.2660 |
| Macro soft F1 | 0.0411 | 0.1574 |
| Pooled soft F1 | 0.0476 | 0.2111 |

## 報告與 artifacts

| 內容 | Group C | Group D |
|---|---|---|
| 完整結果 | [results](group-c/results/) | [results](group-d/results/) |
| 執行摘要 | [run_summary.json](group-c/results/run_summary.json) | [run_summary.json](group-d/results/run_summary.json) |
| PredictionCase | [23 份 JSON](group-c/results/prediction_cases/) | [23 份 JSON](group-d/results/prediction_cases/) |
| Judge Markdown report | [report.md](group-c/results/llm_judge/benchmark_eval_scar_6022_20261013/report.md) | [report.md](group-d/results/llm_judge/benchmark_eval_scar_6022_20261012/report.md) |
| Judge JSON report | [report.json](group-c/results/llm_judge/benchmark_eval_scar_6022_20261013/report.json) | [report.json](group-d/results/llm_judge/benchmark_eval_scar_6022_20261012/report.json) |
| Pairwise scores | [judge_artifact.json](group-c/results/llm_judge/benchmark_eval_scar_6022_20261013/judge_artifact.json) | [judge_artifact.json](group-d/results/llm_judge/benchmark_eval_scar_6022_20261012/judge_artifact.json) |
| Evaluation inputs | [manifest.json](group-c/results/llm_judge/benchmark_eval_scar_6022_20261013/manifest.json) | [manifest.json](group-d/results/llm_judge/benchmark_eval_scar_6022_20261012/manifest.json) |

各 repo 目錄保留原生 `report.html` 和 stage logs；`hound-home/` 保留此次保存的 project／hypotheses／graph／manifest 資料。Evaluation manifest 包含此次評估的 Ground Truth 文字，屬於完整評估 artifacts 的一部分。檔案原樣取自 Private 整合實驗 repo 的保存結果，沒有重新跑模型或修改評分。

這些是當時使用的 Hound snapshots 所產生的歷史結果，不代表本次 fork 提交重新執行了全部 46 次 audit。LLM 再次產生的 findings／評分可能不同。Soft metrics 也不是二元完全命中率。

LLM Judge 執行程式、獨立 Ground Truth dataset 與完整重現說明，請見 [Private 整合 repo](https://github.com/Tang-Chieh/Hound_price_manipulation_experiments)。本目錄不包含 OAuth credentials 或 gateway bearer tokens。
