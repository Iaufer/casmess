def handle_client(client_socket):
    try:
        client_socket.send(
            "Вы хотите:\n1. Зарегистрироваться\n2. Войти\n3. Сменить пароль\n:".encode('utf-8')
        )

        choice = client_socket.recv(1024).decode('utf-8').strip()

        if choice == '1':
            client_socket.send("Вы выбрали регистрацию. Пожалуйста, введите имя пользователя:".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8')
            client_socket.send(f"Регистрация для {username} прошла успешно.".encode('utf-8'))

        elif choice == '2':
            client_socket.send("Вы выбрали вход. Пожалуйста, введите имя пользователя:".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8')
            client_socket.send(f"Добро пожаловать, {username}!".encode('utf-8'))

        elif choice == '3':
            client_socket.send("Вы выбрали смену пароля. Пожалуйста, введите ваше имя пользователя:".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8')
            client_socket.send(f"Пароль для {username} был успешно изменен.".encode('utf-8'))

        else:
            client_socket.send("Неверный выбор. Пожалуйста, перезапустите программу.".encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
