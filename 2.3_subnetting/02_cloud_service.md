Connecting Raspberry Pi to EMQX Cloud
A Practical Guide to Cloud-Based MQTT Communication

Equipment and software:

Raspberry Pi with Raspberry Pi OS.
Internet connection.
Python 3.
EMQX Cloud account.
Paho MQTT Python library.
1. Introduction to EMQX Cloud
EMQX Cloud provides a hosted MQTT broker that allows IoT devices to exchange messages over the internet.

Unlike a locally installed broker, such as Eclipse Mosquitto, EMQX Cloud runs on remote servers.

This means that your Raspberry Pi can communicate with other devices without needing to host its own MQTT broker.

For this activity, we will use the EMQX Serverless free tier.

The current free quota includes:

1 million session minutes per month.
1 GB of network traffic per month.
1 million rule actions per month.
The free quota is subject to EMQX's usage conditions and limits. We will configure the spending limit to zero to avoid charges beyond the free allowance.

2. Create an EMQX Cloud Account
Open the EMQX Cloud website:
https://www.emqx.com/en
Select the option to register for an account.
Enter your email address and the requested details.
Complete the email verification process.
Log in to the EMQX Cloud Console.
You may be asked to complete mobile verification during registration.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/77f38d3d-75da-4411-b841-2b5a2fccba2a" />

3. Create Your First MQTT Deployment
After logging in, you need to create a project and an MQTT broker.

3.1 Create a project
Open the Overview page.
Select New Project.
Enter a project name, for example:
University-IoT-Lab
Add a short description if requested.
Select Confirm.
3.2 Create a Serverless deployment
Open your newly created project.
Select New Deployment.
Choose the Serverless plan.
Configure your deployment:
Deployment name: student01-broker
Region: Select a region close to your location.
Spend limit: Leave it at 0 to restrict usage to the free quota.
Review the deployment details.
Accept the usage terms.
Select Deploy.
Wait until the deployment status changes to Running.

Your MQTT broker is now ready.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1b07a4ad-fe6f-4072-a014-fee217129c94" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cbc1316c-259c-4422-9548-dbaf916217ec" />

4. Create MQTT Credentials
Your Raspberry Pi needs authentication details to connect to the broker.

Open your deployment.
Navigate to Access Control.
Select Authentication.
Select Add.
Enter the following:
Username: student01
Password: Create a secure password.
Select Confirm.
Keep your credentials safe. You will need them when connecting your Raspberry Pi.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb5cf1e8-c411-469b-8492-6295e410a074" />

5. Retrieve Your MQTT Connection Details
Open the Overview page of your deployment.

You should find the following information:

Parameter	Description
Host	Your unique EMQX broker address
Port	8883
Protocol	MQTT over TLS
Username	Your MQTT username
Password	Your MQTT password
Your broker address will look similar to:

xxxxxxxxxx.emqxsl.com
Use the actual hostname displayed in your account.

rbbfb765.ala.eu-central-1.emqxsl.com

Download the CA certificate
EMQX Serverless requires encrypted connections.

Find the CA Certificate option in your deployment Overview.
Download the certificate.
Save it somewhere accessible from your Raspberry Pi (in the same folder where you will create your Python scripts).
You will need this certificate to establish a secure connection.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dd5836e3-2b29-486a-b417-4213d4046ce3" />

Important: Do not use port 1883 for this Serverless deployment. Use port 8883 with TLS encryption.
