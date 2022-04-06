A Very Easy Recommendation Engine for Django
===

Installation
---

```
pip install very-easy-recommendation-engine-django
```

Configuration
---

Let's say you have a model for movies and ratings of movies like so:

```
"""
movies/models.py
"""

class Movie(models.Model):
    title = models.CharField()


class Rating(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(min=1, max=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

We will build a recommendation engine to show movies a user might like based on their ratings.


```
"""
settings.py
"""

VERY_EASY_RECOMMENDATION_ENGINE = {
    "APPLICATION_ID": "{{ Your Application ID key here }}"
    "API_KEY": "{{ Your secret key here }}"
    "models": {
      "user_movie_recommendations": {
          "output_field": "books.Rating.value"
      }
    }
}
```

```
"""
urls.py
"""

urlpatterns = [
  ...,
  path("very-easy-ai", "very_easy_recommendation_engine.urls")
]
```

That's it! Our servers will start building your recommendation engine and provide an API endpoint for your application to pull recommendations


Getting Recommendations
---

Request:
```
from very_easy_recommendation_engine import VeryEasyRecommendationEngine

rec_engine = VeryEasyRecommendationEngine(model_name="user_movie_recommendations")

# Get recommendations for user number five
recommendations = rec_engine.get_recommendations_for_user(user_id=5)

print(recommendations, limit=15)
```

Output:
```
{
  "results": [
      {
        "objectId": "objectId1",
        "value": 4.89
        // ...
      },
      {
        "objectId": "objectId2",
        "value": 4.87
        // ...
      }
      //...
    ],
    "count": 15,
    "queryId": "43b15df305339e827f0ac0bdc5ebcaa7"
  ]
}
```
