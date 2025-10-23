import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import re

# --- Page Configuration --- final code the goat code 
st.set_page_config(
    page_title="SIES College - Admission Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Professional Blue CSS for SIES Official Use ---
st.markdown("""
<style>
* {
    font-family: 'Segoe UI', 'Arial', sans-serif;
}

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    color: #e0e0e0;
}

/* Header Section */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #000000 0%, #333333 100%);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.logo-section {
    text-align: center;
    flex: 1;
}

.sies-logo {
    font-size: 3.5rem;
    margin-bottom: 10px;
}

.college-name {
    font-size: 1.4rem;
    font-weight: 800;
    color: #007bff;
    letter-spacing: 1px;
    margin: 5px 0;
}

.college-subtitle {
    font-size: 0.9rem;
    color: #a9a9a9;
    font-weight: 500;
}

.main-header {
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
    letter-spacing: 0.5px;
    flex: 2;
}

.subheader {
    text-align: center;
    color: #cccccc;
    font-size: 1rem;
    margin-top: 1rem;
    margin-bottom: 2rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}

/* Sidebar Professional Styling */
.sidebar-header {
    background: linear-gradient(135deg, #000000 0%, #333333 100%);
    color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    font-size: 1.1rem;
    font-weight: 800;
    margin-bottom: 15px;
    text-align: center;
    letter-spacing: 0.5px;
}

.sidebar-section {
    background: #2d2d2d;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    border-left: 5px solid #007bff;
}

.sidebar-section-title {
    color: #ffffff;
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 10px;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    padding: 0.65rem 1rem;
    background: linear-gradient(135deg, #000000 0%, #333333 100%);
    color: #e0e0e0;
    border: 1px solid #007bff;
    font-size: 0.92rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    width: 100%;
    margin: 6px 0;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 123, 255, 0.2);
    background: linear-gradient(135deg, #333333 0%, #000000 100%);
    color: #007bff;
}

/* Info Box - Official Black */
.info-box {
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.4), rgba(51, 51, 51, 0.3));
    border-left: 5px solid #000000;
    border-radius: 12px;
    padding: 16px;
    margin: 12px 0;
    line-height: 1.7;
    font-size: 0.96rem;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.4);
}

.info-box b {
    color: #007bff;
    font-weight: 700;
}

/* Success Box - Blue for Courses */
.success-box {
    background: linear-gradient(135deg, rgba(0, 123, 255, 0.1), rgba(0, 123, 255, 0.05));
    border-left: 5px solid #007bff;
    border-radius: 12px;
    padding: 16px;
    margin: 12px 0;
    box-shadow: 0 3px 10px rgba(0, 123, 255, 0.15);
}

.success-box b {
    color: #007bff;
    font-weight: 700;
}

/* Error Box */
.error-box {
    background: linear-gradient(135deg, rgba(139, 0, 0, 0.2), rgba(128, 0, 0, 0.1));
    border-left: 5px solid #8b0000;
    border-radius: 12px;
    padding: 16px;
    margin: 12px 0;
    color: #ffcccb;
    font-weight: 500;
    box-shadow: 0 3px 10px rgba(139, 0, 0, 0.2);
}

/* Merit List Container */
.merit-list-container {
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.2), rgba(0, 123, 255, 0.05));
    border: 2px solid rgba(0, 123, 255, 0.2);
    border-radius: 12px;
    padding: 18px;
    margin: 12px 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.merit-list-container > b {
    color: #007bff;
    font-size: 1.1rem;
    font-weight: 700;
}

/* Merit Item */
.merit-item {
    padding: 12px;
    margin: 8px 0;
    background: #2d2d2d;
    border-radius: 8px;
    border-left: 4px solid #007bff;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

.merit-item:hover {
    transform: translateX(6px);
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.2);
    background: rgba(0, 123, 255, 0.05);
}

.merit-item a {
    color: #ffffff;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95rem;
}

.merit-item a:hover {
    text-decoration: underline;
    color: #007bff;
}

/* Total Count Badge */
.total-count {
    background: linear-gradient(135deg, #000000 0%, #333333 100%);
    color: #ffffff;
    padding: 12px 18px;
    border-radius: 8px;
    font-weight: 700;
    margin-top: 14px;
    text-align: center;
    font-size: 0.95rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    border: 1px solid #007bff;
}

/* Course Item */
.course-item {
    background: #2d2d2d;
    padding: 12px 14px;
    margin: 8px 0;
    border-radius: 8px;
    border-left: 4px solid #007bff;
    font-size: 0.92rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
    color: #e0e0e0;
}

.course-item:hover {
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.2);
    transform: translateX(3px);
}

/* FAQ Item */
.faq-item {
    background: #2d2d2d;
    padding: 12px 14px;
    margin: 8px 0;
    border-radius: 8px;
    border-left: 4px solid #007bff;
    font-size: 0.92rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
    color: #e0e0e0;
}

.faq-item b {
    color: #007bff;
}

/* Chat Message Styling */
[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 12px;
    margin: 10px 0;
    background: #2d2d2d;
    color: #e0e0e0;
}

/* Input Area */
[data-testid="stChatInputContainer"] {
    margin-top: 1.5rem;
    padding: 10px;
    background: #2d2d2d;
}

/* Contact Section */
.contact-section {
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.3), rgba(0, 123, 255, 0.05));
    border-radius: 10px;
    padding: 15px;
    margin-top: 2rem;
    font-size: 0.85rem;
    color: #cccccc;
    border: 2px solid rgba(0, 123, 255, 0.15);
}

.contact-section b {
    color: #007bff;
    font-weight: 700;
}

.contact-section a {
    color: #ffffff;
    text-decoration: none;
    font-weight: 600;
}

.contact-section a:hover {
    text-decoration: underline;
    color: #007bff;
}

/* Divider */
.stDivider {
    margin: 1.5rem 0;
    border-color: rgba(0, 123, 255, 0.2);
}

/* Footer */
.footer-text {
    text-align: center;
    font-size: 0.8rem;
    color: #a9a9a9;
    margin-top: 20px;
    padding-top: 15px;
    border-top: 1px solid rgba(0, 123, 255, 0.1);
}

@media (max-width: 768px) {
    .header-container {
        flex-direction: column;
        gap: 10px;
    }
    
    .main-header {
        font-size: 1.8rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Faculty & Course Data ---
PRINCIPAL_INFO = {
    'name': 'Dr. Koel Roychoudhury',
    'role': 'Principal of Degree College',
    'department': 'Economics',
    'email': 'principal@siesascn.edu.in'
}

# Junior College Info
JUNIOR_COLLEGE_INFO = {
    'vice_principal': 'Ms. Sunita Ambhore',
    'faculty': [
        'Ms. Rajashri Shinde - Faculty',
        'Ms. Rajeshree Ravi - Faculty',
        'Mr. Vishwanath Kale - Faculty',
        'Ms. Neha Pandey - Faculty',
        'Mr. Sreejith Nair - Faculty',
        'Ms. Subbulaxmi P. Thevar - Faculty (Sports)',
        'Ms. Pooja Sharma - Faculty',
        'Ms. Suhangi Jadhav - Faculty'
    ]
}

# Library Info
LIBRARY_INFO = {
    'librarian': 'Mr. Gulabchandra Sharma'
}

FACULTY_DATA = {
    'economics': {
        'hod': 'Dr. Koel Roychoudhury (also Principal)',
        'full_name': 'Economics',
        'faculty': [
            'Dr. Koel Roychoudhury - Head of Department (also Principal)',
            'Dr. Neera Kumar - Associate Professor',
            'Ms. Alisha Varghese - Assistant Professor'
        ]
    },
    'commerce': {
        'hod': 'Mr. Girish Karnad',
        'full_name': 'Commerce',
        'faculty': [
            'Mr. Girish Karnad - Head of Department',
            'Ms. Sugandha Jha - Vice-Principal',
            'Mr. Vishal Bodhale - Assistant Professor',
            'Ms. Bhavna Koli - Assistant Professor',
            'Ms. Bhakti Joshi - Assistant Professor',
            'Ms. Aditi Kumar - Assistant Professor'
        ]
    },
    'evs': {
        'hod': 'Dr. Jyoti Jatinder Das',
        'full_name': 'Environmental Science (EVS)',
        'faculty': [
            'Dr. Jyoti Jatinder Das - Head of Department',
            'Ms. Rupali Zele - Assistant Professor',
            'Ms. Kamini Thakur - Assistant Professor',
            'Ms. Tanvi Patil - Assistant Professor'
        ]
    },
    'accountancy': {
        'hod': 'Dr. Priyanka Mohan',
        'full_name': 'Accountancy',
        'faculty': [
            'Dr. Priyanka Mohan - Head of Department',
            'Dr. Babita Kakkar - Coordinator for B.Com. Financial Markets',
            'Dr. Snehal Patil-Birje - Coordinator for M.Com. Advanced Accountancy',
            'Ms. Jinal Khetia - Assistant Professor',
            'Ms. Rachana Prasad - Assistant Professor',
            'Ms. Madhurima Chaudhury - Assistant Professor',
            'Mr. Yogendra Dalvi - Assistant Professor',
            'Mr. Siddhesh Hadkar - Assistant Professor'
        ]
    },
    'banking': {
        'hod': 'Ms. Bhumika More',
        'full_name': 'Banking and Insurance',
        'faculty': [
            'Ms. Bhumika More - Head of Department',
            'Mr. Perumal Ramasubramony - Assistant Professor',
            'Ms. Lata Lokhande - Assistant Professor',
            'Mr. Parth Joshi - Assistant Professor'
        ]
    },
    'bms': {
        'hod': 'Mr. Chaitanya Songirkar',
        'full_name': 'Management Studies (BMS)',
        'faculty': [
            'Mr. Chaitanya Songirkar - Head of Department',
            'Ms. Ananya Gon - Assistant Professor',
            'Ms. Nisha Telang - Assistant Professor',
            'Mr. Tanish Hazari - Assistant Professor',
            'Ms. Rashmeet Kaur - Assistant Professor',
            'Ms. Indira Ulagaraman - Assistant Professor',
            'Ms. Deepti Menon - Assistant Professor',
            'Ms. Karishma Kundlani - Assistant Professor',
            'Mr. Dinar Thavi - Assistant Professor'
        ]
    },
    'bammc': {
        'hod': 'Mr. Mithun Pillai',
        'full_name': 'Multimedia and Mass Communication (BAMMC)',
        'faculty': [
            'Mr. Mithun Pillai - Head of Department',
            'Mr. Abhishek Dandekar - Assistant Professor',
            'Dr. Divya Nair - Assistant Professor',
            'Ms. Tejal Shinde - Assistant Professor',
            'Ms. Nivedita Mitra - Assistant Professor',
            'Ms. Swapna Bawkar - Assistant Professor'
        ]
    },
    'cs': {
        'hod': 'Dr. Sheeja Ravi',
        'full_name': 'Computer Science (CS)',
        'faculty': [
            'Dr. Sheeja Ravi - Head of Department',
            'Dr. Rajeshri Shinkar - Assistant Professor',
            'Dr. Trupti Wani - Coordinator for B.Sc. Part-Time',
            'Ms. Fatema Kothari - Assistant Professor',
            'Dr. Aditya Jinturkar - Assistant Professor',
            'Ms. Jahara Sakriwala - Assistant Professor',
            'Dr. Pallavi Vinayak Awate - Assistant Professor',
            'Ms. Flosia Simon Moses - Assistant Professor',
            'Ms. Shrutika Jadhav - Assistant Professor',
            'Ms. Dipti Patil - Assistant Professor for B.Sc. Artificial Intelligence',
            'Ms. Nisha Padmanabhan - Assistant Professor for B.Sc. Part-Time'
        ]
    },
    'it': {
        'hod': 'Dr. Meghna Bhatia',
        'full_name': 'Information Technology (IT)',
        'vice_principal': 'Dr. Anu Thomas',
        'faculty': [
            'Dr. Meghna Bhatia - Head of Department',
            'Dr. Anu Thomas - Vice-Principal for IT Department',
            'Dr. Nutan Sawant - Coordinator for B.Sc. Data Science',
            'Ms. Arti Bansode - Assistant Professor',
            'Dr. Minal Sarode - Assistant Professor',
            'Ms. Shaima Thange - Assistant Professor',
            'Ms. Sameera Ibrahim - Assistant Professor',
            'Ms. Archana Patil - Assistant Professor',
            'Ms. Sweta Bhandari - Assistant Professor',
            'Ms. Varsha Shinde - Assistant Professor for B.Sc. Data Science',
            'Ms. Rashmi Prabha - Assistant Professor for B.Sc. Data Science'
        ]
    },
}

# FAQs (excluding fee structure to handle separately)
FAQS = [
    {
        'q': 'Does the college provide scholarships?',
        'a': 'Yes. Scholarships are available for SC/ST/OBC, economically weaker students, and merit-based achievers as per Government of Maharashtra and University of Mumbai rules.'
    },
    {
        'q': 'Is there a placement cell?',
        'a': 'Yes. The Placement Cell connects students with top recruiters in IT, Banking, Media, Commerce, and Management fields. Regular training and internship drives are conducted.'
    },
    {
        'q': 'What is the attendance policy?',
        'a': 'Students must maintain at least 75% attendance in each subject to be eligible for appearing in university examinations.'
    },
    {
        'q': 'Does the college have a library?',
        'a': 'Yes. The college has a fully equipped library with e-resources, journals, and a digital learning hub.'
    },
    {
        'q': 'Are there extracurricular activities?',
        'a': 'Yes. Students can join NSS, NCC, cultural clubs, sports teams, and various student-led committees.'
    },
    {
        'q': 'Does the college provide hostel facilities?',
        'a': 'No. The college does not have its own hostel but assists students in finding safe accommodations nearby.'
    },
    {
        'q': 'Does the college have an anti-ragging policy?',
        'a': 'Yes, the college has a dedicated Anti-Ragging Committee and promotes anti-ragging initiatives to ensure a safe and welcoming environment for all students.'
    }
]

# Fee Structure Response
FEE_STRUCTURE_RESPONSE = """
<div class="info-box">
<b>Fee Structure Information</b><br><br>
The detailed fee structure for each undergraduate (UG) and postgraduate (PG) program is typically provided in the official college prospectus, which is available on the college website. For the most accurate and up-to-date fee information, prospective students should download the latest prospectus or contact the college admission office directly.
</div>
"""

# STRICT Merit list patterns
MERIT_PATTERNS = {
    'bcom': {
        'patterns': [r'merit list.*b\.?com\.?(?!\s+[ab])', r'b\.?com\.?\s+merit list', r'fybcom', r'merit.*fybcom'],
        'display': 'B.Com',
        'keywords': ['b.com', 'bcom', 'fybcom']
    },
    'it': {
        'patterns': [r'b\.?sc\.?\s*i\.?t\.?', r'f\.?y\.?b\.?sc\.?\s*i\.?t\.?', r'merit list.*it(?!\s+list)', r'bscit'],
        'display': 'B.Sc. Information Technology (IT)',
        'keywords': ['b.sc. it', 'bscit', 'f.y.b.sc.i.t']
    },
    'cs': {
        'patterns': [r'b\.?sc\.?\s*c\.?s\.?(?!\s+[a-z])', r'f\.?y\.?b\.?sc\.?\s*c\.?s\.?', r'computer science', r'bsccs'],
        'display': 'B.Sc. Computer Science (CS)',
        'keywords': ['b.sc. cs', 'bsccs', 'computer science']
    },
    'bms': {
        'patterns': [r'b\.?m\.?s\.?', r'fybms', r'management studies'],
        'display': 'BMS (Management Studies)',
        'keywords': ['bms', 'fybms', 'management studies']
    },
    'bammc': {
        'patterns': [r'b\.?a\.?m\.?m\.?c\.?', r'fybammc', r'multimedia'],
        'display': 'BAMMC (Multimedia & Mass Communication)',
        'keywords': ['bammc', 'fybammc', 'multimedia']
    },
    'ds': {
        'patterns': [r'b\.?sc\.?\s*d\.?s\.?', r'f\.?y\.?b\.?sc\.?\s*d\.?s\.?', r'data science', r'bscds'],
        'display': 'B.Sc. Data Science (DS)',
        'keywords': ['b.sc. ds', 'data science']
    },
    'ai': {
        'patterns': [r'b\.?sc\.?\s*a\.?i\.?', r'f\.?y\.?b\.?sc\.?\s*a\.?i\.?', r'artificial intelligence', r'bscai'],
        'display': 'B.Sc. Artificial Intelligence (AI)',
        'keywords': ['b.sc. ai', 'artificial intelligence']
    },
    'evs': {
        'patterns': [r'b\.?sc\.?\s*evs', r'environmental science', r'fyevs'],
        'display': 'B.Sc. Environmental Science (EVS)',
        'keywords': ['b.sc. evs', 'environmental science']
    },
}

UG_COURSES = [
    "B.Sc. Information Technology (IT) – 3 years – Intake: 120",
    "B.Sc. Computer Science (CS) – 3 years – Intake: 60",
    "B.Sc. Data Science (DS) – 3 years – Intake: 60",
    "B.Sc. Artificial Intelligence (AI) – 3 years – Intake: 60",
    "B.Com. (General) – 3 years – Intake: 240",
    "B.Com. (Banking & Insurance) – 3 years – Intake: 60",
    "B.Com. (Financial Markets) – 3 years – Intake: 60",
    "BMS (Management Studies) – 3 years – Intake: 120",
    "BAMMC (Multimedia & Mass Communication) – 3 years – Intake: 60",
]

PG_COURSES = [
    "M.Com. (Advanced Accountancy) – 2 years – Intake: 60",
    "M.Sc. Information Technology – 2 years – Intake: 30",
    "M.Sc. Computer Science – 2 years – Intake: 30",
    "M.Sc. Data Science – 2 years – Intake: 30",
    "M.Sc. Artificial Intelligence – 2 years – Intake: 30",
]

ADMISSION_PROCEDURE = """
*ADMISSION PROCEDURE AT SIES COLLEGE*

1. *Online Application*: Fill the online admission form at [https://siesascn.edu.in/admissions](https://siesascn.edu.in/admissions)

2. *Merit-Based Selection*: Admissions follow University of Mumbai (UoM) guidelines.

3. *Required Documents*:
   - SSC & HSC Marksheet (certified copy)
   - Transfer Certificate (TC)
   - Caste Certificate (if applicable)
   - Passport-size photographs (4 copies)
   - Aadhaar Card or valid ID

4. *Eligibility Criteria*: Varies by course. Check specific course requirements.

5. *Merit List Announcement*: Released periodically on the website.

6. *Fee Payment*: Online or at college office after selection.

7. *Final Registration*: Document verification and registration at college.

*Contact Info*:
- Website: [https://siesascn.edu.in/admissions](https://siesascn.edu.in/admissions)
- Phone: +91-22-2771 6450 / 2771 2799
- Email: [info@siesascn.edu.in](mailto:info@siesascn.edu.in)
"""

# --- Caching & Web Scraping ---
@st.cache_data(ttl=timedelta(hours=4))
def scrape_data():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    data = {"merit_lists": [], "admissions_link": "https://siesascn.edu.in/admissions"}

    try:
        resp = requests.get("https://siesascn.edu.in/admissions", headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            text = a.text.strip()
            href = a['href']
            if text and len(text) > 3:
                url = href if href.startswith('http') else "https://siesascn.edu.in" + href
                data['merit_lists'].append({
                    "text": text,
                    "url": url,
                    "text_lower": text.lower()
                })
    except Exception:
        pass

    return data

# --- Chatbot Logic ---
class CollegeAssistant:
    def __init__(self, data):
        self.data = data

    def detect_hod_department(self, question):
        q_lower = question.lower()
        if not any(word in q_lower for word in ["hod", "head of", "head", "department"]):
            return None
        
        # Prioritized keywords to avoid overlaps (e.g., economics before cs)
        dept_keywords = {
            'economics': ['economics', 'econ'],
            'commerce': ['commerce', 'comm', 'bcom', 'b.com'],
            'it': ['it', 'information technology'],
            'cs': ['cs', 'computer science'],
            'bms': ['bms', 'management'],
            'bammc': ['bammc', 'multimedia'],
            'accountancy': ['accountancy', 'accounting'],
            'banking': ['banking', 'insurance'],
            'evs': ['evs', 'environmental'],
        }
        
        # Check in order to prioritize economics
        for dept, keywords in dept_keywords.items():
            for kw in keywords:
                if kw in q_lower:
                    return dept
        
        return None

    def detect_merit_department(self, question):
        q_text = question.lower()
        q_text = re.sub(r'[^\w\s]', '', q_text)
        
        matches = {}
        for dept_key, dept_info in MERIT_PATTERNS.items():
            for pattern in dept_info['patterns']:
                if re.search(pattern, q_text, re.IGNORECASE):
                    matches[dept_key] = True
                    break
        
        priority = ['bcom', 'it', 'cs', 'bms', 'bammc', 'ds', 'ai', 'evs']
        for dept in priority:
            if dept in matches:
                return dept
        
        return None

    def filter_merit_lists(self, dept_key):
        filtered = []
        patterns = MERIT_PATTERNS[dept_key]['patterns']
        
        for item in self.data['merit_lists']:
            item_text = item['text_lower']
            item_clean = re.sub(r'[^\w\s]', '', item_text)
            
            for pattern in patterns:
                if re.search(pattern, item_clean, re.IGNORECASE):
                    if item not in filtered:
                        filtered.append(item)
                    break
        
        return filtered

    def find_answer(self, question):
        q_lower = question.lower()

        # Fee Structure queries (specific handling, before general FAQ)
        if any(word in q_lower for word in ["fee", "fees", "fee structure", "cost"]):
            return FEE_STRUCTURE_RESPONSE, "https://siesascn.edu.in/admissions"

        # Junior College queries
        if any(word in q_lower for word in ["junior college", "jc", "vice principal", "junior faculty"]):
            jc_html = '<div class="info-box"><b>Junior College Information</b><br><br>'
            jc_html += f'<b>Vice-Principal:</b> {JUNIOR_COLLEGE_INFO["vice_principal"]}<br><br>'
            jc_html += '<b>Faculty Members:</b><br>'
            for faculty in JUNIOR_COLLEGE_INFO["faculty"]:
                jc_html += f'<div class="course-item">{faculty}</div>'
            jc_html += '</div>'
            return jc_html, None

        # Library queries
        if any(word in q_lower for word in ["library", "librarian", "library staff"]):
            lib_html = f"""
<div class="info-box">
<b>Library Staff</b><br><br>
<b>Librarian:</b> {LIBRARY_INFO['librarian']}<br><br>
The college has a fully equipped library with e-resources, journals, and a digital learning hub.
</div>
"""
            return lib_html, None

        # General FAQ queries (excluding fee structure)
        if any(word in q_lower for word in ["faq", "frequently asked", "scholarships", "placement", "attendance", "hostel", "anti-ragging"]):
            faq_html = '<div class="success-box"><b>Frequently Asked Questions (FAQ)</b><br><br>'
            for faq in FAQS:
                faq_html += f'<div class="faq-item"><b>{faq["q"]}</b><br>{faq["a"]}</div>'
            faq_html += '</div>'
            return faq_html, None

        # Principal
        if any(word in q_lower for word in ["principal", "who is principal"]):
            return f"""
<div class="info-box">
<b>Principal of SIES College</b><br><br>
<b>Name:</b> {PRINCIPAL_INFO['name']}<br>
<b>Role:</b> {PRINCIPAL_INFO['role']}<br>
<b>Department:</b> {PRINCIPAL_INFO['department']}<br>
<b>Email:</b> {PRINCIPAL_INFO['email']}
</div>
""", None

        # HOD and Faculty
        hod_dept = self.detect_hod_department(question)
        if hod_dept:
            if hod_dept in FACULTY_DATA:
                info = FACULTY_DATA[hod_dept]
                dept_html = f'<div class="info-box"><b>Head of Department: {info["full_name"]}</b><br><br>'
                dept_html += f'<b>{info["hod"]}</b><br><br>'
                if 'vice_principal' in info:
                    dept_html += f'<b>Vice-Principal:</b> {info["vice_principal"]}<br><br>'
                dept_html += '<b>Faculty Members:</b><br>'
                for faculty in info['faculty']:
                    dept_html += f'<div class="course-item">{faculty}</div>'
                dept_html += '</div>'
                return dept_html, None

        # Merit Lists
        if any(word in q_lower for word in ["merit list", "merit", "merit lists"]):
            merit_dept = self.detect_merit_department(question)
            
            if not merit_dept:
                return f"""
<div class="error-box">
Please specify a department. Available: B.Com, IT, CS, BMS, BAMMC, DS, AI, EVS
</div>
""", None
            
            filtered = self.filter_merit_lists(merit_dept)
            
            if filtered:
                dept_name = MERIT_PATTERNS[merit_dept]['display']
                merit_html = '<div class="merit-list-container">'
                merit_html += f'<b>Merit Lists for {dept_name}</b><br><br>'
                
                for item in filtered:
                    merit_html += f'<div class="merit-item"><a href="{item["url"]}" target="_blank">{item["text"]}</a></div>'
                
                merit_html += f'<div class="total-count">Total Merit Lists Released: {len(filtered)}</div>'
                merit_html += '</div>'
                
                return merit_html, "https://siesascn.edu.in/admissions"
            else:
                dept_name = MERIT_PATTERNS[merit_dept]['display']
                return f"""
<div class="error-box">
No merit lists found for {dept_name}. Check back soon!
</div>
""", "https://siesascn.edu.in/admissions"

        # UG Courses
        if any(w in q_lower for w in ["undergraduate", "ug", "bachelor"]) and not any(w in q_lower for w in ["post", "pg", "master"]):
            html = '<div class="success-box"><b>Undergraduate Programs</b><br><br>'
            for course in UG_COURSES:
                html += f'<div class="course-item">{course}</div>'
            html += '</div>'
            return html, None

        # PG Courses
        if any(w in q_lower for w in ["postgraduate", "pg", "master", "msc", "mcom"]):
            html = '<div class="success-box"><b>Postgraduate Programs</b><br><br>'
            for course in PG_COURSES:
                html += f'<div class="course-item">{course}</div>'
            html += '</div>'
            return html, None

        # All Courses
        if any(w in q_lower for w in ["all courses", "courses offered"]):
            html = '<div class="success-box"><b>All Courses at SIES College</b><br><br><b>Undergraduate:</b><br>'
            for course in UG_COURSES:
                html += f'<div class="course-item">{course}</div>'
            html += '<br><b>Postgraduate:</b><br>'
            for course in PG_COURSES:
                html += f'<div class="course-item">{course}</div>'
            html += '</div>'
            return html, None

        # Admission Procedure
        if any(w in q_lower for w in ["admission", "apply", "procedure", "requirements"]):
            return ADMISSION_PROCEDURE, "https://siesascn.edu.in/admissions"

        return """
<div class="info-box">
<b>How can we assist you?</b><br><br>
Our admission assistant can help with:<br>
• HOD Information<br>
• Merit Lists<br>
• Courses (Undergraduate & Postgraduate)<br>
• Admission Procedure<br>
• Principal Information<br>
• Junior College Details<br>
• Library Staff<br>
• FAQs<br><br>
Please select an option or ask your question below.
</div>
""", None

# --- Main App ---
st.markdown("""
<div class="header-container">
    <div class="logo-section">
        <div class="sies-logo">🎓</div>
        <div class="college-name">SIES</div>
        <div class="college-subtitle">Rise With Education</div>
    </div>
    <div class="main-header">Admission Assistant</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='subheader'>Your Gateway to Excellence | Official Admission Portal</div>", unsafe_allow_html=True)

with st.spinner("Loading college information..."):
    live_data = scrape_data()
assistant = CollegeAssistant(live_data)

if 'messages' not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """
<div class="info-box">
<b>Welcome to SIES College Admission Assistant</b><br><br>
Explore information about our programs, faculty, and admission procedures. Use the quick links below or ask any questions about SIES College.
</div>
"""
    }]

# --- Chat Display ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# --- Chat Input ---
if prompt := st.chat_input("Ask about admissions, courses, merit lists, or faculty..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp, link = assistant.find_answer(prompt)
            full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
            st.markdown(full_resp, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_resp})

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='sidebar-header'>Quick Navigation</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-section-title">Admission Information</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("B.Com Merit Lists", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Show B.Com merit lists"})
        resp, link = assistant.find_answer("Show B.Com merit lists")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    if st.button("UG Courses", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "UG courses"})
        resp, link = assistant.find_answer("UG courses")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    if st.button("PG Courses", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "PG courses"})
        resp, link = assistant.find_answer("PG courses")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    if st.button("Admission Procedure", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Admission procedure"})
        resp, link = assistant.find_answer("Admission procedure")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()

    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-section-title">Additional Information</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Junior College", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Junior College details"})
        resp, link = assistant.find_answer("Junior College details")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    if st.button("Library Staff", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Librarian information"})
        resp, link = assistant.find_answer("Librarian information")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    if st.button("FAQs", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "FAQs"})
        resp, link = assistant.find_answer("FAQs")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-section-title">Faculty Information</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Principal", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Who is the Principal?"})
        resp, link = assistant.find_answer("Who is the Principal?")
        full_resp = resp + (f"\n\n[Visit Admissions Page]({link})" if link else "")
        st.session_state.messages.append({"role": "assistant", "content": full_resp})
        st.rerun()
    
    st.divider()
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": """
<div class="info-box">
<b>Welcome to SIES College Admission Assistant</b><br><br>
Explore information about our programs, faculty, and admission procedures. Use the quick links below or ask any questions about SIES College.
</div>
"""}]
        st.rerun()

# --- Contact Section (Footer-like) ---
st.markdown("""
<div class="contact-section">
<b>Contact SIES College</b><br><br>
For more details, visit our official website or reach out via email/phone.<br>
<a href="https://siesascn.edu.in" target="_blank">siesascn.edu.in</a> | [info@siesascn.edu.in](mailto:info@siesascn.edu.in) | +91-22-2771 6450
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer-text'>© 2025 SIES College of Arts, Science & Commerce. All rights reserved.</div>", unsafe_allow_html=True)
