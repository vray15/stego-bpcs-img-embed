# 🖼️ BPCS Steganography

**BPCS (Bit-Plane Complexity Segmentation)** là một kỹ thuật steganography tiên tiến cho phép ẩn thông tin bí mật trong ảnh mà không gây khác biệt rõ ràng về mặt thị giác. Phương pháp này khai thác các vùng có độ phức tạp cao trong ảnh (khó nhận ra bằng mắt thường) để nhúng thông điệp mà không làm giảm chất lượng ảnh.

---

## 📘 Tài liệu tham khảo

- Kawaguchi, Eiji, and Richard O. Eason. _"Principles and applications of BPCS steganography."_ Photonics East, 1999.

---

## 🚀 Tính năng chính

- Giấu bất kỳ loại dữ liệu nào (text, ảnh, file nhị phân) vào ảnh PNG.
- Tùy chỉnh ngưỡng độ phức tạp (alpha) để kiểm soát mức độ nhúng.
- Giao diện dòng lệnh trực quan.
- Dễ dàng tích hợp dưới dạng module Python.

---

## 🔧 Cài đặt

```bash
git clone https://github.com/vray15/stego-bpcs-img-embed.git
cd stego-bpcs-img-embed
pip install -r requirements.txt
