import os
import multiprocessing as mp

# For Website
from uuid import uuid4
from flask import Flask, request, render_template, flash, redirect, g

# For screenshot
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


app = Flask(__name__)
app.secret_key = uuid4().hex


keys = ('title', 'link', 'body')
report_template = """
# {title}

## Link
{link}

## Screenshot
![screenshot]({ss_link})

## Message body

{body}
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    # Input validation
    result = request.form
    for i in keys:
        if i in result and len(result[i]) > 0:
            continue
        flash(f'{i.title()} is required', 'error')
        return redirect('/')

    # Help the admin generate a report on the website
    uid = uuid4().hex
    link = result['link']
    mp.Process(target=generate_whole_report, args=(
        uid, link, result['title'], result['body'])).start()

    flash(f'Form submitted successfully. Report ID: {uid}', 'success')
    return redirect('/')


def generate_whole_report(uid: str, link: str, title: str, body: str):
    ss_link = get_screenshot(link, uid)
    generateReport(uid, title, body, link, ss_link)


def get_screenshot(link: str, uid: str):
    save_path = f'screenshots/{uid}.png'
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    sleep(3)
    data = driver.get_screenshot_as_png()
    with open(save_path, 'wb') as f:
        f.write(data)
    driver.close()
    driver.quit()
    return save_path


def generateReport(uid: str, title: str, body: str, link: str, ss_link: str):
    save_path = f'./report/{uid}.md'
    out_format = report_template.format(
        title=title, link=link, body=body, ss_link=os.path.join('..', ss_link))
    with open(save_path, 'w') as f:
        f.write(out_format)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
