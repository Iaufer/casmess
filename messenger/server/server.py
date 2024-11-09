import socket
import threading

from casmess.messenger.db.db import add_username_to_file


def handle_client(client_socket):
    try:
        client_socket.send(
            "Вы хотите:\n1. Зарегистрироваться\n2. Войти\n3. Сменить пароль\n:".encode('utf-8'))

        choice = client_socket.recv(1024).decode('utf-8').strip()

        if choice == '1':
            client_socket.send("Вы выбрали регистрацию. Пожалуйста, введите имя пользователя:".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8')
            client_socket.send(f"Регистрация для {username} прошла успешно.".encode('utf-8'))

            add_username_to_file(username) # сделать проверку на уже имеющийся, может позже переделать под postgresql

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

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)
    print("Server started on port 8080")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
if __name__ == "__main__":
    start_server()
