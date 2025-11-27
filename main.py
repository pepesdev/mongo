from model import User, get_connection

def insert_sample_data():
    users_data = [
        {"name":"Jose Hernandez","email":"hedzjames@gmail.com"},
        {"name":"Berenice Alvarado","email":"bere_1234@gmail.com"}
    ]
    created_users=[]
    for user_data in users_data:
        user = User(**user_data)
        user.save()
        created_users.append(user)
    
    print(f"inserted {len(created_users)} users successfully")

if __name__ == "__main__":
    get_connection()
    insert_sample_data()