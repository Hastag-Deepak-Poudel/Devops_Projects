FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

# We copy everything, but in Dev, we usually 
# override this with a "Volume" in docker-compose
COPY . .

EXPOSE 3000

# Use a dev command (like nodemon) instead of 'node ./app.js'
CMD ["node", "app.js"]
