from app import create_app
from models import User

app = create_app()
with app.app_context():
    user = User.query.filter_by(email='otp_test_user@gmail.com').first()
    if user:
        print(f"OTP for {user.email}: {user.reset_otp}")
    else:
        print("User not found")
