# -*- coding: utf-8 -*-
import os

def generate_html(image_paths):
    # 生成相框HTML代码
    gallery_html = []
    for i, img_path in enumerate(image_paths, 1):
        frame_html = f"""
        <div class="photo-frame">
            <img src="{img_path}" alt="Memory {i}">
        </div>"""
        gallery_html.append(frame_html)
    
    # 完整HTML模板
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MEMORY Gallery</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow-x: hidden;
            background-color: #000011;
            font-family: Arial, sans-serif;
        }}
        
        .memory-container {{
            position: fixed;
            top: 0;
            left: 0;
            display: flex;
            height: 100vh;
            width: 100vw;
            justify-content: space-around;
            pointer-events: none;
        }}
        
        .memory-column {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 20px;
        }}
        
        .memory-letter {{
            color: rgba(100, 255, 255, 0.9);
            font-size: 10px;
            opacity: 0;
            text-shadow: 0 0 5px rgba(0, 200, 255, 0.7);
            transition: opacity 1.5s ease-out;
            margin: 3px 0;
            height: 16px;
            line-height: 16px;
            will-change: opacity;
            letter-spacing: 0.5px;
        }}

        .gallery-container {{
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
            padding: 40px 20px;
            margin-top: 100vh;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }}

        .photo-frame {{
            background: #fff;
            padding: 15px;
            border: 10px solid #f5e6d3;
            box-shadow: 0 0 15px rgba(100, 255, 255, 0.3);
            transform: rotate(-3deg);
            transition: transform 0.3s ease;
        }}

        .photo-frame:hover {{
            transform: rotate(0deg);
        }}

        .photo-frame img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        .photo-frame:nth-child(odd) {{
            transform: rotate(3deg);
        }}
        .photo-frame:nth-child(even):hover {{
            transform: rotate(0deg);
        }}
    </style>
</head>
<body>
    <div class="memory-container" id="memoryContainer"></div>

    <div class="gallery-container">
        {''.join(gallery_html)}
    </div>

    <script>
        const container = document.getElementById('memoryContainer');
        const columns = Math.floor(window.innerWidth / 20);
        const rows = Math.floor(window.innerHeight / 16);
        const word = "MEMORY";
        const wordLength = word.length;
        
        // 创建列和字母
        for (let i = 0; i < columns; i++) {{
            const column = document.createElement('div');
            column.className = 'memory-column';
            
            for (let j = 0; j < rows; j++) {{
                const letter = document.createElement('div');
                letter.className = 'memory-letter';
                letter.textContent = '';
                column.appendChild(letter);
            }}
            
            container.appendChild(column);
        }}
        
        // 水滴下滑动画函数
        function playWaterDropAnimation() {{
            const allColumns = document.querySelectorAll('.memory-column');
            
            allColumns.forEach(column => {{
                if (Math.random() > 0.7) {{
                    const letters = column.querySelectorAll('.memory-letter');
                    const totalLetters = letters.length;
                    const dropLength = Math.max(6, Math.floor(Math.random() * totalLetters));
                    const startPos = Math.floor(Math.random() * (totalLetters - dropLength));
                    
                    const animationDuration = 1000 + Math.random() * 1000;
                    const startDelay = Math.random() * 800;
                    const fadeDelay = 100 + Math.random() * 200;
                    
                    Array.from(letters).slice(startPos, startPos + dropLength).forEach((letter, index) => {{
                        setTimeout(() => {{
                            const charIndex = index % wordLength;
                            letter.textContent = word.charAt(charIndex);
                            letter.style.opacity = '0.9';
                            
                            setTimeout(() => {{
                                letter.style.opacity = '0';
                            }}, fadeDelay + index * 60);
                        }}, startDelay + index * 50);
                    }});
                }}
            }});
        }}
        
        setTimeout(() => {{
            playWaterDropAnimation();
            setInterval(() => {{
                playWaterDropAnimation();
            }}, 1000 + Math.random() * 600);
        }}, 500);
        
        window.addEventListener('resize', () => {{
            location.reload();
        }});
    </script>
</body>
</html>"""

    # 写入文件
    with open("memory_gallery.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"成功生成文件：memory_gallery.html")

if __name__ == "__main__":
    # 需要导入的图片配置（请修改为实际路径）
    image_paths = [
        "images/photo1.jpg",    # 相对路径示例（推荐）
        "images/photo2.jpg",
        "images/photo3.jpg",
        "images/photo4.jpg",
        "images/photo5.jpg",
        "images/photo6.jpg",
        "images/photo7.jpg",
        "images/photo9.jpg",
        "images/photo10.jpg",
        "images/photo11.jpg",
        "images/photo12.jpg",
        "images/photo13.jpg",
        "images/photo14.jpg",
        "images/photo15.jpg",
        "images/photo16.jpg",
        "images/photo17.jpg",
        "images/photo18.jpg",
        "images/photo19.jpg",
        "images/photo20.jpg",
        "images/photo21.jpg",
        "images/photo22.jpg",
        "images/photo23.jpg",
        "images/photo24.jpg",
        "images/photo25.jpg",
        "images/photo26.jpg",
        "images/photo27.jpg",
        "images/photo28.jpg",
        "images/photo29.jpg",
        "images/photo30.jpg",
        "images/photo31.jpg",
        "images/photo32.jpg",
        "images/photo33.jpg",
        # "file:///C:/Users/YourName/Pictures/photo5.jpg",  # 绝对路径示例
    ]
    
    # 检查图片目录是否存在
    if not os.path.exists("images"):
        print("提示：建议在项目目录下创建images文件夹存放图片")
    
    generate_html(image_paths)
