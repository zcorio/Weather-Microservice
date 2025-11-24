import requests
import time

BASE_URL = 'http://localhost:5055'


def test_home_endpoint():
    print("\n" + "="*50)
    print("Testing Home Endpoint")
    print("="*50)
    
    try:
        response = requests.get(f'{BASE_URL}/')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the service. Make sure it's running on port 5055")
        return False


def test_get_cities():
    print("\n" + "="*50)
    print("Testing Get Cities Endpoint")
    print("="*50)
    
    try:
        response = requests.get(f'{BASE_URL}/weather/cities')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the service. Make sure it's running on port 5055")
        return False


def test_get_weather_valid_city():
    print("\n" + "="*50)
    print("Testing Get Weather - Valid City (New York)")
    print("="*50)
    
    try:
        response = requests.get(f'{BASE_URL}/weather?city=New York')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the service. Make sure it's running on port 5055")
        return False


def test_get_weather_invalid_city():
    print("\n" + "="*50)
    print("Testing Get Weather - Invalid City (Mars)")
    print("="*50)
    
    try:
        response = requests.get(f'{BASE_URL}/weather?city=Mars')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 404
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the service. Make sure it's running on port 5055")
        return False


def test_get_weather_missing_parameter():
    print("\n" + "="*50)
    print("Testing Get Weather - Missing Parameter")
    print("="*50)
    
    try:
        response = requests.get(f'{BASE_URL}/weather')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 400
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the service. Make sure it's running on port 5055")
        return False


def test_multiple_cities():
    print("\n" + "="*50)
    print("Testing Multiple Cities")
    print("="*50)
    
    cities = ['London', 'Tokyo', 'Paris']
    all_passed = True
    
    for city in cities:
        try:
            response = requests.get(f'{BASE_URL}/weather?city={city}')
            print(f"\n{city}:")
            print(f"  Status Code: {response.status_code}")
            print(f"  Temperature: {response.json().get('temperature')}°F")
            print(f"  Condition: {response.json().get('condition')}")
            
            if response.status_code != 200:
                all_passed = False
        except requests.exceptions.ConnectionError:
            print(f"ERROR: Cannot connect to the service for {city}")
            all_passed = False
    
    return all_passed


def run_all_tests():
    print("\n" + "="*70)
    print("WEATHER MICROSERVICE TEST SUITE")
    print("="*70)
    print("Make sure the weather service is running before running these tests!")
    print("Start it with: python weather_service.py")
    
    time.sleep(1)
    
    tests = [
        ("Home Endpoint", test_home_endpoint),
        ("Get Cities", test_get_cities),
        ("Get Weather - Valid City", test_get_weather_valid_city),
        ("Get Weather - Invalid City", test_get_weather_invalid_city),
        ("Get Weather - Missing Parameter", test_get_weather_missing_parameter),
        ("Multiple Cities", test_multiple_cities)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\nERROR in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed = sum(1 for _, result in results if result)
    print(f"\nTotal: {passed}/{total} tests passed")
    print("="*70 + "\n")


if __name__ == '__main__':
    run_all_tests()
