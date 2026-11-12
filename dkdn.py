#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DKDN Pro CLI — Hệ thống Tự động hóa Hồ sơ Pháp lý & Nộp Đăng ký Doanh nghiệp Quốc gia.
Tệp khởi chạy mỏng (Thin Launcher) được bảo vệ toàn vẹn bằng chữ ký băm SHA-256.
Mọi chỉnh sửa trái phép đối với tệp này sẽ vô hiệu hóa khóa giải mã AES-256-GCM của lõi thực thi.
"""

import os
import sys


def _bootstrap() -> int:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    try:
        from dkdn_core import _guard_engine
    except ImportError as exc:
        sys.stderr.write(
            "[DKDN] Không thể nạp mô-đun nhân bảo mật nhị phân (dkdn_core._guard_engine).\n"
            f"Chi tiết kỹ thuật: {exc}\n"
            "Vui lòng chạy trên môi trường Python 3.14 (macOS Apple Silicon arm64) đã cài đặt đầy đủ requirements.txt.\n"
        )
        return 1
    return int(_guard_engine.run_cli(sys.argv[1:], os.path.abspath(__file__)))


if __name__ == "__main__":
    raise SystemExit(_bootstrap())
