# HTML to PDF Converter using Playwright

Tool chuyển đổi file HTML thành PDF sử dụng **Playwright** - giải pháp hiện đại và mạnh mẽ nhất cho việc chuyển đổi HTML sang PDF với chất lượng pixel-perfect!

## ✨ Tính năng

- ✅ **CSS Support hoàn hảo** - Hỗ trợ mọi CSS styling hiện đại
- ✅ **JavaScript Support** - Render dynamic content và interactive elements
- ✅ **Chất lượng tuyệt vời** - PDF giống hệt HTML gốc
- ✅ **Hỗ trợ Unicode** - Tiếng Việt và emoji hoàn hảo
- ✅ **Responsive Design** - Tự động điều chỉnh layout
- ✅ **Performance cao** - Xử lý nhanh với Chromium engine

## 🚀 Cài đặt

### 1. Cài đặt Python dependencies
```bash
pip install -r requirements_playwright.txt
```

Hoặc cài đặt trực tiếp:
```bash
pip install playwright==1.40.0
```

### 2. Cài đặt browser engine
```bash
playwright install chromium
```

**Lưu ý:** Bước này tải về Chromium browser engine (~150MB) cần thiết để render HTML.

## 📖 Cách sử dụng

### Chuyển đổi file đơn lẻ
```bash
# Chuyển đổi file HTML cơ bản
python html_to_pdf_playwright.py document.html

# Chỉ định tên file PDF đầu ra
python html_to_pdf_playwright.py document.html output.pdf
```

### Chuyển đổi hàng loạt
```bash
# Chuyển đổi tất cả file HTML trong thư mục hiện tại
python html_to_pdf_playwright.py . -d

# Chuyển đổi và lưu vào thư mục khác
python html_to_pdf_playwright.py ./html_files -d ./pdf_files
```

### Xem hướng dẫn
```bash
python html_to_pdf_playwright.py
```

## 📋 Cú pháp

```bash
python html_to_pdf_playwright.py <input> [output] [-d] [output_dir]
```

**Tham số:**
- `input`: File HTML hoặc thư mục chứa file HTML
- `output`: Tên file PDF đầu ra (tùy chọn)
- `-d`: Chế độ thư mục (chuyển đổi hàng loạt)
- `output_dir`: Thư mục đầu ra cho chế độ thư mục

## 🎨 Tính năng nâng cao

### CSS Support
Tool hỗ trợ đầy đủ CSS styling:
- **Layout**: Flexbox, Grid, Position, Display
- **Typography**: Fonts, sizes, weights, colors, alignment
- **Styling**: Backgrounds, borders, shadows, gradients
- **Responsive**: Media queries, viewport, breakpoints
- **Animations**: Transitions, transforms, keyframes

### JavaScript Support
- Render JavaScript content và dynamic elements
- Interactive components và event handling
- Single Page Applications (SPA)
- AJAX content và API calls

### Tùy chỉnh PDF
```python
options = {
    'format': 'A4',              # A4, Letter, Legal, etc.
    'margin': {                  # Margins
        'top': '1in',
        'right': '1in',
        'bottom': '1in',
        'left': '1in'
    },
    'print_background': True,    # Include background colors
    'prefer_css_page_size': True # Use CSS @page rules
}
```

## 📊 So sánh với các thư viện khác

| Tính năng | **Playwright** | pdfkit | fpdf |
|-----------|----------------|--------|------|
| **CSS Support** | ✅ Hoàn hảo | ✅ Đầy đủ | ❌ Không |
| **JavaScript** | ✅ Hoàn hảo | ✅ Hỗ trợ | ❌ Không |
| **Unicode** | ✅ Hoàn hảo | ✅ Hoàn hảo | ❌ Lỗi |
| **Chất lượng** | ✅ Tuyệt vời | ✅ Cao | ⚠️ Cơ bản |
| **Performance** | ✅ Rất nhanh | ✅ Nhanh | ✅ Rất nhanh |
| **Cài đặt** | ⚠️ Cần browser | ⚠️ Cần wkhtmltopdf | ✅ Rất dễ |

## 🔧 Ví dụ sử dụng

### 1. File HTML với CSS styling
```html
<!DOCTYPE html>
<html>
<head>
    <title>Ví dụ HTML</title>
    <style>
        body { 
            font-family: Arial; 
            color: #333; 
            background: linear-gradient(135deg, #667eea, #764ba2);
        }
        h1 { 
            color: #2c3e50; 
            text-align: center; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .content { 
            background: white; 
            padding: 20px; 
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Tiêu đề chính</h1>
    <div class="content">
        <p>Đây là nội dung văn bản với styling đẹp mắt.</p>
        <ul>
            <li>Mục 1 với emoji 🎉</li>
            <li>Mục 2 với icon ✅</li>
        </ul>
    </div>
</body>
</html>
```

### 2. Chuyển đổi thành PDF
```bash
python html_to_pdf_playwright.py example.html
```

## ⚠️ Lưu ý quan trọng

### Yêu cầu hệ thống
- **Python 3.7+**: Để sử dụng Playwright
- **Chromium Browser**: Tự động tải khi cài đặt
- **RAM**: Tối thiểu 1GB cho file lớn
- **Disk Space**: ~150MB cho Chromium engine

### Xử lý lỗi thường gặp

**Lỗi "playwright not found":**
```bash
# Cài đặt lại playwright
pip install playwright
playwright install chromium
```

**Lỗi "browser not found":**
```bash
# Cài đặt browser engine
playwright install chromium
```

**Lỗi timeout:**
```python
# Tăng timeout trong code
await page.wait_for_timeout(3000)  # 3 giây
```

## 🎯 Lợi ích

### So với các giải pháp khác:
- **Chất lượng cao nhất**: PDF giống hệt HTML gốc
- **CSS Support hoàn hảo**: Hỗ trợ mọi CSS styling
- **JavaScript Support**: Render dynamic content
- **Performance tốt**: Xử lý nhanh với Chromium
- **Ổn định**: Được phát triển bởi Microsoft

### Ứng dụng thực tế:
- **Báo cáo**: Chuyển đổi báo cáo web thành PDF
- **Invoices**: Tạo hóa đơn từ HTML templates
- **Documents**: Chuyển đổi tài liệu web
- **Presentations**: Export slides thành PDF
- **Websites**: Capture toàn bộ website

## 🔧 Tùy chỉnh nâng cao

### Tùy chỉnh PDF options
```python
from html_to_pdf_playwright import convert_html_to_pdf

options = {
    'format': 'A4',
    'margin': {'top': '0.5in', 'right': '0.5in', 'bottom': '0.5in', 'left': '0.5in'},
    'print_background': True,
    'prefer_css_page_size': True,
    'scale': 0.8,  # Scale down to 80%
    'landscape': False  # Portrait mode
}

convert_html_to_pdf('input.html', 'output.pdf', options)
```

### Xử lý JavaScript
```python
# Đợi JavaScript load xong
await page.wait_for_timeout(2000)  # 2 giây

# Hoặc đợi element cụ thể
await page.wait_for_selector('.content-loaded')
```

## 📄 Giấy phép

Tool này sử dụng:
- **Playwright**: Apache License 2.0
- **Chromium**: BSD License

## 🤝 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra Playwright đã cài đặt đúng chưa
2. Đảm bảo Chromium browser đã được tải
3. Thử với file HTML đơn giản trước
4. Kiểm tra console output để debug

### Troubleshooting
```bash
# Kiểm tra cài đặt
playwright --version
playwright install --help

# Test browser
playwright test --browser=chromium
```

---

**Playwright** là lựa chọn tuyệt vời cho việc chuyển đổi HTML thành PDF với chất lượng cao nhất và độ chính xác pixel-perfect! 🎭✨
