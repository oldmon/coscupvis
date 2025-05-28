# coscup-data-analysis 專案說明

這個專案旨在從 COSCUP 的議程數據中進行社群與技術趨勢分析。專案的主要目標是探索不同主題之間的關聯性，並找出在 2020 至 2024 年間活躍的講者。

## 專案結構

- `src/data/raw/sessions/`：包含 2020 至 2024 年 COSCUP 議程的原始數據（JSON 格式）。
- `src/data/processed/`：包含處理後的數據：
  - `speakers.csv`：講者的相關信息。
  - `topics.csv`：主題的關鍵字及其出現次數。
  - `sessions.csv`：各議程的詳細信息。
- `src/scripts/`：包含數據處理和分析的腳本：
  - `fetch_data.py`：從指定的 URL 下載原始數據。
  - `process_data.py`：處理原始數據並生成 CSV 文件。
  - `analyze.py`：分析處理後的數據。
- `src/utils/`：包含輔助函數的腳本，用於數據處理和分析。
- `requirements.txt`：列出專案所需的 Python 庫及其版本。
- `.gitignore`：指定在版本控制中忽略的檔案和資料夾。

## 使用指南

1. 確保已安裝 Python 和相關依賴庫。
2. 使用 `fetch_data.py` 下載原始數據。
3. 使用 `process_data.py` 處理數據並生成 CSV 文件。
4. 使用 `analyze.py` 進行數據分析。

## 貢獻

歡迎任何形式的貢獻，請提出問題或提交拉取請求。