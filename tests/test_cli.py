import csv,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from csv_cleaner.cli import clean_csv
class Tests(unittest.TestCase):
 def test_clean(self):
  with tempfile.TemporaryDirectory() as tmp:
   source=Path(tmp)/"source.csv"; target=Path(tmp)/"target.csv"
   source.write_text("name,city\n Alice , Shanghai \n\nAlice,Shanghai\n",encoding="utf-8")
   report=clean_csv(source,target,encoding="utf-8"); self.assertEqual(report["rows_written"],2)
   with target.open(encoding="utf-8") as handle: rows=list(csv.reader(handle))
   self.assertEqual(rows[1],["Alice","Shanghai"])
if __name__ == "__main__": unittest.main()
