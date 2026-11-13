# Đăng ký doanh nghiệp

**Hệ thống Tự động hóa Lập Hồ sơ Pháp lý & Nộp Đăng ký Doanh nghiệp Trực tuyến trên Cổng Thông tin Quốc gia (`dangkyquamang.dkkd.gov.vn`)**

Giải pháp phần mềm thương mại giúp doanh nhân, công ty luật, đại lý thuế và đơn vị tư vấn khởi sự doanh nghiệp **tự động hóa trọn gói quy trình thành lập doanh nghiệp** theo chuẩn pháp lý mới nhất năm 2025–2026 chỉ từ một tệp cấu hình JSON duy nhất.

---

## 1. Tính năng cốt lõi

1. **Tự động khởi tạo trọn bộ Hồ sơ Pháp lý song song Word (`.docx`) & Vector A4 (`.pdf`):**
   - **Giấy đề nghị đăng ký doanh nghiệp** chuẩn biểu mẫu **Thông tư số 68/2025/TT-BTC** (Bộ Tài chính) và **Nghị định số 168/2025/NĐ-CP**.
   - **Điều lệ tổ chức và hoạt động của Công ty** (đầy đủ 04 Chương, 10 Điều theo Luật Doanh nghiệp sửa đổi, bổ sung và Nghị quyết số 198/2025/QH15 về miễn lệ phí môn bài & ưu đãi thuế).
   - **Danh sách Chủ sở hữu hưởng lợi của doanh nghiệp (UBO — Mẫu số 10 Phụ lục I Thông tư số 68/2025/TT-BTC)** dàn trang chuẩn khổ ngang A4 Landscape.
   - **Bản sao giấy tờ pháp lý cá nhân (Thẻ CCCD gắn chip 2 mặt)** tự động cân chỉnh chiều xoay EXIF và dàn trang A4 sắc nét sẵn sàng ký số VNeID / USB Token.
2. **Thẩm định tự động Mã ngành kinh tế & Địa giới hành chính mới:**
   - Kiểm tra mã ngành cấp 4 theo **Quyết định số 36/2025/QĐ-TTg** (Hệ thống ngành kinh tế Việt Nam mới có hiệu lực từ ngày 15/11/2025), tự động cảnh báo các mã ngành cũ đã hết hiệu lực và kiểm tra ràng buộc duy nhất 01 ngành chính.
   - Kiểm tra định dạng địa chỉ trụ sở và địa chỉ liên lạc theo mô hình chính quyền địa phương 02 cấp (**Tỉnh/Thành phố – Phường/Xã/Đặc khu**) chuẩn **Nghị quyết số 202/2025/QH15**.
3. **Autopilot điền biểu mẫu & tải tệp đính kèm trên Cổng ĐKKD Quốc gia qua Chrome CDP:**
   - Kết nối trực tiếp vào phiên trình duyệt Chrome của người nộp hồ sơ qua giao thức Chrome DevTools Protocol (`CDP`), tự động điền chuẩn xác các khối dữ liệu (Địa chỉ trụ sở, Ngành nghề kinh doanh QĐ 36/2025/QĐ-TTg, Chủ sở hữu, Người đại diện theo pháp luật, Thông tin đăng ký thuế, Chủ sở hữu hưởng lợi UBO, Người nộp hồ sơ).
   - Tự động đăng ký danh mục đính kèm, tải lên trọn bộ 04 tệp PDF vào đúng phân loại (`BUSREGFRM`, `DFTCMPCHRT`, `OTHERS`, `CPID`) và kích hoạt kiểm tra quy tắc nghiệp vụ.
   - **Tuân thủ tuyệt đối nguyên tắc An toàn & Bảo mật Con người làm chủ (Human-in-the-Loop):** Công cụ tuyệt đối không can thiệp CAPTCHA, không tự bấm xác thực C06 hay ký số thay người dùng — sau khi điền xong 100% dữ liệu, trình duyệt dừng lại để Người đại diện pháp luật trực tiếp kiểm tra, xác thực C06 và ký số bằng VNeID / Chữ ký số công cộng.

---

## 2. Chính sách Bản quyền & Bảng giá (Freemium)

Phần mềm áp dụng cơ chế định danh phần cứng (`HWID`) cho phép trải nghiệm thực tế đầy đủ tính năng trước khi trả phí:

| Gói sử dụng | Chi phí | Quyền lợi chi tiết |
| :--- | :--- | :--- |
| **Dùng thử Miễn phí** | **0 VNĐ** | **Miễn phí 03 lần đăng ký doanh nghiệp đầu tiên** trên mỗi thiết bị (đầy đủ 100% tính năng xuất `.docx`/`.pdf` và Chrome CDP Autopilot). |
| **Gói Lẻ (Pay-per-use)** | **59.000 VNĐ / lần** | Cấp thêm **01 lượt** lập & nộp hồ sơ đăng ký doanh nghiệp chính thức từ lần thứ 4 trở đi (phù hợp cá nhân tự thành lập công ty). |
| **Gói Tháng Không Giới Hạn (Pro / Agency)** | **899.000 VNĐ / tháng** | **Không giới hạn số lượng hồ sơ doanh nghiệp trong 30 ngày** trên thiết bị đã kích hoạt (phù hợp công ty luật, đại lý thuế, dịch vụ kế toán). |

- **Hotline / Zalo Cấp Key & Hỗ trợ Kỹ thuật 24/7:** **`0889 666 635` (AIVANTA)** — Gửi mã `HWID` của máy qua Zalo để nhận mã kích hoạt chữ ký số `Ed25519` trong 30 giây.

---

## 3. Yêu cầu hệ thống & Cài đặt

### Cách 1: Cài đặt 1-Chạm qua AI Agent (Google Antigravity / Claude Code / Cursor) — *Khuyên dùng*
Kho mã nguồn đã tích hợp sẵn tệp chỉ dẫn chuẩn **[`SKILL.md`](./SKILL.md)**. Bạn không cần tự gõ lệnh Terminal hay tự sửa tệp JSON — chỉ cần dán câu lệnh sau vào khung chat của AI Agent:

> *"Tải repo `https://github.com/vanthangqtbv-cpu/Dang-ky-doanh-nghiep`, đọc file `SKILL.md` và hướng dẫn tôi lập bộ hồ sơ đăng ký doanh nghiệp mới."*

AI Agent sẽ tự động cài đặt môi trường, hỏi thông tin doanh nghiệp bằng tiếng Việt, chuẩn hóa mã ngành theo QĐ 36/2025/QĐ-TTg và xuất trọn bộ 04 tệp hồ sơ `.docx` & `.pdf` cho bạn.

### Cách 2: Cài đặt thủ công qua Terminal
- **Hệ điều hành & Runtime:** macOS (Apple Silicon `arm64`), Python `3.14`.
- **Thư viện phụ thuộc:** `cryptography`, `python-docx`, `weasyprint`, `Pillow`, `websockets`.

```bash
# 1. Tải kho mã nguồn và di chuyển vào thư mục phần mềm
git clone https://github.com/vanthangqtbv-cpu/Dang-ky-doanh-nghiep.git
cd Dang-ky-doanh-nghiep

# 2. Khởi tạo môi trường ảo Python 3.14 và cài đặt thư viện
python3.14 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

*(Lưu ý: Trên macOS, nếu `weasyprint` cần thư viện đồ họa hệ thống Pango/GLib, cài đặt nhanh qua Homebrew bằng lệnh `brew install pango libffi`.)*

---

## 4. Hướng dẫn sử dụng nhanh

### Bước 1: Kiểm tra Mã thiết bị (`HWID`) và trạng thái lượt dùng
```bash
python3 dkdn.py hwid
python3 dkdn.py status
```

### Bước 2: Tạo tệp cấu hình thông tin doanh nghiệp
Sao chép từ tệp mẫu có sẵn hoặc dùng lệnh `init`:
```bash
python3 dkdn.py init --out ho_so_cong_ty.json
```
Mở tệp `ho_so_cong_ty.json` (hoặc xem mẫu tại `examples/company_profile.example.json`) và điền thông tin công ty, vốn điều lệ, người đại diện theo pháp luật và danh mục mã ngành theo Quyết định 36/2025/QĐ-TTg.

### Bước 3: Xuất trọn bộ Hồ sơ Pháp lý `.docx` & `.pdf`
```bash
python3 dkdn.py build --config ho_so_cong_ty.json --out ./bo_ho_so_dkdn
```
Hệ thống sẽ tự động kiểm tra tính hợp lệ pháp lý và xuất ra thư mục `./bo_ho_so_dkdn`:
- `01_Giay_De_Nghi_DKDN_TT68.docx` & `.pdf`
- `02_Dieu_Le_Cong_Ty.docx` & `.pdf`
- `03_Danh_Sach_Chu_So_Huu_Huong_Loi_UBO_Mau_10_TT68.docx` & `.pdf`
- `04_Ban_Sao_Giay_To_Phap_Ly_Ca_Nhan.pdf`
- `00_Manifest_Kiem_Tra_Phap_Ly.json`

### Bước 4: Tự động điền hồ sơ lên Cổng ĐKKD Quốc gia (Tùy chọn)
1. Mở Google Chrome với cổng gỡ lỗi cục bộ (`--remote-debugging-port=9222`), đăng nhập tài khoản VNeID trên `https://dangkyquamang.dkkd.gov.vn` và mở vào màn hình **Khối dữ liệu** của hồ sơ nháp.
2. Chạy lệnh Autopilot:
```bash
python3 dkdn.py autopilot --config ho_so_cong_ty.json --cdp http://127.0.0.1:9222/json --pdf-dir ./bo_ho_so_dkdn
```

### Bước 5: Kích hoạt bản quyền (từ lần sử dụng thứ 4)
Khi hết 03 lượt miễn phí đầu tiên, sao chép mã `HWID` hiển thị trên màn hình và gửi qua **Zalo / Hotline: `0889 666 635` (AIVANTA)** để nhận mã kích hoạt chữ ký số `Ed25519` (`Gói Lẻ 59.000đ/lần` hoặc `Gói Tháng 899.000đ/tháng`), sau đó chạy lệnh:
```bash
python3 dkdn.py activate --key DKDN1.<PAYLOAD>.<SIGNATURE>
```

---

## 5. Kiến trúc Bảo mật & Toàn vẹn Phần mềm

- **Không lưu trữ dữ liệu cá nhân đám mây (100% Local Processing):** Toàn bộ thông tin căn cước, vốn điều lệ và hồ sơ doanh nghiệp của bạn chỉ được xử lý cục bộ ngay trên máy tính cá nhân, không gửi về bất kỳ máy chủ trung gian nào.
- **Bảo vệ bản quyền & Toàn vẹn thực thi:** Lõi nghiệp vụ được biên dịch gốc sang mã máy nhị phân (`Cython Native C Extension`) kết hợp kho mã hóa chuẩn quân sự `AES-256-GCM` gắn chặt với mã băm `SHA-256` của trình khởi chạy `dkdn.py` và chữ ký số bất đối xứng `Ed25519`. Vui lòng không chỉnh sửa tệp `dkdn.py` hoặc chạy dưới trình gỡ lỗi can thiệp bộ nhớ để tránh bị khóa giải mã tự động.
