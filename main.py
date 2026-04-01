from model import User, get_connection

def insert_sample_data():
    users_data = [
        {"name":"Jose Hernandez","email":"hedz@gmail.com"},
        {"name":"Berenice Alvarado","email":"bere_1234@gmail.com"}
    ]
    created_users=[]
    for user_data in users_data:
        user = User(**user_data)
        user.save()
        created_users.append(user)
    
    print(f"inserted {len(created_users)} users successfully")

def get_all_users():
    users = User.objects()
    for user in users:
        print(f"{user.name} - {user.email}")
    return list(users)

def get_user_by_email(email):
    return User.objects(email=email).first()
  
if __name__ == "__main__":
    get_connection()
    insert_sample_data()
    print("\n--- ALL USERS ---")
    get_all_users()
    
    print("\n--- FIND ONE ---")
    user = get_user_by_email("hedz@gmail.com")
    if user:
        print(user.name)