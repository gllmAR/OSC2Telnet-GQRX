## OSC2TelnetGQRX.py

### description

Transforme un message OSC (/F (int) ) en commande Telnet pour GQRX

### Requis

*  pyosc
```
sudo easy_install pip
sudo pip install pyosc
```
v2 _ transition vers de pythonOSC vers pyOSC https://github.com/ptone/pyosc

### Installation

		python OSC2TelnetGQRX.py


### Troubleshoot


* Si  :

 		sock.connect(sa)
		ConnectionRefusedError: [Errno 61] Connection refused
	*  S'assurer que l'application GQRX est lancé
	*  S'assurer que GQRX fonctionne (violet)
	*  S'assurer que le bouton de contrôle Telnet (vert)
	*  ![](assets/gqrxToolbar.png)
