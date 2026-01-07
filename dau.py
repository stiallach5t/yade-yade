import streamlit as st
from PIL import Image
import os
import base64

# Cấu hình trang web
st.set_page_config(
    page_title="Hồ Sơ Của TranVy",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- HÀM TẠO NỀN PIXEL ĐỘNG VÀ GIAO DIỆN MÀU MỚI ---
def local_css_and_js():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            color: #f0f0f0;
        }

        #pixel-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.5;
        }

        .profile-img-container {
            display: flex;
            justify-content: center;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        
        .profile-img {
            border-radius: 50%;
            border: 5px solid #ff00cc;
            box-shadow: 0 0 30px rgba(255, 0, 204, 0.6);
            transition: all 0.4s ease;
            object-fit: cover;
            width: 220px;
            height: 220px;
        }
        
        .profile-img:hover {
            transform: scale(1.1) rotate(-5deg);
            border-color: #33ccff;
            box-shadow: 0 0 40px rgba(51, 204, 255, 0.8);
        }

        [data-testid="stVerticalBlock"] > div > div > div[style*="border"] {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 25px !important;
            backdrop-filter: blur(15px);
            transition: all 0.3s ease;
            padding: 25px;
        }
        
        .skill-tag {
            display: inline-block;
            padding: 8px 16px;
            margin: 6px;
            background: linear-gradient(90deg, #ff00cc, #33ccff);
            color: white;
            border-radius: 50px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            font-weight: bold;
        }

        .gradient-text {
            background: linear-gradient(90deg, #ff00cc, #33ccff, #ff00cc);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            text-align: center;
            animation: shine 3s linear infinite;
        }

        @keyframes shine {
            to { background-position: 200% center; }
        }
        
        .center-text {
            text-align: center;
        }

        /* Nút bấm kiểu neon */
        .stButton>button {
            border-radius: 50px;
            background: linear-gradient(90deg, #ff00cc, #33ccff);
            color: white;
            border: none;
            font-weight: bold;
            padding: 10px 30px;
            transition: 0.3s;
        }

        /* --- PHẦN SOCIAL LINKS ĐẶC SẮC --- */
        .social-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
            padding: 20px;
        }

        .social-link {
            text-decoration: none;
            color: white;
            font-size: 1.5rem;
            font-weight: 800;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: all 0.3s ease;
            position: relative;
        }

        .social-link i {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .social-link:hover {
            transform: translateY(-10px);
            filter: drop-shadow(0 0 15px currentColor);
        }

        .fb-link:hover { color: #1877F2; }
        .gh-link:hover { color: #ffffff; }
        .ig-link:hover { color: #E4405F; }

        .social-label {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            opacity: 0.6;
            transition: opacity 0.3s;
        }

        .social-link:hover .social-label {
            opacity: 1;
        }
        </style>

        <!-- Import Font Awesome để lấy icon -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

        <canvas id="pixel-canvas"></canvas>

        <script>
        const canvas = document.getElementById('pixel-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let particles = [];
        const colors = ['#ff00cc', '#33ccff', '#ffffff'];

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 4 + 1; 
                this.speedX = (Math.random() - 0.5) * 1.2;
                this.speedY = (Math.random() - 0.5) * 1.2;
                this.color = colors[Math.floor(Math.random() * colors.length)];
            }
            update() {
                this.x += this.speedX; this.y += this.speedY;
                if (this.x > canvas.width) this.x = 0;
                if (this.x < 0) this.x = canvas.width;
                if (this.y > canvas.height) this.y = 0;
                if (this.y < 0) this.y = canvas.height;
            }
            draw() {
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 8;
                ctx.shadowColor = this.color;
                ctx.fillRect(Math.floor(this.x), Math.floor(this.y), this.size, this.size);
            }
        }

        function init() {
            particles = [];
            const count = (canvas.width * canvas.height) / 12000;
            for (let i = 0; i < count; i++) { particles.push(new Particle()); }
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particles.length; i++) {
                particles[i].update(); particles[i].draw();
            }
            requestAnimationFrame(animate);
        }
        init(); animate();
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight; init();
        });
        </script>
    """, unsafe_allow_html=True)

local_css_and_js()

# --- LINK ẢNH ĐẠI DIỆN ---
MY_IMAGE_SOURCE = "https://scontent.fhan15-1.fna.fbcdn.net/v/t39.30808-6/602351839_122162512520745859_419513426744476516_n.jpg?stp=cp6_dst-jpg_tt6&_nc_cat=105&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=9j2YpAy3HHcQ7kNvwFf1LqM&_nc_oc=AdngdAuSr1fe2JM2LWLIAQdBtWOEdFvFppS5Eoh_eQxVXIvBe6CGW4mDGIjN3WfJNe6MkqwElbxjwgeg106tMBBO&_nc_zt=23&_nc_ht=scontent.fhan15-1.fna&_nc_gid=7jbxQPLaXV8ZZEUjwcW5nA&oh=00_AfpGwdjhOPlu1stRSQHgPUMQ8K7kUZzvJy7NAJZRus2cAA&oe=6963B449"

st.markdown(f"""
    <div class="profile-img-container">
        <img src="{MY_IMAGE_SOURCE}" class="profile-img">
    </div>
""", unsafe_allow_html=True)

# --- TIÊU ĐỀ VÀ NỘI DUNG ---
st.markdown("<h1 class='gradient-text' style='font-size: 4rem;'>TranVy</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-text' style='font-size: 1.5rem; color: #33ccff; font-weight: bold;'>🌈 Trùm Cuối Pixel Art | Chúa Tể Python 🌈</p>", unsafe_allow_html=True)

st.write("##")

col_mid_1, col_mid_2, col_mid_3 = st.columns([1, 2, 1])
with col_mid_2:
    with st.container(border=True):
        st.markdown("<h3 style='text-align: center; color: #ff00cc;'>Tuyên Ngôn Của T</h3>", unsafe_allow_html=True)
        st.write("""
        Chào mấy con vợ! Web này t build bằng Python, nhìn là biết t ngầu vcl rồi đúng ko? 
        Đừng có nhìn lâu quá kẻo bị "gây" bởi vẻ đẹp trai và trí tuệ vô cực của t. 
        T không chỉ code giỏi mà t còn đẹp lồng lộn, bóng lộn như mấy hạt Pixel đang bay ở nền web này vậy. 
        Ai thấy t ngầu thì bấm nút dưới đây, không ngầu cũng phải bấm vì t đẹp t có quyền!
        """)
        
        if st.button("🔥 Bấm vào đây nếu m thấy t quá đẹp trai", use_container_width=True):
            st.balloons()
            st.snow()
            st.success("T biết mà, m không thể cưỡng lại được sự quyến rũ này đâu! Email t: tranquocanhvy@gmail.com")

st.write("##")
st.markdown("<h2 class='gradient-text'>⚡ Siêu Năng Lượng Của T</h2>", unsafe_allow_html=True)

skills = {
    "Ngôn ngữ (T nói gì máy cũng nghe)": ["Python Master", "JS Ninja", "SQL Boss"],
    "Công cụ (Đồ chơi của t)": ["Git", "VS Code Siêu Cấp", "Docker", "Linux Pro"]
}

c1, c2 = st.columns(2)
with c1:
    with st.container(border=True):
        st.write(f"#### {list(skills.keys())[0]}")
        st.markdown(" ".join([f'<span class="skill-tag">{s}</span>' for s in skills[list(skills.keys())[0]]]), unsafe_allow_html=True)
with c2:
    with st.container(border=True):
        st.write(f"#### {list(skills.keys())[1]}")
        st.markdown(" ".join([f'<span class="skill-tag">{s}</span>' for s in skills[list(skills.keys())[1]]]), unsafe_allow_html=True)

st.write("##")
st.divider()

# --- FOOTER SOCIAL LINKS ---
st.markdown("<h2 class='gradient-text'>📫 Kết Nối Với T</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class="social-container">
        <a href="https://www.facebook.com/sucvattranv/" target="_blank" class="social-link fb-link">
            <i class="fab fa-facebook"></i>
            <span class="social-label">Facebook</span>
        </a>
        <a href="https://github.com/stiallach5t" target="_blank" class="social-link gh-link">
            <i class="fab fa-github"></i>
            <span class="social-label">GitHub</span>
        </a>
        <a href="https://www.instagram.com/emyeuanhjack2cu/" target="_blank" class="social-link ig-link">
            <i class="fab fa-instagram"></i>
            <span class="social-label">Instagram</span>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br><center><p style='opacity: 0.4; font-size: 0.8rem;'>Copyright © 2024 TranVy - Quá Đẹp Trai Để Làm Người Thường</p></center>", unsafe_allow_html=True)