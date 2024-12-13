# PROJECT TITLE
Real Estate API

## Introduction
The Real Estate API is a powerful tool designed for developers and real estate professionals to access and manage property listings and user favorites. This API allows users to efficiently search for properties and view detailed information.

## API Endpoints

### 1. List Properties
- **URL**: `/properties`
- **Method**: `GET`
- **Description**: Fetch a list of available properties with essential details.
- **Query Parameters**:
  - `city` (optional): Filter properties by city name.
  - `price_min` (optional): Minimum price for filtering properties.
  - `price_max` (optional): Maximum price for filtering properties.
  - `property_type` (optional): Type of property (e.g., apartment, house).
- **Response**:
  - A JSON array of properties, each containing:
    - `id`: Unique identifier for the property
    - `address`: Property address
    - `city`: City where the property is located
    - `price`: Listing price
    - `property_type`: Type of property
    - `description`: Brief description of the property

### 2. Get Property Details
- **URL**: `/properties/{id}`
- **Method**: `GET`
- **Description**: Retrieve detailed information about a specific property.
- **Path Parameters**:
  - `id`: The unique ID of the property.
- **Response**:
  - A JSON object containing detailed property information, including:
    - `id`
    - `address`
    - `price`
    - `property_type`
    - `square_footage`
    - `bedrooms`
    - `bathrooms`
    - `additional_description`

### 3. Location Information
- **URL**: `/location-info`
- **Method**: `GET`
- **Query Parameters**:
  - `latitude` and `longitude` or `address`: Required to specify the location.
- **Response**:
  - A JSON object with apartments within that location.
  

### 4. Favorites Management
- **URL**: `/favorites`
- **Method**: `POST` / `GET`
- **Description**: Save and retrieve favorite properties for users.
- **Request Body** (for `POST`):
  - `user_id`: The ID of the user.
  - `property_id`: The ID of the property to be added to favorites.
- **Response**:
  - For `GET`: A list of properties saved by the user.
  - For `POST`: Confirmation of the property added to favorites.

## Getting Started

### Prerequisites
- python (version 12 or higher)
- Django 

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/cleoivvy/estate-api.git
