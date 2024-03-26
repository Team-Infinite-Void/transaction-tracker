import pyotp
import qrcode

def generate_secret():
    """Generate a secret key."""
    return pyotp.random_base32()

def generate_totp_uri(secret, user_email="user@example.com", issuer_name="YourApp"):
    """Generate a provisioning URI for a TOTP QR code."""
    return pyotp.totp.TOTP(secret).provisioning_uri(name=user_email, issuer_name=issuer_name)

def generate_qr_code(uri):
    """Generate a QR code from the TOTP URI."""
    qr = qrcode.make(uri)
    qr.save("totp_setup.png")
    print("QR code saved as totp_setup.png. Scan it with Google Authenticator.")

def generate_and_verify_otp(secret):
    """Generate an OTP and prompt for verification."""
    totp = pyotp.TOTP(secret)
    otp = totp.now()

    print("Current OTP:", otp)  # Print the OTP generated
    user_provided_otp = input("Enter the OTP from Google Authenticator: ")
    # Increase the verification window
    if totp.verify(user_provided_otp, valid_window=1):
        print("The OTP is valid.")
    else:
        print("The OTP is invalid.")

def main():
    # Generate a secret key for a new user
    secret = generate_secret()
    print("Secret key (store securely):", secret)

    # Generate a provisioning URI and QR code for the user
    totp_uri = generate_totp_uri(secret, "user@example.com", "YourApp")
    print("Provisioning URI (for testing, typically encoded in QR):", totp_uri)
    generate_qr_code(totp_uri)

    # Demonstration of OTP generation and verification
    generate_and_verify_otp(secret)

if __name__ == "__main__":
    main()
