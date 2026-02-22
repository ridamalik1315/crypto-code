## Cyber Cipher Lab

An educational cyber-security themed web app built on your existing Python cipher scripts. It lets you experiment with:

- XOR cipher (encode / decode)
- Permutation cipher (encode / decode)
- RSA cipher (encode / decode, given key parameters)
- MD5 brute-force of 3-character strings

### Running the project

1. **Create a virtual environment (recommended)**

```bash
python -m venv .venv
.venv\Scripts\activate  # on Windows PowerShell
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Start the web app**

```bash
python app.py
```

4. **Open in your browser**

Navigate to `http://127.0.0.1:5000` and you should see the Cyber Cipher Lab interface.

### Notes

- RSA requires you to supply a valid exponent and modulus `(e or d, n)` — you can generate these using your existing `RSA_key_generator.py` script.
- The MD5 demo only brute-forces all 3-character strings made from letters and digits for a given MD5 hash. It is for educational purposes only.

