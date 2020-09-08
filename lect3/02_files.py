import wget
import os.path

if __name__ == '__main__':
    link = 'https://uc7cc7dc63fa4965bcbeb9aeaded.dl.dropboxusercontent.com/cd/0/get/A_D4XjWoY777ZX4HGLMEGo-DMut9goft49NbfGp1QvGqFyFn8g2hrH4w4n5X8H4W6k-g5fC-7U_gJE1qYEmI7oxZ3lcrF3QyVrMkaEJU2ojDpw/file?_download_id=15034702969671887726724878419158280277208332200849467166478379979&_notify_domain=www.dropbox.com&dl=1'
    if not os.path.isfile('referat.txt'):
        wget.download(link, 'referat.txt')
    with open('referat.txt', 'r', encoding='utf-8') as f:
        file_content = f.read()
    print(f"Words quantity is equal to {len(file_content.split(' '))}")
    new_content = file_content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(new_content)
