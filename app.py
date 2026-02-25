import streamlit as st

# 頁面設定：針對手機版最佳化
st.set_page_config(page_title="行程與導航指南", page_icon="🗺️", layout="centered")

# --- 第一部分：老師 ---
st.title("台南老師")
# link_button 在手機上會顯示為一個大按鈕，方便觸控
st.link_button("👉 點我導航至 停車點", "https://maps.app.goo.gl/jxkgMhww3xWPH2WK8", use_container_width=True)

# 圖片放置處：使用 try-except 避免您還沒放圖片時網頁報錯
try:
    # use_container_width=True 會讓圖片自動撐滿手機螢幕寬度
    st.image("image_teacher_parking.jpg", caption="停車點實景", use_container_width=True)
except FileNotFoundError:
    st.info("🖼️ 圖片預留區：請將檔名命名為 `image_teacher_parking.jpg` 並上傳至 GitHub")

# 老師家 (走路)
st.markdown("### 🚶 老師家 &nbsp;&nbsp; <span style='font-size: 16px; font-weight: normal;'>臺南市西港區新興街106巷8號</span>", unsafe_allow_html=True)

st.link_button("👉 點我導航至：老師家", "https://maps.app.goo.gl/9C5QxTWD7q9AK5eq8", use_container_width=True)

try:
    st.image("image_teacher_house.jpg", caption="老師家實景", use_container_width=True)
except FileNotFoundError:
    st.info("🖼️ 圖片預留區：請將檔名命名為 `image_teacher_house.jpg` 並上傳至 GitHub")

# 視覺分隔線
st.divider() 

# --- 第二部分：祭改 ---
st.title("祭改 - 臺南開基玉皇宮")
st.write("""
臺南市北區佑民街111號
""")
# 停車入口 (開車)
st.subheader("🚗 停車入口")
st.link_button("👉 點我導航至：停車入口", "https://maps.app.goo.gl/ibzkYZTDCEtPn9HGA", use_container_width=True)

try:
    st.image("image_entrance.jpg", caption="停車入口實景", use_container_width=True)
except FileNotFoundError:
    st.info("🖼️ 圖片預留區：請將檔名命名為 `image_entrance.jpg` 並上傳至 GitHub")

# 停車場 (開車)
st.subheader("🅿️ 停車場")
st.link_button("👉 點我導航至：停車場", "https://maps.app.goo.gl/1bYYhVkcfYMhcdtk8", use_container_width=True)

try:
    st.image("image_parking.jpg", caption="停車場實景", use_container_width=True)
except FileNotFoundError:
    st.info("🖼️ 圖片預留區：請將檔名命名為 `image_parking.jpg` 並上傳至 GitHub")

# 文字區塊
st.subheader("📝 補充說明")
st.write("""
到廟後，到1F中間進去，左邊，說要祭改，，給林老師，問他林老師是哪一個他會跟你說，然後拿祭改的東西去排隊(放在林老師桌上，放完後去2F拜、1拜，等祭改
""")
