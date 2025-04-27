Pin Cracker
Overview
This project is a Python-based brute force script designed to guess a PIN code for an HTTP application running on a specific port. The script simulates multiple PIN attempts and looks for a success response from the server. The challenge involves figuring out the address, port, and proper parameters to send to the server.

How to Run
Running the Server:

Before running the Python script, you need to first run the server. The server is launched via an executable file (.exe).

After running the executable, open a web browser and navigate to http://127.0.0.1:8888. This will start interacting with the application and be ready for the PIN attempts.

Running the Python Script:

Open the project folder in Visual Studio Code (or any Python IDE).

Ensure that you have Python installed on your system.

Install any required dependencies (like requests), if not already installed.

Run the Python script by executing it in the terminal:

python brute_force.py
The script will automatically try all 3-digit PIN combinations and attempt to log in. It will output progress to the console.

How I Approached the Challenge
Finding the Address and Port:
I used Wireshark to capture network traffic when running the provided .exe file.
By observing the packets, I found that the application was listening on 127.0.0.1 (localhost) and port 8888.

Determining What to Send:
Using Wireshark, I followed the HTTP stream of the captured packets.
In the HTML response, I saw that the server expects a field named magicNumber for the PIN input.
So in my script, I formatted my requests to send the PIN using magicNumber as the field name.

Handling Constraints:
The server had a rate limiter that triggered if too many requests were sent too quickly (showing "Whoa, slow down!").
I added a time delay (time.sleep(4)) between each attempt to avoid getting blocked.

Lessons Learned:
I learned how rate-limiting can slow down brute-force attacks, and how to read and interpret network traffic using Wireshark.

Security Improvements (Recommendations):

Implement lockout mechanisms after several wrong attempts.

Require longer passwords instead of simple 3-digit PINs.

Rate-limit by IP address aggressively and implement CAPTCHA after repeated failures.

