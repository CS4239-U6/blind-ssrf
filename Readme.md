# Blind SSRF

Blind SSRF arises when an application can be induced to issue a backend HTTP request to a supplied URL,
but the response from the backend request is not returned in the application's frontend response.
In other words, the attacker cannot exactly see the result of their actions, i.e. "blind".

## What is the effect of Blind SSRF?

The impact of Blind SSRF is lower than that of their fully-informed counterpart because of their one-way nature.
They cannot be easily exploited by the user to receive backend information.

## How do attackers know that requests are firing off?

It is usually checked via sending a HTTP request from a vulnerable system to an external system that is controlled by the malicious attacker.

If a HTTP request is observed by an attacker, then it is vulnerable to SSRF.

## Quick Start

1. Clone the repo with `git clone https://github.com/CS4239-U6/blind-ssrf.git`.
1. Install requirements using `pip3 install -r requirements.txt`.
1. Run the vulnerable server using `python3 VulnerableServer/__main__.py`.


## How to exploit?

As this is a blind SSRF, the attacker does not know the result of the request. In order to view the results, follow the instructions below
1. Go to [https://webhook.site/](https://webhook.site/) to get a url representing the webhook.
2. Copy the link from the website. EG: `https://webhook.site/{some_uuid_here}`
3. Paste it into the server's `/` route.
4. Press submit and watch the `https://webhook.site` panel reflect a request from the server

Even though we are unable to physically see the request from the server, the SSRF still happens as observed from the [https://webhook.site](https://webhook.site) request.

## Tech Stack

1. `flask`: Web framework.
1. `selenium`: For screenshot functionalities.
