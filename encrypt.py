from cryptography.fernet import Fernet
import base64, hashlib

# Step 1: Master secret (choose your own strong string, don't share this)
MASTER_SECRET = "MySecretKeyForApp"

# Step 2: DB fingerprint (this locks the password to THIS database only)
DB_FINGERPRINT = "localhost:3306_sakila"

# Step 3: Generate key based on secret + DB fingerprint
salt = hashlib.sha256(DB_FINGERPRINT.encode()).digest()
key = base64.urlsafe_b64encode(
    hashlib.pbkdf2_hmac('sha256', MASTER_SECRET.encode(), salt, 100000, dklen=32)
)

# Step 4: Encrypt your real MySQL password
cipher = Fernet(key)
real_password = "MySQLrealPassword123"  # Replace with your real MySQL password
encrypted_password = cipher.encrypt(real_password.encode())

print("🔒 Encrypted password, save this safely:")
print(encrypted_password)
