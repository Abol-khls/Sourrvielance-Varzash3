# Sourrvielance — a tiny, friendly link collector



This little script quietly polls the Varzesh3 "most visited" news API and saves the article links it finds into `links.txt`.


**What this repo contains**

- `1.py`: the small Python script that fetches the API and writes links.

- `links.txt`: created by the script; contains one URL per line.



**What it does**

- Every 120 seconds the script requests the "most visited" endpoint from Varzesh3.

- Collected links are saved to `links.txt` in UTF‑8 format.



**Optional but recommended**

1. Make a virtual environment and activate it.

## Installation

1.  Clone this repository:

    ```sh
    git clone https://github.com/Abol-khls/Get-Links-Frome-Varzash3.com.git
    ```

3.  Install Python virtual environment:

    ```sh
    python -m venv .venv
    ```

4.  activate Python virtual environment:

    ```sh
    .venv\Scripts\activate
    ```




5. Install the required package:




   ```powershell

   pip install requests

   ```



5. Run the script:



   ```powershell

   python 1.py

   ```



4. Open `links.txt` to see the saved URLs.



**Use**

Use this script responsibly. Make sure your use follows Varzesh3's API rules and local laws.

## License

MIT License


