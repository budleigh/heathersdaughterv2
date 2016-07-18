# heathersdaughterv2

get:
- python3
- node 6.x

run:
- virtualenv hd-env
- source hd-env/bin/activate
- pip install -r requirements.txt
- npm install (should run bower install automatically)

if needed, hook up heroku remote:
- heroku git:remote -a heathersdaughterv2

then you can run either by
- python hd.py
or
- heroku local
