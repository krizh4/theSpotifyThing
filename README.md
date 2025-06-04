# theSpotifyThing

**theSpotifyThing** is a Python-based tool that extracts all track names from a specified Spotify playlist and saves them to a `.txt` file. Additionally, it offers the capability to download these tracks.

---

## 🚀 Features

- Extracts all track names from a Spotify playlist.
- Saves the extracted track names to `output.txt`.
- Downloads tracks for offline access.

---

## 🛠 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/krizh4/theSpotifyThing.git
cd theSpotifyThing
```


### 2. Set Up Spotify API Credentials

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an app to get your **Client ID** and **Client Secret**.
- Create a file named `vars.py` in the project root with the following content:

  ```vars.py
  client_id = 'your_spotify_client_id'
  client_secret = 'your_spotify_client_secret'
  ```


### 3. Install Dependencies
```bash
pip install -r requirements.tx
```

### 4. Run the Script


Follow the prompt to enter the playlist URL. The script will generate `output.txt` and optionally download the tracks.
```bash
python main.py
```
---

## 📄 Output

- `output.txt` — Contains all track names from the specified playlist.
- Downloaded tracks will be saved to a folder if enabled.

---

## 📝 Notes

- Make sure the playlist is public or accessible via your Spotify credentials.
- Track downloads may depend on availability and Spotify’s usage policy.

---

## 🤝 Contributing

Contributions are welcome! Fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
