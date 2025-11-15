# Weather Microservice

A Flask-based weather microservice that provides simulated weather data for various cities. The service runs on port 5055 and offers a simple REST API for retrieving weather information.

## Features

- Get weather data for specific cities
- Retrieve list of available cities
- Simulated real-time weather data including temperature, conditions, humidity, and wind speed
- Easy-to-use REST API

## Installation

1. **Create a virtual environment:**
   ```python
   # Run in your terminal or command prompt:
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   
   On Windows:
   ```python
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```python
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```python
   pip install -r requirements.txt
   ```

4. **Start the microservice:**
   ```python
   python weather_service.py
   ```

   The service will start on `http://localhost:5055`

## API Endpoints

### 1. Home Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns service information and available endpoints

### 2. Get Available Cities
- **URL:** `/weather/cities`
- **Method:** `GET`
- **Description:** Returns a list of cities with available weather data

### 3. Get Weather Data
- **URL:** `/weather`
- **Method:** `GET`
- **Query Parameters:** 
  - `city` (required): Name of the city
- **Description:** Returns current weather data for the specified city

## How to REQUEST Data from the Microservice

To request data from the microservice, send an HTTP GET request to the appropriate endpoint.

### Example Request - Using Python:

```python
import requests

# Request weather data for New York
response = requests.get('http://localhost:5055/weather?city=New York')
data = response.json()
print(data)
```

### Example Request - Using JavaScript (fetch):

```javascript
fetch('http://localhost:5055/weather?city=New York')
    .then(response => response.json())
    .then(data => console.log(data));
```

### Example Request - Using Another Python Program:

```python
import requests

# In your client Python application
def get_weather_data(city_name):
    """Request weather data from the microservice"""
    try:
        response = requests.get(f'http://localhost:5055/weather?city={city_name}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error connecting to microservice: {e}")
        return None

# Use it in your program
weather = get_weather_data('New York')
if weather:
    print(f"Temperature: {weather['temperature']}°F")
```

## How to RECEIVE Data from the Microservice

The microservice returns data in JSON format. You need to parse the JSON response to extract the weather information.

### Example Response:

```json
{
  "city": "New York",
  "temperature": 72,
  "temperature_unit": "Fahrenheit",
  "condition": "Sunny",
  "humidity": "65%",
  "wind_speed": "12 mph",
  "timestamp": "2024-11-15T21:30:00.123456"
}
```

### Example - Receiving and Processing Data in Python:

```python
import requests

# Make the request
response = requests.get('http://localhost:5055/weather?city=London')

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and use the data
    city = weather_data['city']
    temperature = weather_data['temperature']
    condition = weather_data['condition']
    humidity = weather_data['humidity']
    wind_speed = weather_data['wind_speed']
    
    print(f"Weather in {city}:")
    print(f"  Temperature: {temperature}°F")
    print(f"  Condition: {condition}")
    print(f"  Humidity: {humidity}")
    print(f"  Wind Speed: {wind_speed}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
```

### Example - Receiving Data in JavaScript:

```javascript
async function getWeather(city) {
    try {
        const response = await fetch(`http://localhost:5055/weather?city=${city}`);
        
        if (response.ok) {
            const data = await response.json();
            
            console.log(`Weather in ${data.city}:`);
            console.log(`  Temperature: ${data.temperature}°F`);
            console.log(`  Condition: ${data.condition}`);
            console.log(`  Humidity: ${data.humidity}`);
            console.log(`  Wind Speed: ${data.wind_speed}`);
        } else {
            console.error('Error:', response.status);
        }
    } catch (error) {
        console.error('Failed to fetch weather data:', error);
    }
}

getWeather('Tokyo');
```

## Available Cities

The following cities have weather data available:
- New York
- London
- Tokyo
- Paris
- Sydney

## Testing the Service

A comprehensive test suite is included to verify the microservice functionality.

**Run the tests:**

1. First, start the weather service in one terminal/command prompt:
   ```python
   python weather_service.py
   ```

2. In another terminal/command prompt, run the test suite:
   ```python
   python test_weather_service.py
   ```

The test suite will verify:
- Home endpoint functionality
- City listing
- Valid city weather requests
- Invalid city handling
- Missing parameter handling
- Multiple city requests

## UML Sequence Diagram

The following diagram illustrates how requesting and receiving data works with the Weather Microservice:

```
Client Application                Weather Microservice
        |                                  |
        |   HTTP GET /weather?city=London  |
        |--------------------------------->|
        |                                  |
        |         [Process Request]        |
        |         [Validate City]          |
        |         [Generate Weather Data]  |
        |                                  |
        |   HTTP 200 OK                    |
        |   JSON Response:                 |
        |   {                              |
        |     "city": "London",            |
        |     "temperature": 55,           |
        |     "condition": "Rainy",        |
        |     ...                          |
        |   }                              |
        |<---------------------------------|
        |                                  |
        |   [Parse JSON Response]          |
        |   [Extract Data Fields]          |
        |   [Display/Use Weather Data]     |
        |                                  |


Alternative Flow - Invalid City:

Client Application                Weather Microservice
        |                                  |
        |   HTTP GET /weather?city=Mars    |
        |--------------------------------->|
        |                                  |
        |         [Process Request]        |
        |         [Validate City]          |
        |         [City Not Found]         |
        |                                  |
        |   HTTP 404 Not Found             |
        |   JSON Response:                 |
        |   {                              |
        |     "error": "Weather data...",  |
        |     "available_cities": [...]    |
        |   }                              |
        |<---------------------------------|
        |                                  |
        |   [Handle Error]                 |
        |   [Display Error Message]        |
        |                                  |
```

## Communication Contract

### Request Format:
- **Protocol:** HTTP
- **Method:** GET
- **URL Pattern:** `http://localhost:5055/weather?city={city_name}`
- **Headers:** None required
- **Body:** None (query parameter used)

### Response Format:
- **Content-Type:** `application/json`
- **Success Status Code:** 200
- **Error Status Codes:** 400 (Bad Request), 404 (Not Found)

### Data Fields:
| Field | Type | Description |
|-------|------|-------------|
| city | string | Name of the city |
| temperature | integer | Temperature value |
| temperature_unit | string | Unit of temperature (Fahrenheit) |
| condition | string | Weather condition description |
| humidity | string | Humidity percentage |
| wind_speed | string | Wind speed with unit |
| timestamp | string | ISO format timestamp of data generation |

## Error Handling

### Missing City Parameter (400 Bad Request):
```json
{
  "error": "City parameter is required",
  "example": "/weather?city=New York"
}
```

### Invalid City (404 Not Found):
```json
{
  "error": "Weather data not available for Mars",
  "available_cities": ["New York", "London", "Tokyo", "Paris", "Sydney"]
}
```

## Port Configuration

The service runs on **port 5055** by default. If you need to change the port, modify the last line in `weather_service.py`:

```python
app.run(host='0.0.0.0', port=5055, debug=True)
```

## Notes

- The weather data is simulated and randomly generated for demonstration purposes
- Each request generates new random weather data within realistic ranges for each city
- The service is designed for development/testing and should not be used in production without proper security measures
- CORS is not configured by default; add Flask-CORS if cross-origin requests are needed

## License

This is a sample microservice for educational purposes.
