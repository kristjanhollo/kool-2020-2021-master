current_users = ["user01", "user02", "user03", "user04", "user05", "user06"]
new_users = ["user10", "user11", "user02", "user03", "john"]

for users in new_users:
    if users in current_users:
        print(f"Please enter new username: {users}")
    else:
        print(f"Username is available: {users}")

