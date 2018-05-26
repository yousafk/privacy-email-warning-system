import httplib2, pygame, sys, time, os, getpass 
from xml.dom.minidom import parseString

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
gmail_feed_url = "https://mail.google.com/mail/feed/atom"
privacy_ids = []

def auth(username, password):
    http = httplib2.Http()
    http.add_credentials(username, password)

    return http

def get_feed(http):
    resp, content = http.request(gmail_feed_url , "GET", body={}, headers={'Content-Type': 'application/atom+xml'})
    return resp, content

def parse_feed(content):
    try:
        dom = parseString(content)
        feed_list = dom.getElementsByTagName('entry')
        result = []
        for feed in feed_list:
            entry = {'email_id': feed.getElementsByTagName('id')[0].firstChild.nodeValue.strip(),
            'title': feed.getElementsByTagName('title')[0].firstChild.nodeValue.strip()}
            result.append(entry)
        return result
    except:
        pass

def alert_for_privacy(result):
    full_path = os.path.join(APP_FOLDER, "sound.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(full_path)
    
    try:
        for r in result:
            if 'privacy' in r['title'].lower() and r['email_id'] not in privacy_ids:
                pygame.mixer.music.play()
                time.sleep(2)
                privacy_ids.append(r['email_id'])
    except:
        pass

def prompt_credentials():
    username = input('Please enter username without @gmail: ')
    password = getpass.getpass('Please enter password: ')
    return username, password

if __name__ == "__main__":
    username, password = prompt_credentials()
    http = auth(username, password)
    resp, feed = get_feed(http)

    while resp.status != 200:
        print("Unable to connect with username and password. Please try again.\n")
        username, password = prompt_credentials()
        resp, feed = get_feed(auth(username, password))

    print("Gilfoyle's privacy warning system has begun. Anytime you receive an email with the subject privacy involved, it'll go off :)")

    while True:
        try:
            resp, feed = get_feed(http)
            alert_for_privacy(parse_feed(feed))
            time.sleep(10)
        except:
            print("Encountered an error.")
            break
