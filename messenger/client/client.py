import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 8080))

    initial_message = client.recv(1024).decode('utf-8')
    print(initial_message)

    action_choice = input("Введите номер действия: ")
    client.send(action_choice.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    print(response)

    username = input("Введите имя пользователя: ")
    client.send(username.encode('utf-8'))

    final_response = client.recv(1024).decode('utf-8')
    print(final_response)

    client.close()

if __name__ == "__main__":
    start_client()
