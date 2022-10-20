# Cloud 3
# show_policy():
#     page = render_template('privacy.html')
#     return page


# if __name__ == '__main__':

#     def say_hello():
#     page = render_template('index.html')
#     return page

# @app.route('/privacy', methods=['GET'])
# def show_policy():
#     page = render_template('privacy.html')
#     return page


# if __name__ == '__main__':
#     # This is used when running locally, only to verify it does not have
#     # significant errors. It cannot demonstrate restricting access using
#     # Identity-Aware Proxy when run locally, only when deployed.
#     #
#     # When deploying to Google App Engine, a webserver process such as
#     # Gunicorn will serve the app. This can be configured by adding an
#     # `entrypoint` to app.yaml.
#     app.run(host='127.0.0.1', port=8080, debug=True)





gcloud command line
This is the gcloud command line with the parameters you have selected. gcloud reference 




gcloud compute networks create managementnet --project=qwiklabs-gcp-03-b317955146bf --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional


gcloud compute networks subnets create managementsubnet-us --project=qwiklabs-gcp-03-b317955146bf --range=10.130.0.0/20 --stack-type=IPV4_ONLY --network=managementnet --region=us-central1




gcloud compute --project=qwiklabs-gcp-03-b317955146bf firewall-rules create managementnet-allow-icmp-ssh-rdp --direction=INGRESS --priority=1000 --network=managementnet --action=ALLOW --rules=tcp:22,tcp:3389,icmp --source-ranges=0.0.0.0/0