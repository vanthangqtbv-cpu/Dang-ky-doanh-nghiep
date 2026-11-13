---
name: dang-ky-doanh-nghiep
description: Tự động hóa lập trọn bộ Hồ sơ Pháp lý thành lập doanh nghiệp (.docx & .pdf chuẩn Thông tư 68/2025/TT-BTC, Nghị định 168/2025/NĐ-CP, Mã ngành QĐ 36/2025/QĐ-TTg, Địa giới 2 cấp NQ 202/2025/QH15, Mẫu UBO số 10) và tự động điền biểu mẫu trực tuyến trên Cổng Đăng ký doanh nghiệp Quốc gia (dangkyquamang.dkkd.gov.vn). Kích hoạt khi người dùng muốn thành lập công ty, soạn hồ sơ đăng ký kinh doanh, điều lệ công ty, danh sách chủ sở hữu hưởng lợi UBO hoặc nộp hồ sơ ĐKKD qua mạng.
---

# Skill: Tự Động Hóa Đăng Ký Doanh Nghiệp (`dang-ky-doanh-nghiep`)

Skill này giúp AI Agent (Google Antigravity, Claude Code, Cursor) tự động hóa trọn gói quy trình lập hồ sơ pháp lý và điền biểu mẫu đăng ký thành lập doanh nghiệp trên Cổng thông tin quốc gia về đăng ký doanh nghiệp (`https://dangkyquamang.dkkd.gov.vn`) thông qua bộ công cụ `dkdn.py`.

---

## 1. Quy Trình Thực Thi Dành Cho AI Agent

Khi người dùng yêu cầu lập hồ sơ thành lập công ty hoặc nộp hồ sơ đăng ký doanh nghiệp:

### Bước 1: Kiểm tra môi trường & Trạng thái bản quyền (`HWID`)
1. Kiểm tra thư mục cài đặt repo `Dang-ky-doanh-nghiep` và khởi tạo môi trường ảo Python `3.14` nếu chưa có:
   ```bash
   python3.14 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```
2. Kiểm tra mã thiết bị (`HWID`) và số lượt dùng thử miễn phí còn lại:
   ```bash
   .venv/bin/python3 dkdn.py status
   ```
   - Phần mềm tặng **03 lượt đăng ký doanh nghiệp đầu tiên hoàn toàn miễn phí (0 VNĐ)** trên mỗi thiết bị.
   - Nếu thiết bị đã hết 03 lượt miễn phí, chạy lệnh `.venv/bin/python3 dkdn.py hwid`, hiển thị mã `HWID` cho người dùng và hướng dẫn liên hệ **Hotline / Zalo cấp Key tự động: `0889 666 635` (AIVANTA)** để nhận mã kích hoạt (`Gói Lẻ: 59.000 VNĐ/lần` hoặc `Gói Tháng Không Giới Hạn: 899.000 VNĐ/tháng`), sau đó kích hoạt bằng:
     ```bash
     .venv/bin/python3 dkdn.py activate --key <MA_KEY_ED25519>
     ```

### Bước 2: Thu thập thông tin & Chuẩn hóa Pháp lý 2025–2026
AI Agent hỗ trợ người dùng chuẩn hóa thông tin và tạo tệp cấu hình `.json` theo cấu trúc tại `examples/company_profile.example.json` với 3 quy tắc bắt buộc:
1. **Địa giới hành chính 02 cấp (Nghị quyết 202/2025/QH15):**
   - Địa chỉ trụ sở chính (`headquarters.full_address`) và địa chỉ thường trú/liên lạc chỉ gồm: `Số nhà/Đường, Phường/Xã/Đặc khu, Tỉnh/Thành phố, Việt Nam` (tuyệt đối không ghi Quận/Huyện/Thị xã cũ).
2. **Hệ thống ngành kinh tế Việt Nam mới (Quyết định 36/2025/QĐ-TTg hiệu lực từ 15/11/2025):**
   - Áp mã ngành cấp 4 (4 chữ số) chuẩn QĐ 36/2025/QĐ-TTg (ví dụ: không dùng các mã cũ đã bãi bỏ như `6201`, `6202`, `6209`, `6311`, `6312`, `4651`; thay bằng `6219`, `6220`, `6310`, `5829`, `4650`...).
   - Chỉ chọn duy nhất **01 ngành kinh doanh chính** (`"is_main": true`).
3. **Thông tin Chủ sở hữu / Người đại diện theo pháp luật & Ảnh CCCD:**
   - Điền đầy đủ Họ tên IN HOA, ngày sinh, số CCCD 12 số, ngày cấp, nơi cấp và đường dẫn ảnh chụp 2 mặt thẻ CCCD (`cccd_front_image`, `cccd_back_image`) để phần mềm tự động dàn trang PDF A4.

### Bước 3: Xuất trọn bộ 04 Hồ sơ Pháp lý (`.docx` & `.pdf` Vector A4)
Chạy lệnh xuất hồ sơ:
```bash
.venv/bin/python3 dkdn.py build --config <duong_dan_file.json> --out ./bo_ho_so_dkdn
```
Bộ hồ sơ xuất ra tại `./bo_ho_so_dkdn` gồm:
- `01_Giay_De_Nghi_DKDN_TT68.docx` & `.pdf` *(Mẫu số 2 Phụ lục I Thông tư 68/2025/TT-BTC)*
- `02_Dieu_Le_Cong_Ty.docx` & `.pdf` *(Đầy đủ 04 Chương, 10 Điều chuẩn Luật Doanh nghiệp)*
- `03_Danh_Sach_Chu_So_Huu_Huong_Loi_UBO_Mau_10_TT68.docx` & `.pdf` *(Mẫu số 10 Phụ lục I TT 68/2025/TT-BTC khổ ngang A4 Landscape)*
- `04_Ban_Sao_Giay_To_Phap_Ly_Ca_Nhan.pdf` *(CCCD 2 mặt dàn trang A4)*

### Bước 4: Tự động điền biểu mẫu & Đính kèm tệp lên Cổng ĐKKD Quốc gia (Human-in-the-Loop)
1. Hướng dẫn người dùng mở trình duyệt Google Chrome với cổng kết nối cục bộ (`--remote-debugging-port=9222`), đăng nhập VNeID vào `https://dangkyquamang.dkkd.gov.vn` và mở màn hình **Khối dữ liệu** của hồ sơ đăng ký mới.
2. Chạy lệnh Autopilot:
   ```bash
   .venv/bin/python3 dkdn.py autopilot --config <duong_dan_file.json> --cdp http://127.0.0.1:9222/json --pdf-dir ./bo_ho_so_dkdn
   ```
3. **Nguyên tắc An toàn Con người làm chủ (Human-in-the-Loop):**
   - Tuyệt đối không giải/vượt CAPTCHA, không tự bấm xác thực C06 hay ký số thay người dùng.
   - Sau khi `dkdn.py autopilot` điền xong 100% các khối dữ liệu và đính kèm đủ 04 tệp PDF, thông báo để Người đại diện theo pháp luật trực tiếp kiểm tra lại trên màn hình trình duyệt, bấm xác thực C06, nhập mã kiểm tra và ký số nộp hồ sơ.

---

## 2. Hỗ Trợ Kỹ Thuật & Cấp Bản Quyền (License Key)
- **Đơn vị phát triển:** **AIVANTA**
- **Hotline / Zalo hỗ trợ & cấp Key 24/7:** **`0889 666 635`**
- **Chính sách giá:**
  - **03 lượt đầu tiên:** **Miễn phí 100% (`0 VNĐ`)**
  - **Gói Lẻ (từ lần thứ 4):** **`59.000 VNĐ / lần`**
  - **Gói Tháng Không Giới Hạn (Đại lý thuế / Công ty Luật / Dịch vụ Kế toán):** **`899.000 VNĐ / tháng`**
