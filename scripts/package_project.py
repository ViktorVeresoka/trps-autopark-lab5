"""Пакування вихідного коду без локальних налаштувань і кешу."""
from pathlib import Path
import tomllib
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    version = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    output = ROOT / "dist" / f"autopark-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    files = [ROOT / name for name in ("README.md", "pyproject.toml", ".gitignore")]
    for directory in ("src", "tests", "docs", "scripts", ".github/workflows"):
        files.extend(path for path in (ROOT / directory).rglob("*")
                     if path.is_file() and "__pycache__" not in path.parts
                     and path.suffix != ".pyc")
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(f"Created {output.name}: {len(files)} files")


if __name__ == "__main__":
    main()
