from pyprojroot import here


qmds = [p for p in here().glob("**/*.qmd")]

# Replace triple line breaks with double line breaks
for qmd in qmds:
    with open(qmd, "r") as f:
        text = f.read()
    text = text.replace("\n\n\n", "\n\n")
    with open(qmd, "w") as f:
        f.write(text)
