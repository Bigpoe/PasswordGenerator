from scripts.create_entry.new_entry import CreateEntry
from scripts.save_password.save_entry import SaveEntry


if __name__ == '__main__':
    create_entry = CreateEntry()
    url_name = create_entry.ask_url()
    username = create_entry.ask_username()
    password = create_entry.generate_password()

    create_entry = SaveEntry()
    create_entry.save_entry(url_name, username, password)
    
    print('-' * 20 )
    print(f'URL: {url_name}\nUsername: {username}\nThis is your password: {password} ')
