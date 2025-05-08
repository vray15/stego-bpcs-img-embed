# HƯỚNG DẪN THỰC HÀNH BÀI LAB STEGO-BPCS-IMG-EMBED

Bài lab này hướng dẫn thực hiện giấu thông điệp vào ảnh sử dụng thuật toán BPCS (Bit-Plane Complexity Segmentation) trong môi trường ảo hóa Labtainer. Dưới đây là các bước chi tiết để thực hiện bài lab.

---

## Chuẩn bị môi trường

1. **Phần mềm cần thiết**:
   - Phần mềm ảo hóa: VMWare Workstation.
   - Máy ảo Labtainer được cấu hình kết nối internet.

2. **Tải bài lab**:
   - Mở terminal trong thư mục `/home/student/labtainer/labtainer-student`.
   - Thực hiện lệnh:
     ```
     imodule https://github.com/vray15/stego-bpcs-img-embed/raw/refs/heads/master/imodule.tar
     ```

3. **Khởi tạo bài lab**:
   - Chạy lệnh:
     ```
     labtainer -r stego-bpcs-img-embed
     ```
   - Nhập email sử dụng mã sinh viên khi được yêu cầu (dùng để chấm điểm).

---

## Các nhiệm vụ cần thực hiện

### 1. Tiền xử lý dữ liệu

#### a. Xử lý dữ liệu đầu vào với thông điệp
- Mục tiêu: Chuyển chuỗi ký tự trong file `text.txt` thành chuỗi bit và lưu vào `message.txt`.
- Thực hiện:
  1. Đưa file `text.txt` vào thư mục `examples`.
  2. Chỉnh sửa file `binary.py` để nhận đầu vào từ `text.txt`.
  3. Chạy lệnh:
     ```
     python3 binary.py > message.txt
     ```

#### b. Xử lý dữ liệu đầu vào với ảnh
- Mục tiêu: Kiểm tra độ nhiễu của ảnh `vessel.png` và xác định dung lượng tin ẩn có thể giấu.
- Thực hiện:
  1. Cài đặt các thư viện cần thiết:
     ```
     pip3 install numpy scipy matplotlib Pillow
     ```
  2. Kiểm tra dung lượng và độ nhiễu của ảnh:
     ```
     python -m bpcs.bpcs capacity -i examples/vessel.png -a <ngưỡng phức tạp>
     ```
     (Thay `<ngưỡng phức tạp>` bằng giá trị alpha phù hợp, ví dụ: 0.3).

---

### 2. Giấu tin trong ảnh

- Mục tiêu: Giấu thông điệp từ `message.txt` vào ảnh `vessel.png` sử dụng thuật toán BPCS.
- Thực hiện:
  - Chạy lệnh:
    ```
    python3 -m bpcs.bpcs encode -i examples/vessel.png -m examples/message.txt -a <alpha> -o output.png
    ```
    - `-i`: File ảnh đầu vào (`vessel.png`).
    - `-m`: File chứa thông điệp (`message.txt`).
    - `-a`: Ngưỡng phức tạp (alpha, ví dụ: 0.3).
    - `-o`: File ảnh đầu ra sau khi giấu tin (`output.png`).

---

### 3. Kiểm tra ảnh đã giấu tin

- Mục tiêu: Kiểm tra xem việc giấu tin có thành công hay không thông qua độ nhiễu và biểu đồ.
- Thực hiện:
  1. **Xem ảnh đã giấu**:
     - Cài đặt công cụ `fim`:
       ```
       sudo apt update
       sudo apt install fim
       ```
     - Xem ảnh:
       ```
       fim output.png
       ```
  2. **Kiểm tra độ nhiễu bằng biểu đồ**:
     - Cài đặt thư viện GUI cho Python:
       ```
       sudo apt update
       sudo apt install python3-tk
       ```
     - Vào thư mục `examples` và chỉnh sửa file `compare_hist.py` (bỏ comment phần đầu vào).
     - Chạy lệnh:
       ```
       python3 compare_hist.py
       ```
     - Kết quả: Quan sát biểu đồ để thấy sự chênh lệch độ nhiễu. Nếu giao diện hiển thị “Da ma hoa”, giấu tin thành công.

---

### 4. Kết thúc bài lab

- Kết thúc bài lab bằng lệnh:
     ```
       stoplab
       ```
