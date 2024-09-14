# Dish Rating API

This is a RESTful API for a MealRater application. It allows users to create, read, update, and delete meals and their ratings.

## Endpoints

### Meals

- `GET /api/meals/` - Get a list of all meals
- `GET /api/meals/{id}/` - Get a specific meal by id
- `POST /api/meals/` - Create a new meal
- `PUT /api/meals/{id}/` - Update a specific meal by id
- `DELETE /api/meals/{id}/` - Delete a specific meal by id

### Ratings

- `GET /api/meals/{id}/ratings/` - Get a list of all ratings for a specific meal by id
- `POST /api/meals/{id}/ratings/` - Create a new rating for a specific meal by id

### Rate Meal

- `POST /api/meals/{id}/rate/` - Rate a specific meal by id. The request data should include the 'stars' and 'username' fields.

