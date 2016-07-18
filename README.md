# heathersdaughterv2

get:
- python3
- node 6.x
- heroku cli

run:
- virtualenv hd-env
- source hd-env/bin/activate
- pip install -r requirements.txt
- npm install (should run bower install and grunt automatically)

hook up heroku remote:
- heroku git:remote -a heathersdaughterv2

then you can run with
- heroku local
