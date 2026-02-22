from flask import Flask, render_template, request, Response

from crypto_algorithms import (
    xor_encrypt,
    xor_decrypt,
    permutation_encrypt,
    permutation_decrypt,
    rsa_encrypt,
    rsa_decrypt,
    md5_bruteforce_3char,
)

app = Flask(__name__)

CIPHERS = [
    {"id": "xor", "name": "XOR Cipher"},
    {"id": "perm", "name": "Permutation Cipher"},
    {"id": "rsa", "name": "RSA Cipher"},
    {"id": "md5", "name": "MD5 Brute Force (3 chars)"},
]


def _process_cipher_form(form_data):
    result = None
    error = None

    cipher = form_data.get("cipher")
    mode = form_data.get("mode")
    text = form_data.get("text", "")
    key = form_data.get("key", "")
    exponent_raw = form_data.get("exponent", "")
    modulus_raw = form_data.get("modulus", "")
    hash_value = form_data.get("hash_value", "")

    try:
        if cipher == "xor":
            if mode == "encode":
                result = xor_encrypt(text, key)
            else:
                result = xor_decrypt(text, key)

        elif cipher == "perm":
            if mode == "encode":
                result = permutation_encrypt(text, key)
            else:
                result = permutation_decrypt(text, key)

        elif cipher == "rsa":
            if not exponent_raw or not modulus_raw:
                raise ValueError("Exponent and modulus are required for RSA.")

            exponent = int(exponent_raw)
            modulus = int(modulus_raw)

            if mode == "encode":
                result = rsa_encrypt(text, exponent, modulus)
            else:
                result = rsa_decrypt(text, exponent, modulus)

        elif cipher == "md5":
            if mode == "encode":
                raise ValueError("This MD5 demo only supports cracking 3-character strings by hash.")

            if not hash_value:
                raise ValueError("Please enter an MD5 hash to crack.")

            cracked = md5_bruteforce_3char(hash_value)
            if cracked is not None:
                result = f"Found matching 3-character string: {cracked}"
            else:
                result = "No matching 3-character string found in the search space."

        elif cipher:
            error = "Unknown cipher selected."

    except Exception as exc:  # noqa: BLE001
        error = str(exc)

    return result, error


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    form = {}

    if request.method == "POST":
        cipher = request.form.get("cipher")
        mode = request.form.get("mode")
        text = request.form.get("text", "")
        key = request.form.get("key", "")
        exponent_raw = request.form.get("exponent", "")
        modulus_raw = request.form.get("modulus", "")
        hash_value = request.form.get("hash_value", "")

        form = {
            "cipher": cipher,
            "mode": mode,
            "text": text,
            "key": key,
            "exponent": exponent_raw,
            "modulus": modulus_raw,
            "hash_value": hash_value,
        }

        result, error = _process_cipher_form(form)

    return render_template("index.html", ciphers=CIPHERS, result=result, error=error, form=form)


@app.route("/export", methods=["POST"])
def export():
    form = {
        "cipher": request.form.get("cipher"),
        "mode": request.form.get("mode"),
        "text": request.form.get("text", ""),
        "key": request.form.get("key", ""),
        "exponent": request.form.get("exponent", ""),
        "modulus": request.form.get("modulus", ""),
        "hash_value": request.form.get("hash_value", ""),
    }

    result, error = _process_cipher_form(form)

    if error:
        return Response(f"Error: {error}", status=400, mimetype="text/plain")

    if not result:
        return Response("No output to export.", status=400, mimetype="text/plain")

    cipher = form.get("cipher") or "cipher"
    mode = form.get("mode") or "encode"
    filename = f"{cipher}_{mode}_output.txt"

    return Response(
        result,
        mimetype="text/plain; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.route("/learn")
def learn():
    return render_template("learn.html", ciphers=CIPHERS)


if __name__ == "__main__":
    app.run(debug=True)

