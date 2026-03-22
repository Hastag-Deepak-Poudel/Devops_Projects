To run this application successfully:

1. clone the repo
2. go inside flaskapp directory and activate the virtual environment by:
        source myenv/bin/activate     ---------> In terminal
3. install dependencies by using: pip install -r requirements.txt
4. Check if the program is running successfully by: python3 app.py
5. create a .service file of project if you want to run it 24/7


            (OPTIONAL)
6.          sudo nano /etc/systemd/system/flaskapp.service
            [Unit]
            Description=Gunicorn instance to serve flaskapp
            After=network.target

            [Service]
            User=sammy
            Group=www-data
            WorkingDirectory=/home/user/flaskapp
            Environment="PATH=/home/user/Desktop/flaskapp/myprojectenv/bin"
            ExecStart=/home/user/Desktop/flaskapp/flaskapp/env/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

            [Install]
            WantedBy=multi-user.target     # { note: in 'user' write your pc 'username}


7.  sudo systemctl start myproject
    sudo systemctl enable myproject


8. sudo systemctl status myproject

9. sudo nano /etc/nginx/sites-available/flaskapp    {creating a conf file in sites-available}

10. server {
        listen 80;
        server_name _;

        location / {
            proxy_pass http://unix:/home/sammy/myproject/myproject.sock; // If you are using gunicorn 
            proxy_pass http://127.0.0.1:5000;
        }

    }

11. delete default sym link 
    sudo rm -s /etc/nginx/sites-enabled

    create a sym link
    sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled

12. Open browser and search for localhost:80, your flask app page will appear.