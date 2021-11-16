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

## Tech Stack

1. `flask`: Web framework.
1. `selenium`: For screenshot functionalities.
