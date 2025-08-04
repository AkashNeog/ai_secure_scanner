import streamlit as st
from vuln_scanner import scan_code

st.title("🔐 AI Secure Code Scanner")
uploaded_file = st.file_uploader("Upload a Python file to scan", type="py")

if uploaded_file:
    code = uploaded_file.read().decode()
    st.code(code, language='python')

    with open("temp_uploaded.py", "w") as f:
        f.write(code)

    st.info("🔎 Scanning...")
    graph, comments, vulnerabilities = scan_code(code, "temp_uploaded.py")

    st.subheader("🧠 NLP: Suspicious Comments")
    for c in comments:
        st.warning(f"{c['comment']} → Reason: {c['reason']}")

    st.subheader("🕸️ AST: Potential Vulnerabilities")
    for v in vulnerabilities:
        st.error(f"{v['type']} → {v['reason']}")

    st.success("✅ Scan complete")
