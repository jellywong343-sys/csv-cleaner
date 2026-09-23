from __future__ import annotations
import argparse,csv
from pathlib import Path

def clean_csv(source:Path,destination:Path,drop_empty=True,deduplicate=True,encoding="utf-8-sig"):
 sample=source.read_text(encoding=encoding)[:8192]
 try: dialect=csv.Sniffer().sniff(sample,delimiters=",;\t|")
 except csv.Error: dialect=csv.excel
 rows_read=rows_written=empty_removed=duplicates_removed=0; seen=set()
 with source.open("r",encoding=encoding,newline="") as src,destination.open("w",encoding="utf-8",newline="") as dst:
  reader=csv.reader(src,dialect); writer=csv.writer(dst,dialect)
  for row in reader:
   rows_read+=1; cleaned=tuple(cell.strip() for cell in row)
   if drop_empty and not any(cleaned): empty_removed+=1; continue
   if deduplicate and cleaned in seen: duplicates_removed+=1; continue
   seen.add(cleaned); writer.writerow(cleaned); rows_written+=1
 return {"rows_read":rows_read,"rows_written":rows_written,"empty_rows_removed":empty_removed,"duplicates_removed":duplicates_removed}

def main():
 parser=argparse.ArgumentParser(description="Clean whitespace, empty rows, and duplicate CSV rows."); parser.add_argument("source"); parser.add_argument("destination")
 parser.add_argument("--keep-empty",action="store_true"); parser.add_argument("--keep-duplicates",action="store_true"); parser.add_argument("--encoding",default="utf-8-sig"); args=parser.parse_args()
 report=clean_csv(Path(args.source),Path(args.destination),not args.keep_empty,not args.keep_duplicates,args.encoding)
 for key,value in report.items(): print(f"{key.replace('_',' ').title()}: {value}")
if __name__ == "__main__": main()
