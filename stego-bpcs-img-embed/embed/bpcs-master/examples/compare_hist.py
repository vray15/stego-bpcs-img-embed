from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def get_histogram(path):
    img = Image.open(path).convert("L")
    hist = img.histogram()
    return np.array(hist)
#hist1 = get_histogram('vessel.png')
#hist2 = get_histogram('encoded.png')

diff = np.abs(hist1 - hist2)
mae = np.mean(diff)
plt.plot(hist1, label='Gốc')
plt.plot(hist2, label='Đã encode')
plt.legend()
plt.title('So sánh Histogram ảnh Gốc vs. Ảnh đã Encode')
plt.xlabel('Giá trị pixel (0-255)')
plt.ylabel('Số lượng pixel')
plt.grid(True)
plt.show()

print(f"Do lech histogram (MAE): {mae:.2f}")
threshold = 10  # <= 5 la gan như khong thay doi

if mae > threshold:
    print("Da ma hoa")
else:
    print("Chua ma hoa")
