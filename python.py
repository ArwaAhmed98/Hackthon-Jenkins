import requests

webhook_url = "https://vodafone.webhook.office.com/webhookb2/eb0c06d1-590f-4bac-b21d-fd6a41e86cde@68283f3b-8487-4c86-adb3-a5228f18b893/IncomingWebhook/471c53e15e7d4ddb9fc6fdc5eb0c6001/8073a3a4-4a6a-4909-bacf-f7eff6c2fcc4"
message = {
    "text": "{jenkins_url}/job/{job_name}/{build_number}/"
}
response = requests.post(webhook_url, json=message)
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")

http://{jenkins_url}/job/{job_name}/{build_number}/
