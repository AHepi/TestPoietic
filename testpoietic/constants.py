from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PRIMARY_SUBJECT = (
    REPOSITORY_ROOT
    / "subject"
    / "spark-poietic-layered-kernel-v1.2-purpose-guarded.md"
)
PRIMARY_SHA256 = "9c5d389afc1f334733604083710f6625638b8933825a6312c7403e7de08dafbc"

DECLARED_PARENT_HASHES = {
    "spark-poietic-layered-kernel-v1.0.md": (
        "f729870e30f825b27b6bbab4322cca9296590b8d44eb301a4e11baedc2c6cbef"
    ),
    "spark-poietic-layered-kernel-v1.1-audit-repaired.md": (
        "b0ed8e4bb69ef9604bef6554ab3805f95f0f84937a8224744042f3aa0bf2cc1c"
    ),
    "the-creativity-criticism.md": (
        "ecd07f5553d1b4e1ae8bb5be4804206c6b4ed1098efab73952543892f20719a8"
    ),
}
