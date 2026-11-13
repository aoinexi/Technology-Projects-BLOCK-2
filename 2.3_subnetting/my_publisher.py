import ssl
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

msgs = [
	{'topic': "my test", 'payload': "test 1"},
	("my test", "test 2", 0, False)
]

sslSettings = ssl.create_default_context(
	cafile="emqxs;-ca.crt"
)

auth = {
	'username': "aoinexi"
	'password': "VbnM_12@34"
}

publish.multiple(
	msg,
	hostname="HOSTNAME",
	port=8883,
	auth=auth
	tls=sslSettings,
	protocol=paho.MQTTv311
)

print("Messages published successfully!")
