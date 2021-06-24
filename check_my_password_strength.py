import sys
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the api and try again')
    return response


def read_response(response):
    print(response.text)


def get_password_leaks_count(pw_hashes, pw_hash_to_check):
    pw_hashes = (line.split(':') for line in pw_hashes.text.splitlines())
    for h, count in pw_hashes:  # h is the tail of the pw hashes, whose first 5 chars match with your pw
        #print(h, count)
        if h == pw_hash_to_check:
            return count
    return 0


# check password if it exists in API response.
def pwned_api_check(password):
    # converting password into sha1
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    #print(first5_char, tail)
    response = request_api_data(first5_char)
    #print(response)
    # return read_response(response)
    return get_password_leaks_count(response, tail)


args = input('Enter the passwords you want to check: ')
user_entered = args.split()
print(user_entered)

for password in user_entered:
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times, you should probably change it ...')
    else:
        print(f'{password} was not found, that is a good password')

'''
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, you should probably change it ...')
        else:
            print(f'{password} was not found, that is a good password')
    return 'done !'


main(sys.argv[1:])
'''
