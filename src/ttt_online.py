from time import time
from requests import Session, Response

class TttOnline:
	def __init__(self) -> None:
		self.api = "https://keralamedia.online/crisscross"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G9880 Build/RP1A.2007201.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
			"X-Requested-With": "com.web.tictactoeonlineplayers2"
		}
		self.player_id = None

	def _get(self, endpoint: str, params: dict = {}) -> Response:
		return self.session.get(
			f"{self.api}{endpoint}", params=params)

	def check_username(self, username: str) -> dict:
		params = {
			"pname": username
		}
		return self._get(
			"/check_username.php", params).json()

	def get_country(self) -> dict:
		return self._get("/get_country.php").json()

	def get_date(self) -> dict:
		return self._get("/get_date.php").json()

	def login(self, email: str) -> dict:
		params = {
			"pemail": email
		}
		response = self._get(
			"/login_user.php", params).text
		self.player_id = response.split(":*")[0]
		return response

	def check_ban(self, player_id: int) -> dict:
		params = {
			"pid": player_id
		}
		return self._get(
			"/check_ban.php", params).json()

	def update_profile(
			self,
			username: str,
			player_id: int,
			picture: str = "profiles/icon_add.png",
			score: int = 0,
			cs: int = 0,
			country_code: str = "sk",
			city: str = "NA") -> str:
		params = {
			"name": username,
			"pic": picture,
			"score": score,
			"pid": player_id,
			"cs": cs,
			"flager": f"https://flagcdn.com/48x36/{country_code}.png",
			"city": city
		}
		return self._get("/update_pid.php", params).text

	def get_recent_players(self) -> dict:
		return self._get("/get_recent.php").json()

	def get_player_defeats(self, player_id: int) -> dict:
		return self._get("/get_defeats.php?pid={player_id}").json()        

	def get_top_20(self) -> str:
		return self._get("/get_top_20.php").text

	def get_player_email(self, player_id: int) -> dict:
		params = {
			"pid": player_id
		}
		return self._get("/get_email.php", params).json()

	def check_email(self, email: str) -> dict:
		params = {
			"cemail": email
		}
		return self._get("/check_email.php", params).json()

	def send_token(
			self,
			username: str,
			email: str) -> dict:
		params = {
			"pemail": email,
			"pname": usernamea
		}
		return self._get("/send_token.php", params).json()

	def set_champions(self, player_id: int) -> dict:
		params = {
			"pid1": player_id,
			"pid2": player_id
		}
		return self._get("/set_champions.php", params).json()

	def set_email(
			self,
			player_id: int,
			email: str) -> str:
		params = {
			"pemail": email,
			"pid": player_id
		}
		return self._get("/set_final_email.php", params).text
