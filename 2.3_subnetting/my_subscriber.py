import ssl
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe

# Callback function to print incoming messages
def print_msg(client, userdata, message):
    print(
        "{} : {}".format(
            message.topic,
            message.payload.decode()
        )
    )

# Use TLS for a secure connection with EMQX Cloud
sslSettings = ssl.create_default_context(
    cafile="emqxsl-ca.crt"
)

# Enter your EMQX Cloud credentials
auth = {
    'username': "aoinexi",
    'password': "VbnM_12@34"
}

# Subscribe to the topic and exit cleanly on Ctrl+C
try:
    subscribe.callback(
        print_msg,
        "my test",
        hostname="rbbfb765.ala.eu-central-1.emqxsl.com",
        port=8883,
        auth=auth,
        tls=sslSettings,
        protocol=paho.MQTTv311
    )
except KeyboardInterrupt:
    print("\nSubscriber stopped.")
