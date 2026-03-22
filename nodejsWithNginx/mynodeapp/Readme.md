do npm install 
run node app.js

install nginx
sudo systemctl enable nginx
sudo system start nginx

do:
sudo vim /etc/nginx/conf.d/nodeapp.conf
        inside the .conf file, write: server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}

then restart nginx
run app.js (keep it running)
go to web browser then do, <------------------------------------|
    search: http://127.0.0.1 or localhost                       |
                                                                |
    you will be redirected to your website                      |
                                                                |
if some errors then do,                                         |           
                                                                |   
sudo tail -f /var/log/nginx/error.log                           |        
                                                                |   
if you see something like Permission Denied, then do            |
                                                                |    
sudo setsebool -P httpd_can_network_connect 1                   |       
                                                                |    
                                                                |    
then restart nginx                                              |
then do in line 21       -----------------------------------------

