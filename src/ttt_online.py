from time import time
from requests import Session

class TttOnline:
    def __init__(self) -> None:
        self.api = "https://keralamedia.online/crisscross"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G9880 Build/RP1A.2007201.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
            "X-Requested-With": "com.web.tictactoeonlineplayers2"
        }
        self.player_id = None

    def check_username(self, username: str) -> dict:
        return self.session.get(
            f"{self.api}/check_username.php?pname={username}").json()

    def get_country(self) -> dict:
        return self.session.get(f"{self.api}/get_country.php").json()

    def get_date(self) -> dict:
        return self.session.get(f"{self.api}/get_date.php").json()

    def login(self, email: str) -> dict:
        response = self.session.get(
            f"{self.api}/login_user.php?pemail={email}").text
        self.player_id = response.split(":*")[0]
        return response

    def check_ban(self, player_id: int) -> dict:
        return self.session.get(
            f"{self.api}/check_ban.php?pid={player_id}").json()

    def update_profile(
            self,
            username: str,
            player_id: int,
            picture: str = "profiles/icon_add.png",
            score: int = 0,
            cs: int = 0,
            country_code: str = "sk") -> str:
        return self.session.get(
            f"{self.api}/update_pid.php?name={username}&pic={picture}&score={score}&pid={player_id}&cs={cs}&flager=https://flagcdn.com/48x36/{country_code}.png&city=NA").text

    def get_recent_players(self) -> dict:
        return self.session.get(
            f"{self.api}/get_recent.php").json()

    def get_player_defeats(self, player_id: int) -> dict:
        return self.session.get(
            f"{self.api}/get_defeats.php?pid={player_id}").json()        

    def get_top_20(self) -> str:
        return self.session.get(
            f"{self.api}/get_top_20.php").text

    def get_player_email(self, player_id: int) -> dict:
        return self.session.get(
            f"{self.api}/get_email.php?pid={player_id}").json()

    def check_email(self, email: str) -> dict:
        return self.session.get(
            f"{self.api}/check_email.php?cemail={email}").json()

    def send_token(
            self,
            username: str,
            email: str) -> dict:
        return self.session.get(
            f"{self.api}/send_token.php?pemail={email}&pname={username}").json()

    def set_champions(self, player_id: int) -> dict:
        return self.session.get(
            f"{self.api}/set_champions.php?pid1={player_id}&pid2={player_id}").json()

    def set_email(
            self,
            player_id: int,
            email: str) -> str:
        return self.session.get(
            f"{self.api}/set_final_email.php?pemail={email}&pid={player_id}").text
