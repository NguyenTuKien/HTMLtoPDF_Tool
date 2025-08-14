#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to PDF Converter using Playwright
Tool chuyển đổi file HTML thành PDF sử dụng Playwright - giải pháp hiện đại nhất
"""

import os
import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def convert_html_to_pdf_async(input_file, output_file=None, options=None):
    """Chuyển đổi HTML thành PDF sử dụng Playwright (async)"""
    try:
        # Kiểm tra file đầu vào
        if not os.path.exists(input_file):
            print(f"❌ Không tìm thấy file: {input_file}")
            return False
        
        # Tạo tên file đầu ra
        if output_file is None:
            input_path = Path(input_file)
            output_file = str(input_path.with_suffix('.pdf'))
        
        # Cấu hình mặc định cho PDF
        if options is None:
            options = {
                'format': 'A4',
                'margin': {
                    'top': '1in',
                    'right': '1in',
                    'bottom': '1in',
                    'left': '1in'
                },
                'print_background': True,
                'prefer_css_page_size': True
            }
        
        print(f"📖 Đang đọc file: {input_file}")
        
        # Chuyển đổi đường dẫn file thành URL
        file_url = f"file://{os.path.abspath(input_file)}"
        
        async with async_playwright() as p:
            # Khởi tạo browser
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            print(f"🔄 Đang tạo PDF: {output_file}")
            
            # Điều hướng đến file HTML
            await page.goto(file_url, wait_until='networkidle')
            
            # Đợi thêm một chút để đảm bảo CSS và JavaScript load xong
            await page.wait_for_timeout(1000)
            
            # Tạo PDF
            await page.pdf(path=output_file, **options)
            
            await browser.close()
            
            print(f"✅ Hoàn thành! File PDF: {output_file}")
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False


def convert_html_to_pdf(input_file, output_file=None, options=None):
    """Wrapper function để chạy async function"""
    return asyncio.run(convert_html_to_pdf_async(input_file, output_file, options))


async def convert_directory_async(input_dir, output_dir=None, options=None):
    """Chuyển đổi tất cả file HTML trong thư mục (async)"""
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"❌ Thư mục không tồn tại: {input_dir}")
        return False
    
    # Tạo thư mục đầu ra
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Tìm file HTML
    html_files = list(input_path.glob("*.html")) + list(input_path.glob("*.htm"))
    
    if not html_files:
        print(f"❌ Không tìm thấy file HTML nào trong: {input_dir}")
        return False
    
    print(f"🔍 Tìm thấy {len(html_files)} file HTML")
    
    success_count = 0
    for html_file in html_files:
        if output_dir:
            output_file = str(Path(output_dir) / f"{html_file.stem}.pdf")
        else:
            output_file = str(html_file.with_suffix('.pdf'))
        
        print(f"\n📄 Xử lý: {html_file.name}")
        if await convert_html_to_pdf_async(str(html_file), output_file, options):
            success_count += 1
    
    print(f"\n🎉 Hoàn thành! {success_count}/{len(html_files)} file thành công")
    return success_count == len(html_files)


def convert_directory(input_dir, output_dir=None, options=None):
    """Wrapper function để chạy async function"""
    return asyncio.run(convert_directory_async(input_dir, output_dir, options))


def show_help():
    """Hiển thị hướng dẫn sử dụng"""
    print("🔄 HTML to PDF Converter using Playwright")
    print("=" * 50)
    print("Cách sử dụng:")
    print("  python html_to_pdf_playwright.py <file.html>")
    print("  python html_to_pdf_playwright.py <file.html> <output.pdf>")
    print("  python html_to_pdf_playwright.py <thư_mục> -d")
    print("  python html_to_pdf_playwright.py <thư_mục> -d <thư_mục_đầu_ra>")
    print("\nVí dụ:")
    print("  python html_to_pdf_playwright.py document.html")
    print("  python html_to_pdf_playwright.py document.html output.pdf")
    print("  python html_to_pdf_playwright.py ./html_files -d")
    print("  python html_to_pdf_playwright.py ./html_files -d ./pdf_files")
    print("\n📋 Yêu cầu:")
    print("  - playwright: pip install playwright")
    print("  - playwright install chromium")


def main():
    """Hàm chính"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    input_path = sys.argv[1]
    
    # Chế độ thư mục
    if len(sys.argv) > 2 and sys.argv[2] == '-d':
        output_dir = sys.argv[3] if len(sys.argv) > 3 else None
        convert_directory(input_path, output_dir)
    else:
        # Chế độ file đơn lẻ
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_html_to_pdf(input_path, output_file)


if __name__ == "__main__":
    main()
