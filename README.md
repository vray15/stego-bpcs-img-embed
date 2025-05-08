✍️ Bước 1: Copy nội dung sau (toàn bộ Markdown đã mình viết ở trên)
Bạn có thể copy từ đây:

<details> <summary>Click để hiện nội dung README.md</summary>
markdown
# 🖼️ BPCS Steganography

BPCS (Bit-Plane Complexity Segmentation) là một kỹ thuật steganography tiên tiến giúp **ẩn thông điệp trong hình ảnh mà không làm thay đổi vẻ ngoài** của ảnh. Phương pháp này thay thế các vùng có độ phức tạp cao trong ảnh với thông tin bí mật cần giấu.

## 📘 Tài liệu tham khảo
- Kawaguchi, Eiji, and Richard O. Eason. _"Principles and applications of BPCS steganography."_ Photonics East, 1999.

---

## 🚀 Tính năng chính
- Ẩn thông điệp (file bất kỳ, không chỉ là văn bản) trong ảnh PNG.
- Tùy chỉnh ngưỡng phức tạp (`alpha`) để điều chỉnh khả năng giấu thông tin.
- Hỗ trợ encode, decode và kiểm tra khả năng chứa thông điệp của ảnh vessel.
- Có thể sử dụng như module Python hoặc dòng lệnh.

---

## 🔧 Cài đặt

Clone repo về và cài dependencies nếu cần:
```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
```
🧑‍💻 Cách sử dụng
🔐 Encode – Giấu thông điệp trong ảnh
bash
python -m bpcs.bpcs encode \
  -i examples/vessel.png \
  -m examples/message.txt \
  -a 0.45 \
  -o examples/encoded.png
-i: ảnh gốc (vessel image)

-m: thông điệp cần giấu (có thể là bất kỳ file nào)

-a: ngưỡng phức tạp (complexity threshold), mặc định 0.45

-o: ảnh đầu ra chứa thông điệp đã giấu

🔓 Decode – Giải mã thông điệp đã giấu
bash
Sao chép
Chỉnh sửa
python -m bpcs.bpcs decode \
  -i examples/encoded.png \
  -a 0.45 \
  -o examples/message_decoded.txt
File output message_decoded.txt sẽ giống với file gốc message.txt.

📏 Capacity – Kiểm tra dung lượng có thể giấu được
bash
Sao chép
Chỉnh sửa
python -m bpcs.bpcs capacity \
  -i examples/vessel.png \
  -a 0.45
Ví dụ: ảnh vessel.png có dung lượng 158 KB, có thể chứa khoảng 66 KB dữ liệu ẩn.

🛠️ Tùy chỉnh nâng cao
BPCS không sử dụng khóa hoặc mật khẩu. Tuy nhiên, bạn có thể tự mã hóa thông điệp trước khi encode, và giải mã sau khi decode, nhằm tăng độ an toàn.

Ngoài việc điều chỉnh alpha, bạn có thể thêm các bước mã hóa như AES, RSA,...

📦 Sử dụng như module Python
python
Sao chép
Chỉnh sửa
import bpcs

alpha = 0.45
vessel_path = '../examples/vessel.png'
message_path = '../examples/message.txt'
encoded_path = '../examples/encoded.png'
decoded_path = 'tmp.txt'

bpcs.capacity(vessel_path, alpha)
bpcs.encode(vessel_path, message_path, encoded_path, alpha)
bpcs.decode(encoded_path, decoded_path, alpha)
🧪 Chạy test
bash
Sao chép
Chỉnh sửa
python -m bpcs.bpcs test
🐢 Tưởng tượng vui
Bạn có thể giấu một con rùa trong ảnh một con rùa, và tiếp tục giấu nữa... Turtles all the way down. 🐢

📬 Liên hệ
Phát triển bởi [Your Name]. Cần hỗ trợ hoặc muốn đóng góp? Hãy mở issue hoặc pull request nhé!

yaml
Sao chép
Chỉnh sửa

</details>

---

### 🧷 **Bước 2**: Quay lại tab GitHub

1. Dán nội dung đã copy vào khung trống trong ảnh bạn gửi.
2. Kéo xuống dưới cùng → nhập mô tả commit như `"Add complete README for BPCS stego project"`.
3. Bấm nút xanh **"Commit changes…"** ✅

---

Bạn có muốn mình viết thêm phần mã hóa trước khi embed bằng `cryptography` không?







