import requests
from bs4 import BeautifulSoup
import argparse
import os

# Here will be functions for processing different input options.
def search_full_name(name):
    # search logic for fulname
    split_name = name.split(" ")
    first_name = split_name[0]
    last_name = split_name[1]
    url = f"https://www.whitepages.be/Search/Person/?what={first_name}+{last_name}&where="
    response = requests.get(url)
    html_content = response.content.decode("utf-8")
    soup = BeautifulSoup(html_content, 'html.parser')
    # address search
    address_span = soup.find('span', class_='wg-address')
    address = address_span.get_text(strip=True) if address_span else "Address is not found"

    # phone search
    data_small_result = soup.find('div', class_='wg-results-list__item')['data-small-result']
    phone = "Phone is not found"
    if data_small_result:
        data_small_result_dict = eval(data_small_result.replace('&quot;', '"'))
        phone = data_small_result_dict.get("phone", "Phone is not found")
    
    return address, phone, first_name, last_name

# Create dictionary for results
user_social = {}
# Launching a scan on the namecheckup service.
def serv_namecheckup(service, username, url):
    # add headers, we need place here referer, without it data not return
    headers = {
        'referrer': '/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36',
        'accept': '*/*',
    }
    # dictionary wwith username and social network
    data = {
        'data[name]': username,
        'data[media]': service,
        'data[tx]': '1'
    }

    # Making a request to check the social network specified in the parameters
    # and receiving the response in JSON format
    # Extracting the necessary data, specifically, the unavailability for registration
    # This will indicate the existence of this username in the service
    # Adding to the dictionary
    try:
        response = requests.post('https://namecheckup.com/api/v1/media/check', headers=headers, data=data).json()
        if response['data']['available'] == False:
            if username not in user_social:
                user_social[username] = dict()
            if str(response['data']['media']).lower() not in user_social[username]:
                user_social[username][str(response['data']['media']).lower()] = url
        # print(user_social)
        return user_social
    except Exception as e:
        print(f"Error: {e}") 

# create dictionary with services for namecheckup
service_namecheckup = {
                    'facebook': f'https://www.facebook.com/',
                    'youtube': f'https://www.youtube.com/',
                    'github': f'https://github.com/',
                    'telegram': f'https://telegram.me/',
                    'bitbucket': f'https://bitbucket.org/'
}
def search_username(username):
    # Scanning services and sending requests
    for service, base_url in service_namecheckup.items():
        full_url = f"{base_url}{username}"
        try:
           user_social = serv_namecheckup(service, username, full_url)
        except Exception as e:
            print(f"Error {service}: {e}")

    return user_social

def get_ip_info(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()
    not_data = "Not data"
    country = data.get("country", not_data)
    city = data.get("regionName", not_data)  # Use get method for to avoid KeyError
    isp = data.get("isp", not_data)
    lat = data.get("lat", not_data)
    lon = data.get("lon", not_data)
    return country, city, isp, lat, lon

def format_user_social(user_social):
    # create list for result
    formatted_results = []
    # iterate through all services from the global dictionary.
    for service in service_namecheckup.keys():
        # check if the service is in the search results.
        status = "Yes" if service in user_social else "No"
        formatted_results.append(f"{service}: {status}")
    return '\n'.join(formatted_results)

def save_result_to_file(result, filename="result.txt"):
    if os.path.exists(filename):
        i = 1
        while True:
            new_filename = f"{filename.split('.')[0]}_{i}.txt"
            if not os.path.exists(new_filename):
                filename = new_filename
                break
            i += 1
    with open(filename, "a") as file:
        file.write(result + "\n")
    return filename

def main():
    parser = argparse.ArgumentParser(description='Welcome to passive v1.0.0')
    parser.add_argument('-fn', '--fullname', help='Search with full-name')
    parser.add_argument('-ip', '--ipaddress', help='Search with ip address')
    parser.add_argument('-u', '--username', help='Search with username')
    args = parser.parse_args()

    if args.fullname:
        address, phone, first_name, last_name = search_full_name(args.fullname)
        result = f"First name: {first_name}\nLast name: {last_name}\nAddress: {address}\nNumber: {phone}"
        filename = save_result_to_file(result)
        print(f"{result}\nSaved in {filename}")
    elif args.ipaddress:
       country, city, isp, lat, lon = get_ip_info(args.ipaddress)
       result = f"ISP: {isp}\nCity, country: {city}, {country}\nLat/Lon: {lat}/{lon}"
       filename = save_result_to_file(result)
       print(f"{result}\nSaved in {filename}")
    elif args.username:
       user_social = search_username(args.username)
       formated_result = format_user_social(user_social[args.username])
       filename = save_result_to_file(formated_result)
       print(f"{formated_result}\nSaved in {filename}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
