# toribio bota


Eibarko Euskararen hiztegiko sarrerak Twiterrera bidaltzen dituen robota.

Inspirazioa: https://github.com/ZiTAL/bermiotarra

Erabilitako baliabideak: Eibarko Euskararen Hiztegia http://www.eibarko-euskara.eus/hiztegia


## Zergatik?

Eta zergatik ez?

## Nola dabil hau?

Bi script daude hemen, lehenengoak hiztegi guztia deskargatzen du Internetetik, www.eibarko-euskara.eus webguneko hiztegiaren orrialde guztiak irakurriz, eta JSON fitxategi baten gordetzen du.

Bigarren scriptak, JSON fitxategi hori irakurtzen du eta ausaz sarrera bat aukeratu eta Twitterrera bidaltzen du. Ondoren sarrera hori markatu egiten du hurrengo baten ez dezan berriz ere txiokatu.

## Twitter kredentzialak

Honek ondo funtzionatzeko Twitterren aplikazio bat erregistratu behar duzu eta han lortutako APIaren gakoak JSON formatuan gorde `credentials.twitter.json` izeneko fitxategi baten. Fitxategiaren formatua horrelakoa izan behar da:

```json
{
  "API_KEY": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "API_SECRET": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "BEARER_TOKEN": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "ACCESS_TOKEN_KEY": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "ACCESS_TOKEN_SECRET": "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
}


```


## Lizentzia

GNU GPLv3
