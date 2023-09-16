# streamlit-app-project
Tooling for datascientists lecture - DSB 2023/24

This project aims to create a car insurance company customer information app using Streamlit and containerize it with Docker. The project utilizes a car insurance dataset to provide insights and visualize information through an interactive web application.

## Dataset

The chosen dataset contains customer information for a car insurance company. It includes various attributes such as gender, age, driving license status, region code, previous insurance status, vehicle age, vehicle damage, annual premium, policy sales channel.

## Repository Structure

The GitHub repository follows a specific structure to organize the project:

- **app**: This folder contains everything necessary to run the Streamlit app. It includes the app code, required dependencies, and the Dockerfile for containerization. Additionally, the "app" folder contains an empty **data** folder, which will be used to store dataset files.

## Data Source

The dataset for this project can be found on Dropbox. It consists of two main components:

1. **CSV Dataset**: The CSV file contains the car insurance customer information dataset, which serves as the primary data source for the application.

2. **Image**: An image file is included in the Dropbox link.

## Getting Started

To run the project, there are two ways:

**The first way:**

1. Open [Docker play](https://labs.play-with-docker.com/)

2. Select the ADD NEW INSTANCE
   
4. Run the following code :

    ```bash
   docker run -dp 0.0.0.0:3000:3000 msrichard/streamlitprojectrepo:final-app
   ```
5. Open port 3000. 

**Or follow the following steps:** 

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MarieSophieRichard/streamlit-app-project.git
   ```

2. Navigate to the "app" folder:

   ```bash
   cd app
   ```

3. Download data from Dropbox and but the two downloaded files in the **data** folder. [Dropbox link](https://www.dropbox.com/scl/fo/1f8ens3hb0z6zablb8hw2/h?rlkey=3t8lf0jzcd6mx5m171ie92zxo&dl=0)

4. Build the Docker image using the provided Dockerfile:

   ```bash
   docker build -t car-insurance-app .
   ```

6. Run the Docker container:

   ```bash
   docker run -p 8501:8501 car-insurance-app
   ```

7. Access the Streamlit app in your web browser at [http://localhost:8501](http://localhost:8501).

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests.
