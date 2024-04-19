# Specify a base image
FROM node:18-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the client app
COPY . .

# Build the project for production
RUN npm run build

# Expose port and start application
EXPOSE 3000
CMD ["npm", "start"]
