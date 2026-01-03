from app import create_app, db
from models import User
import sys

def setup():
    app = create_app()
    with app.app_context():
        print("Initializing Database...")
        db.create_all()
        
        # --- Create Default Admin ---
        admin_username = "Vrushabhsakhiya"
        admin_pass = "@VrU(846)"
        
        user = User.query.filter_by(username=admin_username).first()
        
        if not user:
            print(f"Creating Admin User: {admin_username}...")
            user = User(
                username=admin_username,
                role='master',
                permissions='all',
                is_verified=True
            )
            user.set_password(admin_pass)
            db.session.add(user)
            db.session.commit()
            print("Admin User Created Successfully!")
        else:
            print(f"Admin User {admin_username} already exists. Updating password/role...")
            user.role = 'master'
            user.set_password(admin_pass)
            db.session.commit()
            print("Admin User Updated Successfully!")

        # --- Optional: Prompt for extra admin ---
        # Uncomment if interactive creation is desired
        # print("\nDo you want to create an extra admin? (y/n)")
        # ...
        
        print("\n" + "="*40)
        print("          SETUP COMPLETE          ")
        print("="*40)
        print(f" Admin Username : {admin_username}")
        print(f" Admin Password : {admin_pass}")
        print("="*40 + "\n")
        print("You can now run 'python app.py' to start the server.")

if __name__ == '__main__':
    setup()
