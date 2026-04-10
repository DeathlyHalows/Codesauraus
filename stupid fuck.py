import streamlit as st
import hashlib
import time
from ecdsa import SigningKey, SECP256k1
from cryptography.fernet import Fernet
import base64
import os

st.set_page_config(page_title="Quantum Crypto Demo", layout="wide")

st.title("🔐 Quantum vs Classical Cryptography Demo")

st.markdown("""
This demo shows why **ECDSA breaks under quantum computers** and why  
**Post-Quantum Cryptography (PQC)** remains secure.

---
""")

col1, col2 = st.columns(2)

# =========================
# 🔴 ECDSA PANEL
# =========================
with col1:
    st.header("🔴 Traditional Messaging (ECDSA)")

    if st.button("Generate ECDSA Keys"):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.verifying_key

        st.session_state.ecdsa_sk = sk
        st.session_state.ecdsa_vk = vk

        st.success("Keys Generated")

    message = st.text_input("Enter Message (ECDSA)", "Hello Quantum World")

    if st.button("Send Message (ECDSA)"):
        if "ecdsa_sk" not in st.session_state:
            st.error("Generate keys first!")
        else:
            msg_hash = hashlib.sha256(message.encode()).digest()
            signature = st.session_state.ecdsa_sk.sign(msg_hash)

            st.session_state.ecdsa_signature = signature
            st.session_state.ecdsa_message = message

            st.success("Message Signed & Sent")

    if st.button("Quantum Attack on ECDSA 💥"):
        if "ecdsa_signature" not in st.session_state:
            st.warning("Send a message first!")
        else:
            with st.spinner("Quantum computer running Shor's Algorithm..."):
                time.sleep(2)

            st.error("🚨 PRIVATE KEY RECOVERED!")
            st.error("🚨 MESSAGE COMPROMISED!")

            st.code("""
Simulated Attack:
- Elliptic Curve Discrete Log Problem broken
- Private key derived from public key
- Signature forgeable
""")

# =========================
# 🟢 PQC PANEL
# =========================
with col2:
    st.header("🟢 Post-Quantum Messaging (PQC - Kyber Style)")

    if st.button("Generate PQC Keys"):
        # Simulated PQC key (random secure key)
        key = Fernet.generate_key()

        st.session_state.pqc_key = key
        st.success("Post-Quantum Key Generated")

    pqc_message = st.text_input("Enter Message (PQC)", "Hello Secure Future")

    if st.button("Send Message (PQC)"):
        if "pqc_key" not in st.session_state:
            st.error("Generate keys first!")
        else:
            f = Fernet(st.session_state.pqc_key)
            encrypted = f.encrypt(pqc_message.encode())

            st.session_state.pqc_cipher = encrypted

            st.success("Message Encrypted with PQC")
            st.code(encrypted)

    if st.button("Quantum Attack on PQC 🚀"):
        if "pqc_cipher" not in st.session_state:
            st.warning("Send a message first!")
        else:
            with st.spinner("Quantum computer attempting attack..."):
                time.sleep(2)

            st.success("✅ ATTACK FAILED")
            st.success("✅ MESSAGE STILL SECURE")

            st.code("""
Reason:
- Based on lattice problems (Kyber-like)
- No known efficient quantum attack
- Resistant to Shor's Algorithm
""")

# =========================
# 📊 COMPARISON SECTION
# =========================

st.markdown("---")
st.header("📊 Security Comparison")

st.table({
    "Feature": [
        "Underlying Problem",
        "Quantum Resistance",
        "Used Today",
        "Future Security"
    ],
    "ECDSA": [
        "Elliptic Curve Discrete Log",
        "❌ Broken by Shor",
        "✅ Yes",
        "❌ Unsafe"
    ],
    "PQC (Kyber-style)": [
        "Lattice-based",
        "✅ Resistant",
        "⚠️ Emerging",
        "✅ Safe"
    ]
})

# =========================
# 🧠 EDUCATIONAL SECTION
# =========================

st.markdown("---")
st.header("🧠 Explanation")

st.markdown("""
### 🔴 Why ECDSA Fails
- Based on **Elliptic Curve Discrete Log Problem**
- Quantum computers use **Shor’s Algorithm**
- Can derive private key from public key

### 🟢 Why PQC Works
- Based on **lattice problems**
- No efficient quantum algorithm known
- Used in modern secure systems (inspired by Spixi)

---
""")

# =========================
# 🎯 FINAL RESULT
# =========================

st.markdown("## 🎯 Final Verdict")

st.success("""
✔ Classical crypto (ECDSA) is NOT future-proof  
✔ Quantum computers will break it  
✔ Post-Quantum Cryptography is the future  
✔ Systems like Spixi are already preparing for this  
""")