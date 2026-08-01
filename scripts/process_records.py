#!/usr/bin/env python3
"""
Data processor for Zimbabwe Public Service Knowledge Dataset.
- Converts processed/records.jsonl to processed/records.csv
- Generates agency metadata cards in metadata/metadata_cards/
- Updates manifest.json and metadata/dataset_metadata.json
"""

import csv
import json
import os
from datetime import datetime

DATASET_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORDS_JSONL = os.path.join(DATASET_ROOT, "processed", "records.jsonl")
RECORDS_CSV = os.path.join(DATASET_ROOT, "processed", "records.csv")
INTENTS_JSONL = os.path.join(DATASET_ROOT, "labels", "multilingual_intents.jsonl")
METADATA_DIR = os.path.join(DATASET_ROOT, "metadata", "metadata_cards")
DATASET_METADATA = os.path.join(DATASET_ROOT, "metadata", "dataset_metadata.json")
MANIFEST_PATH = os.path.join(DATASET_ROOT, "manifest.json")

def process_dataset():
    print("=" * 60)
    print("RUNNING DATASET CONVERSION & PROCESSOR")
    print("=" * 60)

    if not os.path.exists(RECORDS_JSONL):
        print(f"Error: {RECORDS_JSONL} not found.")
        return

    records = []
    with open(RECORDS_JSONL, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    print(f"Read {len(records)} records from JSONL.")

    # 1. Write CSV export
    os.makedirs(os.path.dirname(RECORDS_CSV), exist_ok=True)
    fieldnames = [
        "record_id", "service", "agency", "agency_code", "category",
        "requirements", "fees_summary", "steps_summary", "processing_time",
        "source_url", "last_verified"
    ]

    with open(RECORDS_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            fees_str = "; ".join([f"{item['item']}: ${item['amount_usd']}" for item in r.get("fees", [])])
            steps_str = " | ".join(r.get("steps", []))
            reqs_str = "; ".join(r.get("requirements", []))

            writer.writerow({
                "record_id": r.get("record_id"),
                "service": r.get("service"),
                "agency": r.get("agency"),
                "agency_code": r.get("agency_code"),
                "category": r.get("category"),
                "requirements": reqs_str,
                "fees_summary": fees_str,
                "steps_summary": steps_str,
                "processing_time": r.get("processing_time"),
                "source_url": r.get("source_url"),
                "last_verified": r.get("last_verified")
            })

    print(f"Exported records to CSV: {RECORDS_CSV}")

    # 2. Group by Agency and generate Agency Metadata Cards
    os.makedirs(METADATA_DIR, exist_ok=True)
    agencies = {}
    for r in records:
        code = r.get("agency_code", "GENERIC")
        if code not in agencies:
            agencies[code] = {
                "agency_name": r.get("agency"),
                "agency_code": code,
                "records": []
            }
        agencies[code]["records"].append(r)

    for code, data in agencies.items():
        card_path = os.path.join(METADATA_DIR, f"{code.lower()}_metadata_card.json")
        card_content = {
            "agency_code": code,
            "agency_name": data["agency_name"],
            "record_count": len(data["records"]),
            "covered_services": [r["service"] for r in data["records"]],
            "last_audit_date": datetime.now().strftime("%Y-%m-%d"),
            "data_steward": "Dataprenuers / Lincoln Tinaye Rwodzi",
            "license": "CC-BY-4.0",
            "provenance_summary": "Extracted from official portal & verified with administrative office documentation."
        }
        with open(card_path, 'w', encoding='utf-8') as f:
            json.dump(card_content, f, indent=2)

    print(f"Generated {len(agencies)} agency metadata cards in {METADATA_DIR}")

    # 3. Write dataset_metadata.json
    dataset_meta = {
        "dataset_name": "Zimbabwe Public Service Knowledge & AI Benchmark Dataset",
        "version": "1.0.0-phase1",
        "description": "Multilingual AI-ready dataset of Zimbabwean government administrative procedure knowledge.",
        "maintainer": "Dataprenuers Team",
        "license": "CC-BY-4.0",
        "languages": ["en", "sn", "nd"],
        "total_records": len(records),
        "total_agencies": len(agencies),
        "agencies": list(agencies.keys()),
        "categories": list(set(r.get("category") for r in records if r.get("category"))),
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }

    with open(DATASET_METADATA, 'w', encoding='utf-8') as f:
        json.dump(dataset_meta, f, indent=2)

    # 4. Write manifest.json
    manifest = {
        "name": "zimbabwe-public-service-dataset",
        "version": "1.0.0",
        "created_at": "2026-07-14",
        "updated_at": datetime.now().strftime("%Y-%m-%d"),
        "files": {
            "records_jsonl": "processed/records.jsonl",
            "records_csv": "processed/records.csv",
            "intents_jsonl": "labels/multilingual_intents.jsonl",
            "schema_json": "schema/schema.json",
            "quality_report": "validation/quality_report.md"
        },
        "stats": {
            "record_count": len(records),
            "agency_count": len(agencies)
        }
    }

    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f"Updated manifest.json and dataset_metadata.json successfully.")

if __name__ == "__main__":
    process_dataset()
