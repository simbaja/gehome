"""Clean, build, validate, and upload gehomesdk distributions via twine."""

import argparse
from importlib.util import find_spec
from pathlib import Path
import shutil
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent


def clean_build_artifacts(repo_root: Path) -> None:
    """Remove stale distribution, build, and egg-info directories."""
    for folder_name in ("dist", "build"):
        target = repo_root / folder_name
        if target.exists():
            print(f"Removing {target}...")
            shutil.rmtree(target)

    for egg_info in repo_root.glob("*.egg-info"):
        if egg_info.is_dir():
            print(f"Removing {egg_info}...")
            shutil.rmtree(egg_info)


def run_command(args: list[str], cwd: Path) -> None:
    """Run a subprocess command and raise on non-zero exit."""
    print(f"Running: {' '.join(args)}")
    subprocess.run(args, cwd=cwd, check=True)


def build_distributions(repo_root: Path) -> list[str]:
    """Build sdist and wheel distributions and return their paths."""
    if find_spec("build") is not None:
        run_command([sys.executable, "-m", "build"], cwd=repo_root)
    else:
        run_command(
            [sys.executable, "setup.py", "sdist", "bdist_wheel"],
            cwd=repo_root,
        )

    dist_dir = repo_root / "dist"
    artifacts = sorted(str(p) for p in dist_dir.iterdir() if p.is_file())
    if not artifacts:
        raise RuntimeError("No distribution files were produced in dist/.")
    return artifacts


def main(argv: list[str] | None = None) -> int:
    """Clean stale artifacts, build package distributions, check, and upload."""
    parser = argparse.ArgumentParser(
        description="Clean dist/build artifacts, build gehomesdk, and upload via twine."
    )
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Clean, build, and run twine check without uploading.",
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="Optional twine repository name (e.g. testpypi).",
    )
    args = parser.parse_args(argv)

    clean_build_artifacts(REPO_ROOT)
    artifacts = build_distributions(REPO_ROOT)

    run_command([sys.executable, "-m", "twine", "check", *artifacts], cwd=REPO_ROOT)

    if args.build_only:
        print("Build and twine check succeeded (--build-only set; skipping upload).")
        return 0

    upload_cmd = [sys.executable, "-m", "twine", "upload"]
    if args.repository:
        upload_cmd.extend(["--repository", args.repository])
    upload_cmd.extend(artifacts)
    run_command(upload_cmd, cwd=REPO_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
