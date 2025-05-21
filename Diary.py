from datetime import datetime

text = input("What happened today?: ")
docname = datetime.now().strftime("%Y-%m-%d")

with open(docname, "w") as doc:
    doc.write(f"{docname}: {text}\n")

print("Done! The text has been saved")
