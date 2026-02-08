import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="مهنتي | منصة التوظيف", page_icon="💼", layout="centered")

# 2. إضافة لمسات جمالية (CSS) لتحسين الخطوط والألوان
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        height: 3em;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية مع الشعار
with st.sidebar:
    # حاول رفع شعارك هنا
    # st.image("logo.png", width=150) 
    st.title("💼 مـهـنـتـي")
    st.markdown("---")
    menu = st.radio("انتقل إلى:", ["🏠 الرئيسية", "🔍 تصفح الوظائف", "➕ أضف وظيفة"])

# 4. محتوى الصفحة الرئيسية
if menu == "🏠 الرئيسية":
    st.markdown("<h1 style='text-align: center;'>مرحباً بك في منصة مهنتي</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1521737711867-e3b97375f902?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    st.write("المنصة الأولى للربط بين الكفاءات وأصحاب العمل بطريقة عصرية وسهلة.")

elif menu == "🔍 تصفح الوظائف":
    st.header("🔍 استكشف الفرص")
    # محاكاة لعرض الوظائف بشكل "بطاقات" (Cards)
    col1, col2 = st.columns(2)
    with col1:
        st.info("*مصمم واجهات*\n\nشركة الإبداع - الرياض\n\nراتب: 8,000 ريال")
    with col2:
        st.info("*مطور بايثون*\n\nتقنية المشرق - جدة\n\nراتب: 12,000 ريال")

elif menu == "➕ أضف وظيفة":
    st.header("➕ نشر إعلان جديد")
    with st.container():
        title = st.text_input("المسمى الوظيفي")
        company = st.text_input("اسم الشركة")
        desc = st.text_area("وصف الوظيفة والمتطلبات")
        if st.button("نشر الآن"):
            st.balloons()
            st.success("تم نشر إعلانك بنجاح!")