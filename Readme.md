# Blind SSRF

Blind SSRF arises when an application can be indeced to issue a back-end HTTP request to a supplied URL, but the response from the backend-request is not returned in the application's front-end response.

## What is the effect of blind SSRF?

The impact of blind SSRF is lower than that of the fully informed SSRF because of their one way nature. They cannot be easily exploited by the user to receive backend information.

## How is it detected?

It is usually detected by sending a http request from a vulnerable system to an external system that is controlled by the malicious attacker.

If a http request is observed by an attacker, then it is vulnerable to SSRF.


# Quick Start
1. Clone the repo with `git clone https://github.com/CS4239-U6/blind-ssrf.git`
2. Go to the vulnerable server using `cd "vulnerable server"`
3. Install requirements using `pip install -r requirements.txt`
4. Run the file using `python __main__.py`


# Tech stack
1. flask - web framework
2. selenium - screenshot functions