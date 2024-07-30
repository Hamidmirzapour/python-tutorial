from pathlib import Path

ecommerce_path = Path("ecommerce")
email_path = Path("Email")

print(ecommerce_path.exists())
email_path.mkdir()
email_path.rmdir()

for pyfile in ecommerce_path.glob("*.py"):
    print(pyfile)