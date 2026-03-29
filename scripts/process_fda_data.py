#!/usr/bin/env python3
"""處理沙烏地阿拉伯 SFDA 藥品資料

從 SFDA 開放資料入口下載已註冊藥品 Excel 並轉換為 JSON 格式。

SFDA 在其開放資料頁面提供本地與非本地人用藥品的 Excel 清單。
本腳本自動下載兩個清單並合併。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    SFDA Open Data: https://www.sfda.gov.sa/en/open-data
    - Local Human Medicines List 2023 (.xlsx)
    - Non-Local Human Medicines List 2023 (.xlsx)
    SFDA Developer Portal API (需 OAuth): https://developer.sfda.gov.sa/

產生檔案:
    data/raw/sa_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_sfda_data(raw_dir: Path) -> list[Path]:
    """從 SFDA 開放資料入口下載藥品清單 Excel

    SFDA 在 sfda.gov.sa/en/open-data 提供 2023 年度的本地與非本地
    人用藥品 Excel 清單。

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        成功下載的檔案路徑列表
    """
    # SFDA 開放資料 - 已驗證可下載的 URL (2026-03 測試通過)
    download_list = [
        {
            "name": "SFDA Local Human Medicines 2023",
            "url": "https://www.sfda.gov.sa/sites/default/files/2023-10/"
                   "\u0642\u0627\u0626\u0645\u0629-\u0627\u0644\u0623\u062f\u0648"
                   "\u064a\u0629-\u0627\u0644\u0628\u0634\u0631\u064a\u0629-"
                   "\u0627\u0644\u0645\u062d\u0644\u064a\u0629-\u0627\u0644\u0645"
                   "\u0633\u062c\u0644\u0629-2023\u0645.xlsx",
            "filename": "sfda_local_human_medicines_2023.xlsx",
        },
        {
            "name": "SFDA Non-Local Human Medicines 2023",
            "url": "https://www.sfda.gov.sa/sites/default/files/2023-10/"
                   "\u0642\u0627\u0626\u0645\u0629-\u0627\u0644\u0623\u062f\u0648"
                   "\u064a\u0629-\u0627\u0644\u0628\u0634\u0631\u064a\u0629-"
                   "\u0627\u0644\u063a\u064a\u0631-\u0645\u062d\u0644\u064a\u0629-"
                   "\u0627\u0644\u0645\u0633\u062c\u0644\u0629-2023\u0645.xlsx",
            "filename": "sfda_nonlocal_human_medicines_2023.xlsx",
        },
    ]

    raw_dir.mkdir(parents=True, exist_ok=True)
    downloaded = []

    for item in download_list:
        output_path = raw_dir / item["filename"]
        print(f"正在下載: {item['name']}")
        print(f"  URL: {item['url'][:80]}...")

        try:
            response = requests.get(item["url"], timeout=120, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0",
            })
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "html" in content_type.lower():
                print(f"  返回 HTML 頁面，非 Excel 檔案，跳過")
                continue

            with open(output_path, "wb") as f:
                f.write(response.content)

            size_kb = output_path.stat().st_size / 1024
            print(f"  下載完成: {output_path.name} ({size_kb:.0f} KB)")

            if size_kb < 1:
                print(f"  檔案過小，可能無效")
                output_path.unlink(missing_ok=True)
                continue

            downloaded.append(output_path)

        except requests.RequestException as e:
            print(f"  下載失敗: {e}")
            continue

    if not downloaded:
        raise FileNotFoundError(
            f"無法自動下載 SFDA 藥品清單\n\n"
            f"請手動取得資料：\n\n"
            f"方法 A: SFDA 開放資料頁面\n"
            f"  1. 前往 https://www.sfda.gov.sa/en/open-data\n"
            f"  2. 下載 'Local Human Medicines List' 和 'Non-Local Human Medicines List'\n"
            f"  3. 將 Excel 檔案放置於: {raw_dir}/\n\n"
            f"方法 B: SFDA Developer Portal API\n"
            f"  1. 前往 https://developer.sfda.gov.sa/get-start\n"
            f"  2. 註冊帳號並建立應用程式\n"
            f"  3. 使用 Registered Drug Service API\n\n"
            f"支援格式: .xlsx, .xls, .csv"
        )

    return downloaded


def find_data_files(raw_dir: Path) -> list[Path]:
    """在 raw 目錄中尋找已存在的 SFDA 資料檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的資料檔案路徑列表
    """
    patterns = [
        "sfda*.xlsx", "sfda*.xls", "sfda*.csv",
        "SFDA*.xlsx", "SFDA*.xls", "SFDA*.csv",
        "*medicines*.xlsx", "*drugs*.xlsx",
    ]

    files = []
    seen = set()
    for pattern in patterns:
        for f in raw_dir.glob(pattern):
            if f not in seen:
                files.append(f)
                seen.add(f)

    return files


def process_sfda_excels(excel_paths: list[Path], output_path: Path) -> Path:
    """處理 SFDA Excel 檔案並轉換為 JSON

    讀取一或多個 SFDA Excel 檔案，合併後輸出。

    SFDA Excel 欄位:
        TradeName, ScientificName, Size, SizeUnit,
        DrugType, DrugTypeAr, LegalStatus, LegalStatusAr,
        Manufacturer_Name, Manufacturer_Country

    Args:
        excel_paths: Excel 檔案路徑列表
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    all_dfs = []

    for excel_path in excel_paths:
        print(f"\n讀取: {excel_path.name}")
        print(f"  大小: {excel_path.stat().st_size / 1024:.0f} KB")

        suffix = excel_path.suffix.lower()

        if suffix == ".csv":
            try:
                df = pd.read_csv(excel_path, encoding="utf-8", dtype=str, on_bad_lines="skip")
            except UnicodeDecodeError:
                df = pd.read_csv(excel_path, encoding="cp1256", dtype=str, on_bad_lines="skip")
        elif suffix in (".xlsx", ".xls"):
            try:
                df = pd.read_excel(excel_path, engine="openpyxl", dtype=str, sheet_name=0)
            except Exception:
                df = pd.read_excel(excel_path, dtype=str, sheet_name=0)
        else:
            print(f"  不支援的格式: {suffix}，跳過")
            continue

        print(f"  筆數: {len(df)}")
        print(f"  欄位: {', '.join(df.columns.tolist())}")

        # 標記來源（本地/非本地）
        if "local" in excel_path.name.lower() and "non" not in excel_path.name.lower():
            df["_source"] = "Local"
        elif "non" in excel_path.name.lower():
            df["_source"] = "Non-Local"
        else:
            df["_source"] = "Unknown"

        all_dfs.append(df)

    if not all_dfs:
        raise ValueError("無法讀取任何 SFDA 資料檔案")

    # 合併所有資料
    df = pd.concat(all_dfs, ignore_index=True)
    print(f"\n合併後總筆數: {len(df)}")

    # 標準化欄位名稱
    # SFDA 欄位 → 標準欄位映射
    column_renames = {
        "TradeName": "Trade Name English",
        "ScientificName": "Active Ingredient",
        "DrugType": "Drug Type",
        "LegalStatus": "Legal Status",
        "Manufacturer_Name": "Marketing Company",
        "Manufacturer_Country": "Country of Origin",
    }

    for old_name, new_name in column_renames.items():
        if old_name in df.columns:
            df[new_name] = df[old_name]

    # 建立 Status 欄位（所有 SFDA 開放資料中的藥品都是已註冊的）
    df["Status"] = "Registered"

    # 清理資料
    df = df.fillna("")

    # 去除完全重複的行
    original_count = len(df)
    df = df.drop_duplicates(subset=["TradeName", "ScientificName", "Manufacturer_Name"], keep="first")
    if len(df) < original_count:
        print(f"去除重複後: {len(df)} (移除 {original_count - len(df)} 筆重複)")

    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    # 來源分布
    if "_source" in df.columns:
        print(f"\n來源分布:")
        source_counts = df["_source"].value_counts()
        for source, count in source_counts.items():
            print(f"  {source}: {count:,}")

    # 藥品類型分布
    for col_name in ["DrugType", "Drug Type"]:
        if col_name in df.columns:
            print(f"\n藥品類型分布:")
            type_counts = df[col_name].value_counts()
            for dtype, count in type_counts.items():
                if dtype:
                    print(f"  {dtype}: {count:,}")
            break

    # 法律狀態分布
    for col_name in ["LegalStatus", "Legal Status"]:
        if col_name in df.columns:
            print(f"\n法律狀態分布:")
            status_counts = df[col_name].value_counts()
            for status, count in status_counts.items():
                if status:
                    print(f"  {status}: {count:,}")
            break

    # 製造商國家分布
    for col_name in ["Manufacturer_Country", "Country of Origin"]:
        if col_name in df.columns:
            print(f"\n製造商國家 (前 10):")
            country_counts = df[col_name].value_counts().head(10)
            for country, count in country_counts.items():
                if country:
                    print(f"  {country}: {count:,}")
            break

    # 活性成分統計
    for col_name in ["ScientificName", "Active Ingredient"]:
        if col_name in df.columns:
            with_ingredients = (df[col_name] != "").sum()
            unique_ingredients = df[col_name][df[col_name] != ""].nunique()
            if len(df) > 0:
                print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")
                print(f"不重複成分數: {unique_ingredients:,}")
            break


def main():
    print("=" * 60)
    print("處理沙烏地阿拉伯 SFDA 藥品資料")
    print("=" * 60)
    print()
    print("資料來源: SFDA 開放資料入口 (sfda.gov.sa/en/open-data)")
    print("  - Local Human Medicines List 2023")
    print("  - Non-Local Human Medicines List 2023")
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "sa_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已下載的 Excel/CSV
    existing_files = find_data_files(raw_dir)
    if existing_files:
        print(f"使用已存在的資料檔案:")
        for f in existing_files:
            print(f"  - {f.name}")
        excel_paths = existing_files
    else:
        # 自動下載
        excel_paths = download_sfda_data(raw_dir)

    # 處理 Excel 檔案
    process_sfda_excels(excel_paths, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
