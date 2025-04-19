from pypdf import PdfReader
import os, glob

dir = "D:\\ThinkSwiss\\RAG_pdf\\Optimized Documents"
files = glob.glob(os.path.join(dir, "*.pdf"))

for file in files:
    print(f"Reading file: {file}")
    reader = PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text(space_width=False)+"\n"
    text=" ".join(text.splitlines())

    txt_file = os.path.join("D:\\ThinkSwiss\\RAG", os.path.splitext(os.path.basename(file))[0] + ".txt")
    with open(txt_file,'w',encoding="utf-8") as f:
        f.write(text)