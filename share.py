import requests

# script en construction pour rétablir la vérité
# traiter la requete du partage de son

user = "https://soundcloud.com/user-943061607"
url = "/verite/s-Phyl7UCt7H5?si=e601cf61747545cd95377537053cb091&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"

def share():
  requests.get(user + url)

if isDead:
  share()
